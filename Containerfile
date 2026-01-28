# =============================================================================
# Python Template - Multi-stage Container Build
# =============================================================================
# Build: podman build -f Containerfile -t python-template:latest .
# Run:   podman run -p 8000:8000 python-template:latest
# =============================================================================

# -----------------------------------------------------------------------------
# Stage 1: Builder - Install dependencies with uv
# -----------------------------------------------------------------------------
FROM python:3.14-slim AS builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Set environment variables
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

WORKDIR /app

# Install dependencies first (better layer caching)
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# Copy source code and install project
COPY src/ ./src/
COPY README.md ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# -----------------------------------------------------------------------------
# Stage 2: Runtime - Minimal production image
# -----------------------------------------------------------------------------
FROM python:3.14-slim AS runtime

# Labels for container registry
LABEL org.opencontainers.image.title="Python Template" \
      org.opencontainers.image.description="A modern Python project template with FastAPI" \
      org.opencontainers.image.source="https://github.com/nahuel11500/python-template-project" \
      org.opencontainers.image.licenses="MIT"

# Create non-root user for security
RUN groupadd --gid 1000 appgroup && \
    useradd --uid 1000 --gid appgroup --shell /bin/bash --create-home appuser

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PATH="/app/.venv/bin:$PATH" \
    # Application settings
    HOST=0.0.0.0 \
    PORT=8000

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder --chown=appuser:appgroup /app/.venv /app/.venv

# Copy application source
COPY --from=builder --chown=appuser:appgroup /app/src /app/src

# Switch to non-root user
USER appuser

# Expose application port
EXPOSE 8000

# Health check for container orchestration
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Default command: run the API server
# Override with: podman run ... python-template:latest python-template hello
ENTRYPOINT ["python", "-m", "uvicorn", "python_template.api.app:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]

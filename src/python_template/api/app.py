"""FastAPI application setup."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from python_template import __app_name__, __version__
from python_template.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    """Application lifespan handler for startup/shutdown events."""
    # Startup
    yield
    # Shutdown


app = FastAPI(
    title=settings.app_name,
    version=__version__,
    description="A modern Python project template with FastAPI",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@app.get("/", tags=["root"])
async def root() -> dict[str, str]:
    """Root endpoint returning application info."""
    return {
        "name": __app_name__,
        "version": __version__,
        "status": "running",
    }


@app.get("/health", tags=["health"])
async def health() -> JSONResponse:
    """Health check endpoint for container orchestration."""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "version": __version__,
        },
    )

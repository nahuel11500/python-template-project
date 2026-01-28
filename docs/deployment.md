# Deployment

This guide covers deploying Python Template using containers.

## Container Build

The project uses a multi-stage `Containerfile` optimized for production:

### Build the Image

```bash
# Using just
just container-build

# Or directly with podman
podman build -f Containerfile -t python-template:latest .

# Or with docker
docker build -f Containerfile -t python-template:latest .
```

### Run Locally

```bash
# Using just
just container-run

# Or directly
podman run -p 8000:8000 python-template:latest
```

Visit http://localhost:8000 to verify the server is running.

### Container Features

- **Multi-stage build** - Smaller final image
- **Non-root user** - Security best practice
- **Health check** - Automatic container health monitoring
- **uv sync** - Fast, reproducible dependency installation

## GitHub Container Registry

### Automatic Publishing

Container images are automatically published to GitHub Container Registry (ghcr.io) on every release.

Images are tagged with:
- `latest` - Most recent release
- `v1.2.3` - Specific version
- `v1.2` - Minor version
- `v1` - Major version

### Pull the Image

```bash
# Pull latest
podman pull ghcr.io/nahuel11500/python-template-project:latest

# Pull specific version
podman pull ghcr.io/nahuel11500/python-template-project:v1.0.0
```

### Authentication Setup

The release workflow uses GitHub's built-in `GITHUB_TOKEN` for authentication. No additional secrets are required.

#### How It Works

1. The workflow has `packages: write` permission
2. It logs in to ghcr.io using `${{ github.actor }}` and `${{ secrets.GITHUB_TOKEN }}`
3. Images are pushed to `ghcr.io/<owner>/<repo>`

#### For Forks

If you fork this repository:

1. GitHub Actions will have access to `GITHUB_TOKEN` automatically
2. Images will be published to your fork's container registry
3. No additional configuration needed

## PyPI Publishing

### Automatic Publishing

Packages are automatically published to PyPI on every release using trusted publishing (OIDC).

### Setup Trusted Publishing

1. Go to https://pypi.org/manage/account/publishing/
2. Add a new "pending publisher":
   - **PyPI Project Name**: `python-template` (or your package name)
   - **Owner**: `nahuel11500` (your GitHub username/org)
   - **Repository**: `python-template-project`
   - **Workflow name**: `release.yml`
   - **Environment name**: `pypi`
3. The first release will claim the project name

### Benefits

- **No secrets stored** - Uses OIDC for authentication
- **More secure** - No API tokens to manage
- **Automatic** - Works out of the box after setup

## Environment Variables

Configure the container using environment variables:

```bash
podman run -p 8000:8000 \
  -e APP_NAME=my-app \
  -e DEBUG=false \
  -e LOG_LEVEL=INFO \
  python-template:latest
```

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | python-template | Application name |
| `DEBUG` | false | Enable debug mode |
| `HOST` | 0.0.0.0 | Server bind host |
| `PORT` | 8000 | Server bind port |
| `LOG_LEVEL` | INFO | Logging level |

## Health Checks

The container includes a health check endpoint:

```bash
curl http://localhost:8000/health
```

Response:
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

### Container Health Check

The Containerfile includes a built-in health check:

```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1
```

## Kubernetes Deployment

Example Kubernetes deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-template
spec:
  replicas: 3
  selector:
    matchLabels:
      app: python-template
  template:
    metadata:
      labels:
        app: python-template
    spec:
      containers:
        - name: python-template
          image: ghcr.io/nahuel11500/python-template-project:latest
          ports:
            - containerPort: 8000
          env:
            - name: LOG_LEVEL
              value: "INFO"
          livenessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 5
            periodSeconds: 30
          readinessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 5
            periodSeconds: 10
          resources:
            requests:
              memory: "128Mi"
              cpu: "100m"
            limits:
              memory: "256Mi"
              cpu: "500m"
---
apiVersion: v1
kind: Service
metadata:
  name: python-template
spec:
  selector:
    app: python-template
  ports:
    - port: 80
      targetPort: 8000
  type: ClusterIP
```

## Docker Compose

Example `docker-compose.yml`:

```yaml
version: "3.8"

services:
  app:
    image: ghcr.io/nahuel11500/python-template-project:latest
    ports:
      - "8000:8000"
    environment:
      - DEBUG=false
      - LOG_LEVEL=INFO
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 5s
    restart: unless-stopped
```

Run with:

```bash
docker-compose up -d
```

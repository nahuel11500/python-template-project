"""Command-line interface using Typer."""

import typer
from rich.console import Console

from python_template import __app_name__, __version__
from python_template.core.config import settings

app = typer.Typer(
    name=__app_name__,
    help="A modern Python project template CLI",
    add_completion=True,
    no_args_is_help=True,
)

console = Console()


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        console.print(f"[bold]{__app_name__}[/bold] version [green]{__version__}[/green]")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-V",
        help="Show version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """Python Template - A modern Python project template."""
    pass


@app.command()
def serve(
    host: str = typer.Option(settings.host, "--host", "-h", help="Host to bind to"),
    port: int = typer.Option(settings.port, "--port", "-p", help="Port to bind to"),
    reload: bool = typer.Option(settings.reload, "--reload", "-r", help="Enable auto-reload"),
) -> None:
    """Start the FastAPI server."""
    import uvicorn

    console.print(f"[bold green]Starting server at http://{host}:{port}[/bold green]")
    uvicorn.run(
        "python_template.api.app:app",
        host=host,
        port=port,
        reload=reload,
    )


@app.command()
def hello(
    name: str = typer.Argument("World", help="Name to greet"),
) -> None:
    """Say hello to someone."""
    console.print(f"[bold blue]Hello, {name}![/bold blue]")


@app.command()
def info() -> None:
    """Show application information."""
    from rich.table import Table

    table = Table(title="Application Info")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("App Name", settings.app_name)
    table.add_row("Version", __version__)
    table.add_row("Debug", str(settings.debug))
    table.add_row("Host", settings.host)
    table.add_row("Port", str(settings.port))
    table.add_row("Log Level", settings.log_level)

    console.print(table)


if __name__ == "__main__":
    app()

from fastapi import FastAPI
import tradingsignal


def add_root_route(app: FastAPI):
    """Add '/' route to return hello."""

    @app.get("/")
    async def root():
        """Check if the server is running and responds with the version."""
        return "Hello from TradingSignal Version: {}. Happy trading!!".format(tradingsignal.__version__)


def create_app():
    """Setup FastAPI server, server api"""

    app = FastAPI()
    add_root_route(app)

    return app

from fastapi import FastAPI
from se_tools import env_bool  # type: ignore[import-untyped]

from .di import Container
from .routes import router


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI(debug=env_bool('PRESENTATION_SERVICE_DEBUG'))

    app.container = container  # type: ignore[attr-defined]

    app.include_router(router)

    return app


app = create_app()

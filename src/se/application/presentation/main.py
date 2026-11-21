from fastapi import FastAPI
from se_tools import env_bool  # type: ignore[import-untyped]

from .routes import router

app = FastAPI(debug=env_bool('PRESENTATION_SERVICE_DEBUG'))

app.include_router(router)

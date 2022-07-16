from fastapi import FastAPI, APIRouter
from .api.endpoints.v1 import health_check, stats


default_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(default_router)
    application.include_router(health_check.router)
    application.include_router(stats.router)
    return application


app = get_application()

from fastapi import FastAPI

from .core.config import settings
from .core.logger import logger
from .routers import health

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    logger.info(f"🚀 Starting {settings.APP_NAME} in {settings.ENV} mode")
    yield
    # Shutdown code
    logger.info("Shutting down...")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan
)

app.include_router(health.router)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to FastAPI VIP 🚀"}
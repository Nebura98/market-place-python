from fastapi import FastAPI
from loguru import logger

from src.config import settings
from src.infrastructure import application
from src.presentation import endpoint

logger.add(
    "".join(
        [
            str(settings.root_dir),
            "/logs/",
            settings.logging.file.lower(),
            ".log",
        ]
    ),
    format=settings.logging.format,
    rotation=settings.logging.rotation,
    compression=settings.logging.compression,
    level="INFO",
)

app: FastAPI = application.create(
    debug=settings.debug,
    rest_routers=(
        endpoint.products_v1.router,
        endpoint.users_v1.router
    ),
    startup_tasks=[],
    shutdown_tasks=[],
)

import os
import sys

from loguru import logger


LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Убираем стандартные хендлеры
logger.remove()

logger.add(
    sys.stdout,
    colorize=False,
    format="<level>{level: <8}</level>:     {message}",
    level=LOG_LEVEL,
    enqueue=True,
)


def get_logger():
    return logger

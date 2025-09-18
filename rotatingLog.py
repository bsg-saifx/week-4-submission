import logging
from logging.handlers import TimedRotatingFileHandler
import os

if not os.path.exists("logs"):
    os.makedirs("logs")


logger = logging.getLogger("MyLogger")
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(
        filename="logs/app.log",
        when="D",
        interval=1,
        encoding="utf-8",
        utc=True
)

handler.suffix = "%Y-%m-%d_%H-%M-%S"

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("App started")
logger.warning("Warning message")
logger.error("This is an error")


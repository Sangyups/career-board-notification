import logging.config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


config = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)s]: %(filename)s:%(lineno)d - %(message)s"
        }
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "logs/main.log",
            "formatter": "default",
            "level": "INFO",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO",
        },
    },
    "root": {"handlers": ["file", "console"], "level": "INFO"},
}

logging.config.dictConfig(config)
logger = logging.getLogger()

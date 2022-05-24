import logging.config

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
            "filename": "./logs/main.log",
            "formatter": "default",
            "level": "INFO",
        },
    },
    "root": {"handlers": ["file"], "level": "INFO"},
}

logging.config.dictConfig(config)
logger = logging.getLogger()

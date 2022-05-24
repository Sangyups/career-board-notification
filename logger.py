import logging

logger = logging.getLogger()

logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler("./logs/main.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

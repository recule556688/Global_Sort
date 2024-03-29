import logging


def setup_logging():
    logging.basicConfig(  # Configure the logging module
        filename="User_Files/file_sorter.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )


def log_message(level, message):
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "critical":
        logging.critical(message)
    elif level == "debug":
        logging.debug(message)
    else:
        raise ValueError("Invalid level")

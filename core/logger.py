import logging
from logging import Logger, getLogger, Formatter, StreamHandler, INFO


def setting_logger(logger: Logger) -> Logger:

    formatter = Formatter(
        datefmt='%Y-%m-%d %H:%M:%S',
        fmt="%(levelname)s - %(asctime)s - %(name)s - (Line: %(lineno)d) - [%(filename)s]: %(message)s"
    )

    stream_handler = StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.handlers = [stream_handler]

    logger.setLevel(INFO)

    return logger


app_logger = setting_logger(
    logger=getLogger('app')
)

logging.basicConfig(level=INFO)

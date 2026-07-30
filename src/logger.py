import logging


class Logger:

    def __init__(self):

        logging.basicConfig(

            level=logging.INFO,

            format="[%(levelname)s] %(message)s"

        )

        self.logger = logging.getLogger(

            "poll-system"

        )

    def info(self, message):

        self.logger.info(message)

    def warning(self, message):

        self.logger.warning(message)

    def error(self, message):

        self.logger.error(message)

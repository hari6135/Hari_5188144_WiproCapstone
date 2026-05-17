import logging
import os


class LogGen:

    @staticmethod
    def loggen():

        if not os.path.exists("logs"):
            os.makedirs("logs")

        logging.basicConfig(
            filename="logs/project.log",
            format="%(asctime)s : %(levelname)s : %(message)s",
            level=logging.INFO
        )

        logger = logging.getLogger()

        return logger
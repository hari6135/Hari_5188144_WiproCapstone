import logging
import os


class LogGen:

    @staticmethod
    def loggen():

        log_dir = "logs"

        # ============================================
        # CREATE LOG DIRECTORY
        # ============================================

        if not os.path.exists(
                log_dir
        ):

            os.makedirs(
                log_dir
            )

        logger = logging.getLogger()

        logger.setLevel(
            logging.INFO
        )

        # ============================================
        # CLEAR OLD HANDLERS
        # ============================================

        if logger.hasHandlers():

            logger.handlers.clear()

        # ============================================
        # FILE HANDLER
        # ============================================

        file_handler = logging.FileHandler(

            "logs/automation.log",

            mode="a",

            encoding="utf-8"
        )

        formatter = logging.Formatter(

            "%(asctime)s : "
            "%(levelname)s : "
            "%(message)s"
        )

        file_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            file_handler
        )

        return logger
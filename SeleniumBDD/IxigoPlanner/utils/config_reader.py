import configparser


class ConfigReader:

    config = configparser.ConfigParser()

    config.read(
        "config/config.ini"
    )

    # =====================================================
    # BASE URL
    # =====================================================

    @staticmethod
    def get_base_url():

        return ConfigReader.config.get(
            "DEFAULT",
            "base_url"
        )

    # =====================================================
    # BROWSER
    # =====================================================

    @staticmethod
    def get_browser():

        return ConfigReader.config.get(
            "DEFAULT",
            "browser"
        )

    # =====================================================
    # TIMEOUT
    # =====================================================

    @staticmethod
    def get_timeout():

        return ConfigReader.config.getint(
            "DEFAULT",
            "timeout"
        )

    # =====================================================
    # IMPLICIT WAIT
    # =====================================================

    @staticmethod
    def get_implicit_wait():

        return ConfigReader.config.getint(
            "DEFAULT",
            "implicit_wait"
        )

    # =====================================================
    # HEADLESS
    # =====================================================

    @staticmethod
    def get_headless():

        return ConfigReader.config.getboolean(
            "DEFAULT",
            "headless"
        )
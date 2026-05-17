from configparser import ConfigParser


class ConfigReader:

    parser = ConfigParser()

    parser.read("config/config.properties")

    @staticmethod
    def get(key):
        return ConfigReader.parser.get("DEFAULT", key)
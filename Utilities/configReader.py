from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read(r'..//Configurations/config.ini')
    return config.get(section, key)

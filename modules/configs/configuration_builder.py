from glob import glob
from dotenv import dotenv_values

global_config = None


def build_config():
    return dotenv_values(".env")


def get_config():
    global global_config
    if global_config is None:
        global_config = build_config()
    return global_config


def get_database_config():
    config = get_config()
    return {
        
    }
import json

CONFIG_FILE = 'config.json'

def load_config_file():
    with open(CONFIG_FILE) as file:
        return json.load(file)

def get_cfg_option(option):
    return load_config_file()[option]

def get_cfg_list(list_name):
    return get_cfg_option(list_name)

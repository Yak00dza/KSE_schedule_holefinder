import json

CONFIG_FILE = 'config.json'

def load_config_file():
    with open(CONFIG_FILE) as file:
        return json.loads(file)

def get_cfg_option(option):
    return load_config_file()[option]

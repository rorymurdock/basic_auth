"""Example on reading config"""
from basic_auth import Auth

# Get the config from the file
CONFIG = Auth().read_config("general.json")

if CONFIG:
    # Print the details
    print(CONFIG["url"])
    print(CONFIG["authorization"])
else:
    print('Unable to read config')

"""Simple example of using the Basic package"""
from basic_auth import Auth

# Generate config file
Auth().basic_config("url", "username", "password")

# Read config from file
READ = Auth().read_config("basic_config.json")
print(READ)

[![Build Status](https://github.com/rorymurdock/basic_auth/workflows/Pytest/badge.svg)](https://github.com/rorymurdock/basic_auth/actions)
[![Coverage Status](https://coveralls.io/repos/github/rorymurdock/basic_auth/badge.svg?branch=master)](https://coveralls.io/github/rorymurdock/basic_auth?branch=master)

# Basic

A package for creating and reading config files for basic authentication.

# Purpose
A lot of APIs use basic authentication, this is where you concatenate `username` and `password` separated by a `:` and encode them with base64 then prefix with `Basic`. So `username:password` encoded with base64 becomes `Basic dXNlcm5hbWU6cGFzc3dvcmQ=`. This package manages the encoding and storing of this configuration so it can be easily retrieve and used.

# Usage
Getting started is easy, first install the package using `pip install basic`

Next you can create your auth dict

```python
form basic_auth import Auth
```

```python
CONFIG = Auth().basic_config("url", Auth().encode("username", "password"))
```

Write it to file
```python
Auth().create_config("basic_config.json", CONFIG)
```

To read it in your own scripts
```
CONFIG = Auth().read_config("basic_config.json")
```

Have a read of `simple.py`

There's some examples in the Examples directory
`general.py` supports both interactive input and arguments.

```shell
python3 Examples/general.py -url example.com -username user1 -password hunter2
```

and

```shell
python3 Examples/general.py
```

WSO.py shows how to use it and insert your own custom fields too.

# Details
This will create a folder called config and store the config in a json file with the following structure

```json
{
    "url": "url",
    "authorization": "Basic dXNlcm5hbWU6cGFzc3dvcmQ="
}
```

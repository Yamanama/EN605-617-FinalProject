from types import SimpleNamespace
from typing import Any
import json
import sys

class Config(SimpleNamespace):
    def __init__(self, config_file=None, dictionary=None, **kwargs: Any) -> None:
        """Config File to SimpleNamespace Translator. Allows for dot notaion access

        Args:
            config_file (str, optional): The path to the config file. Defaults to None.
            dictionary (dict, optional): The dictionary. Defaults to None.
        """
        super().__init__(**kwargs)
        # Root call. Parse the file
        if config_file is not None:
            # load the file
            try:
                with open(config_file) as f:
                    dictionary = json.load(f)
            except FileNotFoundError:
                print("Couldn't load {0}".format(config_file))
                sys.exit(-1)
        # iterate the key value pairs 
        for key, value in dictionary.items():
            if isinstance(value, dict):
                # recurse into dicts
                self.__setattr__(key, Config(dictionary=value))
            else:
                # add key/value pair to namespace
                self.__setattr__(key, value)
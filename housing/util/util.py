# This file will basically contain all the helper functions
# Like reading a yaml file is not a part of the main pipeline code , but this is a kind 
# of helper function to read the content of the config.yaml file which contains the configuration information



import yaml
import os,sys
from housing.exception import HousingException


def read_yaml_file(file_path:str)-> dict:
    """Reads a yaml file and return the contents as a dcitionary
    file_path=str
    """
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys)
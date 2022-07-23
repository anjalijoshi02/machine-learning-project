from setuptools import find_packages, setup
from typing import List # all the dadatypes are from typing module only

# Declaring variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Anjali Joshi"
DESCRIPTION="this is a machine learning project"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()-> List[str]:
    """
    This function will return the list of all the modules/libraries mentioned inside
    the requirements.txt file

    return : This function is going to return a list of all the libraries
    mentioned inside the requirements.txt file
    """
    # List[str] basically tells what the function returns (here the function returns
    # a list which contains string)
    # This function will read the requirements.txt file and return all the libraries
    # written in that file
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list=[lib_name.replace("\n","") for lib_name in requirement_file.readlines()]
        print(requirement_list)
        if "-e ." in requirement_list:
            requirement_list.remove("-e .")
        return requirement_list


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)
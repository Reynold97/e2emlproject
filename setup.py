from setuptools import find_packages, setup
from typing import List


MINUS_E_DOT = "-e ."

def get_reqeriments(file_path: str)->list[str]:
    requeriments = [],
    with open(file_path) as file_obj:
        requeriments = file_obj.readlines()
        requeriments = [req.replace("\n","") for req in requeriments]
        if MINUS_E_DOT in requeriments:
            requeriments.remove(MINUS_E_DOT)
    return requeriments



setup(
    name= "e2emlproject#1",
    version= "0.0.1", 
    author= "Reynold Oramas",
    author_email= "reynoldalejandro46@gmail.com",
    packages= find_packages(),
    install_requires= get_reqeriments("requirements.txt"),
)
from setuptools import find_packages, setup
from typing import List
HYPEN_DOT='-e .'

def get_requirements(file_path:str)->List[str]:

    '''
    this function will return list of requirements'''
    reqirements=[]
    with open(file_path) as file_obj:
        reqirements=file_obj.readlines()
        reqirements=[req.replace("\n"," ") for req in reqirements]
        if HYPEN_DOT in reqirements:
            reqirements.remove(HYPEN_DOT)
        return reqirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Amit Mehta",
    author_email="amitmehta8406@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
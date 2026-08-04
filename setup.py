from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_recquirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    recquirments=[]
    with open(file_path, 'r') as file_obj:
        recquirments=file_obj.readlines()
        recquirments=[req.replace("\n","") for req in recquirments]

        if HYPHEN_E_DOT in recquirments:
            recquirments.remove(HYPHEN_E_DOT)
    return recquirments
setup(
    name='ml_project',
    version='0.0.1',
    author='Shivangi Soni',
    author_email='shivangisoni687@gmail.com',
    packages=find_packages(),
    install_requires= get_recquirements('recquirements.txt')

)
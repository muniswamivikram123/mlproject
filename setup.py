from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from the given file path.
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()  # Corrected to readlines()
        requirements = [req.strip() for req in requirements]  # Replaced replace with strip()
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='muniswamivikram123',
    author_email='vikrammuniswami07@gmail.com',  # Corrected key name
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)

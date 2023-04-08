from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    with open('requirements.txt','r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name= 'ML Project',
    version= '0.0.1',
    author='Sumit',
    author_email='sumitshirole777@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
)
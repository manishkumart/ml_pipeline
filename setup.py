from setuptools import find_packages, setup
from typing import List


HYPEN_DOT_E="-e ."
def get_requirements(file_path:str) -> List[str]:
    """
    This function returns the list of requiremets
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)

    return requirements

setup(
    name="mlpipeline",
    version="0.0.1",
    author="Manish Kumar Thota",
    author_email="manish.thota1999@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
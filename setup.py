from setuptools import find_packages, setup

setup(
    name='saf_aws',
    packages=find_packages(include=['saf_aws']),
    version='0.1.0',
    description='AWS resource library for the Social Analytics Framework',
    author='Olivier Dupuis',
    license='MIT',
)
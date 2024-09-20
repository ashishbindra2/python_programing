from setuptools import setup, find_packages

setup(
    name='facker_util',
    version='0.0.1',
    packages=find_packages(),  # __init__.py is mandatory for this
    install_requires=["faker","requests"],
)

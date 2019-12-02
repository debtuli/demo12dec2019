from setuptools import setup, find_packages
from io import StringIO

setup (
    name             = "sample:api",
    version          = "0.1",
    description      = "Example application to be deployed.",
    packages         = find_packages(),
    install_requires = ["gunicorn"],
)

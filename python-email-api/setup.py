from setuptools import setup, find_packages
from io import BytesIO     # for handling byte strings
from io import StringIO    # for handling unicode strings

setup (
    name             = "sample:api",
    version          = "0.1",
    description      = "Example application to be deployed.",
    packages         = find_packages(),
    install_requires = ["gunicorn"],
)

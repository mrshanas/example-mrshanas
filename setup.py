from setuptools import setup, find_packages
from codecs import open

def get_readme():

    readme = ""
    with open('README.md','r','utf-8') as f:
        readme = f.read()
    return readme

VERSION = "0.0.4"
DESCRIPTION = "A package that adds one to a given number"
LONG_DESCRIPTION = get_readme()


setup(
    name="example_mrshanas",
    version=VERSION,
    author="Shanas",
    author_email="nassibshaban345@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=["python","first package"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
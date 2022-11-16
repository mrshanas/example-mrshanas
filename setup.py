from setuptools import setup, find_packages

VERSION = "0.0.3"
DESCRIPTION = "A package that adds one to a given number"
LONG_DESCRIPTION = "README.md"

setup(
    name="example_mrshanas",
    version=VERSION,
    author="Shanas",
    author_email="nassibshaban345@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=["python","first package"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
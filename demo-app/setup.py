#!/usr/bin/python3

import os
import setuptools

this = os.path.dirname(os.path.realpath(__file__))
def read(name):
    with open(os.path.join(this, name)) as f:
        return f.read()

setuptools.setup(
    name="popup",
    version="1.0",
    author="Syed Danish Hussaini",
    author_email="hussainidanish347@yahoo.com",
    description="A small demo project for QT5 apps",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['myapp_source'],
    include_package_data=True,
    install_requires=read('requirements.txt'),
    scripts=['bin/popup']
)

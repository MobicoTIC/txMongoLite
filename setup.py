# -*- coding: utf-8 -*-
"""Test the txMongoLite API"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from setuptools import find_packages, setup
import os.path

with open(os.path.join(
        os.path.dirname(__file__),
        "txmongolite", "_version")) as ver:
    __version__ = ver.readline().strip()

classifiers = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
]

with open('README.rst') as f:
    readme = f.read()

setup(
    name="txmongolite",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "txmongo",
    ],
    package_data={"txmongolite": ["_version"]},
    author="Mobico TIC SAS",
    author_email="desarrollo@mobicotic.com",
    classifiers=classifiers,
    description="A MongoLite inspired txmongo based ODM",
    license="LGPLv3+",
    url="https://github.com/MobicoTIC/txMongoLite",
    long_description=readme
)

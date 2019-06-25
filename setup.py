# -*- coding: utf-8 -*-

"""

    Module :mod:``

    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
from os import path
from setuptools import setup
from ConfigParser import SafeConfigParser
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]


here = path.abspath(path.dirname(__file__))

setup_config_parser = SafeConfigParser()
setup_config_parser.read(path.join(here, 'setup.ini'))

setup(
    name='wheredb',
    version=setup_config_parser.get('build', 'version'),
    description='Project WhereDB',

    url='http://github.com/sivacn/wheredb',

    author='Siva Cn',
    author_email='cnsiva@protonmail.com',

    license='MIT',

    packages=['wheredb'],
    namespaces=[
        'wheredb',
        'wheredb.engine',
        'wheredb.db'
    ],
    zip_safe=False
)

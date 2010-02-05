#!/usr/bin/env python

from setuptools import setup

import rsa

setup(name='rsa',
	version=rsa.__version__,
    description='Pure-Python RSA implementation', 
    author='Sybren A. Stuvel',
    author_email='sybren@stuvel.eu', 
    maintainer='Sybren A. Stuvel',
    maintainer_email='sybren@stuvel.eu',
	url='http://www.stuvel.eu/rsa',
	packages=['rsa'],
    license='GPL + EUPL',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security :: Cryptography',
    ],
)

#!/usr/bin/env python

from setuptools import setup, find_packages

# Top-level setup
setup(
    name             = 'radio-contact-tracker',
    version          = '0.1.0',
    description      = '',
    long_description =  'radio-contact-tracker is a utility for tracking reception logs from WSJT-X log files.',
    url              = 'https://github.com/akey7/radio-contact-tracker',
    author           = 'Alicia M. Key, AA0NS',
    author_email     = 'alicia@aa0ns.com',
    install_requires = [
        'pandas',
        'maidenhead',
    ],
    license          = 'MIT',
)

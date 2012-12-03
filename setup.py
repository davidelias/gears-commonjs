#!/usr/bin/env python
from setuptools import setup

setup(name='gears-commonjs',
    version='0.1',
    packages=[
        'gears_commonjs',
    ],
    package_data={
        'tradeup': ['assets/*.*']
    },
)

#-*- coding:utf-8 -*-
'''
Created on 2018-05-23

@author: ranyixu
'''

from setuptools import setup, find_packages

setup(
    name='whatweb',
    version='0.0.1',
    author='ranyixu',
    author_email='1015243376@qq.com',
    packages=find_packages(),
    include_package_data = True,
    zip_safe = False,
    keywords = ['whatweb', 'webscanner', 'asyncio'],
    description='A python wrap fot whatweb',
    classifiers=[  
        "Intended Audience :: Developers",  
        "Operating System :: OS Independent",  
        "Topic :: System :: Networking",  
        "Topic :: Software Development :: Libraries :: Python Modules",  
        "Programming Language :: Python :: 3.4",  
        "Programming Language :: Python :: 3.5",  
        "Programming Language :: Python :: 3.6",  
    ]
)

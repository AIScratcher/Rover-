# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:53:17 2018

@author: JG
"""


from distutils.core import setup, Extension

module1 = Extension('demo',
                    sources = ['demo.cpp'])

setup (name = 'PackageName',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
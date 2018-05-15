from distutils.core import setup, Extension

module = Extension('sub_level',
                    sources = ['main.c'])

setup(name='sub_level',
      version='1.0',
      description="Fast low level function",
      ext_modules = [module])
      

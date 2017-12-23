from distutils.core import setup
from setuptools import find_packages

setup(name='sempylver',
      version='0.0.1',
      description='A simple tool for tracking the semantic version of projects',
      author='Jeff Cochran',
      author_email='jeffrey.david.cochran@gmail.com',
      packages=find_packages(),
      entry_points={
        'console_scripts': [
            'sempylver = sempylver.__main__:cli'
        ]
      }
)
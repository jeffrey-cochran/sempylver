from distutils.core import setup
from setuptools import find_packages


with open('__version__', 'r') as f:
    version = f.read().strip()


setup(
    name='sempylver',
    version=version,
    description='A simple tool for tracking the semantic version of projects',
    author='Jeff Cochran',
    author_email='jeffrey.david.cochran@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sempylver = sempylver.__main__:main'
        ]
    },
    include_package_data=True,
    install_requires=[
        'pyyaml',
    ],
)

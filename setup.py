#######
# ETL "Extract, Transform, and Load." 
#######

from setuptools import setup

VERSION = "0.0.1dev0"

setup(
    name='PNN-practico',
    version=VERSION,
    description='main etl for pose neural network model',
    author='',
    author_email='',
    classifiers=[
        'Programming Language :: Python :: 3.9.1',
    ],
    packages=['pnn_mvp'],
    # install_requires=['scikit-learn==0.23.0']
)
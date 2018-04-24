
from setuptools import setup

setup(
    name='caas',
    packages=['caas'],
    include_package_data=True,
    install_requires=[
        'flask',
        'correios-python-sdk'
    ]
)


from setuptools import setup

setup(
    name='ccwc',
    version='1.0',
    packages=['ccwc'],
    entry_points={
        'console_scripts': [
            'ccwc = ccwc.cli:main'
        ]
    },
    install_requires=[
        # Add any required dependencies here
    ],
    description='A command-line tool like wc',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

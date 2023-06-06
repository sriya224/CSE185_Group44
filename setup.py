# setup tool to create blobfish package for users to download
from setuptools import setup, find_packages

setup(
    name='your-package-name',
    version='1.0',
    description='The blobfish package creates a txt file with a table of kmer counts from a given fasta sequence.',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'blobfish = blobfish.py:main',
        ],
    },
)

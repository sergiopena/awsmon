import os
import setuptools


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name="awsmon",
    version="0.0.1",
    author="Sergio Pena",
    author_email="isergiopena@gmail.com",
    description=("Monitor AWS cloudformation stacks and notify on macos any status change"),
    license="BSD",
    keywords="aws cloudformation monitor macos notify",
    url="https://www.github.com/sergiopena/awsmon",
    packages=setuptools.find_packages(),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'awsmon = awsmon:main'
        ]
    },
    install_requires=[
        'boto3==1.23.6',
        'pydantic==1.10.0a1'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

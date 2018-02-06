# -*- encoding: utf-8 -*-
# ! python3

import io

from setuptools import setup

setup(
    name='tensorflow-serving-api-python3',
    version='1.4.0',
    description="""*UNOFFICIAL* TensorFlow Serving API libraries for Python3""",
    long_description=io.open("README.rst", 'r', encoding="utf-8").read(),
    url='https://github.com/illagrenan/tensorflow-serving-api-python3',
    license='Apache 2.0',
    keywords="TensorFlow Serving API libraries",
    author='Vize',
    author_email='tensorflow-serving-dev@googlegroups.com',
    packages=['tensorflow_serving'],
    install_requires=[
        'grpcio>=1.7.0',
        'tensorflow>=1.4.0'
    ],
    python_requires='~=3.5',
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent'
    ]
)

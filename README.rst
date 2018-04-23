=========================================================
*UNOFFICIAL* TensorFlow Serving API libraries for Python3
=========================================================

+----------------+-----------------------------------------------------------------------------------------------------------------+
| Latest release | .. image:: https://img.shields.io/pypi/v/tensorflow-serving-api-python3.svg                                     |
|                |    :target: https://pypi.python.org/pypi/tensorflow-serving-api-python3                                         |
|                |    :alt: PyPi                                                                                                   |
|                |                                                                                                                 |
|                | .. image:: https://img.shields.io/pypi/implementation/tensorflow-serving-api-python3.svg                        |
|                |    :target: https://pypi.python.org/pypi/tensorflow-serving-api-python3/                                        |
|                |    :alt: Supported Python implementations                                                                       |
|                |                                                                                                                 |
|                | .. image:: https://img.shields.io/pypi/pyversions/tensorflow-serving-api-python3.svg                            |
|                |    :target: https://pypi.python.org/pypi/tensorflow-serving-api-python3/                                        |
|                |    :alt: Supported Python versions                                                                              |
+----------------+-----------------------------------------------------------------------------------------------------------------+
| CI             | .. image:: https://img.shields.io/travis/illagrenan/tensorflow-serving-api-python3.svg                          |
|                |    :target: https://travis-ci.org/illagrenan/tensorflow-serving-api-python3                                     |
|                |    :alt: TravisCI                                                                                               |
+----------------+-----------------------------------------------------------------------------------------------------------------+

Installation
------------

Supported Python versions are: ``3.5`` and ``3.6``.

.. code:: shell

    pip install --upgrade tensorflow-serving-api-python3


Supported versions of Tensorflow
--------------------------------

+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------+
| Tensorflow version    | Serving API version                                    | Link to original serving package                                                       |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``tensorflow~=1.4.0`` | ``pip install 'tensorflow-seving-api-python3~=1.4.0'`` | `https://pypi.org/.../1.4.0 <https://pypi.org/project/tensorflow-serving-api/1.4.0/>`_ |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``tensorflow~=1.5.0`` | TBA                                                    | `https://pypi.org/.../1.5.0 <https://pypi.org/project/tensorflow-serving-api/1.5.0/>`_ |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``tensorflow~=1.6.0`` | ``pip install 'tensorflow-seving-api-python3~=1.6.0'`` | `https://pypi.org/.../1.6.0 <https://pypi.org/project/tensorflow-serving-api/1.6.0/>`_ |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``tensorflow~=1.7.0`` | TBA                                                    | `https://pypi.org/.../1.7.0 <https://pypi.org/project/tensorflow-serving-api/1.7.0/>`_ |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------+


Why?
----

Official Serving package (https://pypi.python.org/pypi/tensorflow-serving-api) is marked as Python2-only although it **supports** Python3 (therefore you cannot ``pip3 install tensorflow-serving-api``). This has been discussed in this thread: https://github.com/tensorflow/serving/issues/700 (unfortunately, the proposal for publishing the Python3 package was rejected).

This package **is only redistribution**: I only downloaded Python2 ``.whl`` from the PyPI, extracted it and added my ``setup.py`` with Python3 support.

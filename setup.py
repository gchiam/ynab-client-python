# coding: utf-8

"""
    YNAB API v1 Python Client

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = 'ynab_client'
VERSION = '0.1.1'

REQUIRES = [
    'urllib3 >= 1.15',
    'six >= 1.10',
    'certifi',
    'python-dateutil'
]

setup(
    name=NAME,
    version=VERSION,
    description='YNAB API v1 Python Client',
    author_email='gordon.chiam@gmail.com',
    url='https://github.com/gchiam/ynab-client-python',
    license='Apache2',
    classifiers=(
	'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ),
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Unofficial Python Library for YNAB API v1 - https://api.youneedabudget.com/v1
    """
)

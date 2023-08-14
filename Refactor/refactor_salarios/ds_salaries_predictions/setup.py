#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Luis Fernandez Perez",
    author_email='A01688848@tec.mx',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Data Science Salarys Predictions",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ds_salaries_predictions',
    name='ds_salaries_predictions',
    packages=find_packages(include=['ds_salaries_predictions', 'ds_salaries_predictions.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/luisfp2000/ds_salaries_predictions',
    version='0.1.0',
    zip_safe=False,
)

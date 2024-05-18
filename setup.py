
from setuptools import setup, find_packages

setup(
    name='HFilter',
    version='0.1.0',
    description='A package for filtering time series, "Why You Should Never Use the Hodrick-Prescott Filter"',
    author='S. Yanki Kalfa',
    author_email='skalfa@ucsd.edu',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.18.0',
        'statsmodels>=0.11.0'
    ],
    test_suite='tests',
    tests_require=[
        'pytest>=5.0.0'
    ],
)

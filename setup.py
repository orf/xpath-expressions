from setuptools import setup
import sys

if sys.version_info < (3, 5):
    raise RuntimeError('xcat requires Python 3.5 and above!')

setup(
    name='xpath-expressions',
    version='0.2',
    packages=['xpath'],
    url='https://github.com/orf/xpath-expressions',
    license='MIT',
    author='orf',
    author_email='tom@tomforb.es',
    description='Manipulate xpath expressions in pure python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ]
)

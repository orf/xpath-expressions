from setuptools import setup
import sys
import pathlib

if sys.version_info < (3, 5):
    raise RuntimeError('xcat requires Python 3.5 and above!')

from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        import shlex
        import pytest
        errno = pytest.main(shlex.split(' '.join(self.pytest_args)))
        sys.exit(errno)


readme = ""
readme_path = pathlib.Path("README.rst")
if readme_path.exists():
    readme = readme_path.read_text()

setup(
    name='xpath-expressions',
    version='0.2',
    packages=['xpath', 'xpath.functions'],
    url='https://github.com/orf/xpath-expressions',
    license='MIT',
    author='orf',
    readme=readme,
    author_email='tom@tomforb.es',
    description='Manipulate xpath expressions in pure python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    tests_require=['pytest', 'lxml'],
    cmdclass={'test': PyTest},
)

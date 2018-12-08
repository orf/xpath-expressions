from setuptools import setup
import pathlib

readme = ""
readme_path = pathlib.Path("README.md")
if readme_path.exists():
    readme = readme_path.read_text()

setup(
    name='xpath-expressions',
    version='1.0.1',
    packages=['xpath'],
    url='https://github.com/orf/xpath-expressions',
    license='MIT',
    author='orf',
    long_description=readme,
    long_description_content_type='text/markdown',
    author_email='tom@tomforb.es',
    python_requires='>=3.5',
    description='Treat XPath expressions as Python objects ',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ]
)

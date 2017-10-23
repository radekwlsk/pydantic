from importlib.machinery import SourceFileLoader
from pathlib import Path
from setuptools import setup

THIS_DIR = Path(__file__).resolve().parent
long_description = (
    THIS_DIR.joinpath('README.rst').read_text() +
    '\n\n' +
    THIS_DIR.joinpath('HISTORY.rst').read_text()
)

# avoid loading the package before requirements are installed:
version = SourceFileLoader('version', 'pydantic/version.py').load_module()

setup(
    name='pydantic',
    version=str(version.VERSION),
    description='Data validation and settings management using python 3.6 type hinting',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Environment :: MacOS X',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
    ],
    author='Samuel Colvin',
    author_email='s@muelcolvin.com',
    url='https://github.com/samuelcolvin/pydantic',
    license='MIT',
    packages=['pydantic'],
    python_requires='>=3.6',
    zip_safe=True,
    extras_require={
        'msgpack': ['msgpack-python>=0.4.8'],
        'ujson': ['ujson>=1.35'],
    }
)

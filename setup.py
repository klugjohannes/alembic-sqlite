import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "alembic-sqlite",
    version = "0.0.1a0",
    author = "Johannes Klug",
    author_email = "mail@room2web.de",
    description = ("a collection of alembic workaround and hacks for improved sqlite support."),
    license = "BSD",
    keywords = "sqlalchemy alembic sqlite",
    packages=['alembic_sqlite', 'tests'],
    long_description=read('README'),
    install_requires=['sqlalchemy', 'alembic'],
)

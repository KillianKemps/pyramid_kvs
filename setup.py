import os
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
name = 'pyramid_kvs'

with open(os.path.join(here, 'README.rst')) as readme:
    README = readme.read()
with open(os.path.join(here, 'CHANGES.rst')) as changes:
    CHANGES = changes.read()

with open(os.path.join(here, name, '__init__.py')) as v_file:
    version = re.compile(r".*__version__ = '(.*?)'",
                         re.S).match(v_file.read()).group(1)


requires = ['pyramid >1.3, <1.5.99',
            'python-memcached',
            'redis']

setup(name=name.replace('_', '-'),
      version=version,
      description='Session and cache for Pyramid',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        ],
      author='Gandi',
      author_email='feedback@gandi.net',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      )


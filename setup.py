import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

setup(name='multi_key_sort',
      version='0.0.1',
      description='multi_key_sort',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python 2.7.x; Python 3.4.x",
        "Topic :: Python :: Sort",
        "Topic :: Python :: Interface",
        ],
      author='HAP Proctor',
      author_email='48.41.50@gmail.com',
      url='https://github.com/48-41-50/inv-control',
      keywords='sort multi-key multi-directional',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      )

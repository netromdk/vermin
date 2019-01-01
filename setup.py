# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
  long_description = f.read()

setup(
  name="vermin",
  version="0.4.10",

  description="Concurrently detect the minimum Python versions needed to run code",
  long_description=long_description,

  url="https://github.com/netromdk/vermin",

  author="Morten Kristensen",
  author_email="msk@nullpointer.dk",

  license="MIT",

  classifiers=[
    "Development Status :: 4 - Beta",

    "Intended Audience :: Developers",

    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",

    "License :: OSI Approved :: MIT License",

    "Topic :: Utilities",
    "Topic :: Software Development",
  ],

  keywords="version detection analysis ast development",

  packages=find_packages(exclude=["tests"]),

  python_requires=">=2.7",

  entry_points={
    "console_scripts": [
      "vermin=vermin:main",
    ],
  },

  project_urls={
    "Bug Reports": "https://github.com/netromdk/vermin/issues",
    "Source": "https://github.com/netromdk/vermin/",
  },
)

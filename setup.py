from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
  name='slowly',
  version='1.0.0',
  packages=find_packages(),
  install_requires=requirements,
  entry_points={
    "console_scripts": [
      "slowly:src.__main__:main"
    ]
  }
)

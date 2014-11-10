try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup
  
config = {
  'description': 'My Project',
  'author': 'john scancella',
  'url': 'https://github.com/johnscancella/learnPythonTheHardWay',
  'download_url': 'https://github.com/johnscancella/learnPythonTheHardWay',
  'author_email': 'jsca@loc.gov',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['NAME'],
  'scripts': [],
  'name': 'projectname'
}

setup(**config)

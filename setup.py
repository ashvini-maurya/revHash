try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Reverse Hash',
    'author': 'Ashvini Kumar',
    'author_email': 'ashvinikumar45@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'name': 'revHash'
}

setup(**config)

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    extras = {}
else:
    extras = {
        'test_suite': 'wsrplib.tests',
        'zip_safe': False,
        'entry_points': 
          "[console_scripts]\n"
          "wsrp_server = wsrplib.serve:main\n"
          "wsrp_client = wsrplib.client:main\n"
    }

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()


setup(name='wsrplib',
      version='0.1',
      description='WSRP protocol',
      long_description='\n\n'.join([README, CHANGES]),
      install_requires=[
        'soaplib',
        'zope.component',
        'Paste',
      ],
      packages=['wsrplib'],
      **extras
     )

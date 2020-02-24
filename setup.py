import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='acpy',
      version='1.0.1',
      description='ActiveCampaign API written in python',
      long_description=read('README.md'),
      author='Miguel Ferrer, 2key.network',
      author_email='hello@2key.network',
      url='https://github.com/2key/activecampaign-python',
      packages=['activecampaign'],
      install_requires=[
          'requests',
      ],
      keywords='activecampaign',
      zip_safe=False,
      license='MIT',
      )

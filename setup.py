from setuptools import setup
import os
here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except:
    README = ""


setup(name='paytm',
      version='0.1.7',
      description='paytm payment gateway',
      long_description=README,
      url='http://github.com/harishbisht/paytm',
      author='Harish Bisht',
      author_email='harish@pickrr.com',
      license='MIT',
      packages=['paytm'],
      install_requires=[
          'requests','pycrypto'
      ],
      zip_safe=False)
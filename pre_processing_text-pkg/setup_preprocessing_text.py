"""
Release my first package to my self.
It will preprocess my data.

Tutorial:
https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html
https://www.tutorialsteacher.com/python/python-package
https://packaging.python.org/

To install in dev mode, run in the terminal:

$ python setup.py develop

Make sure the setup.py file is not inside the directory
you want to packaged.

"""

from setuptools import setup

name='pre_processing_text'
version='0.1'
description='Apply NLP processing functions in order to clean text using regex, normalize English text through lemmatization and remove stopwords'
url='#'
author='lclarete'
author_email='livia.clarete@gmail.com'
# license='MIT'
packages=['pre_processing_text']
zip_safe=False

setup(name=name,
version=version,
description=description,
url=url,
author=author,
author_email=author_email,
# license=license,
packages=packages,
zip_safe=False)

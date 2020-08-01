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

name='data_pipeline'
version='0.1'
description='Package divided into five peices: get-data; eda; preprocessing-text; modeling; plot-viz.'
url='#'
author='lclarete'
author_email='livia.clarete@gmail.com'
# license='MIT'
packages=['data_pipeline']

setup(name=name,
version=version,
description=description,
url=url,
author=author,
author_email=author_email,
# license=license,
# zip_safe=False,
packages=packages
)

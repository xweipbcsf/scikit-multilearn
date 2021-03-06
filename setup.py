# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
# import sphinx_pypi_upload
import codecs

with codecs.open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='scikit-multilearn',
    version='0.1.0rc1',
    packages=find_packages(exclude=['docs', 'tests', '*.tests']),
    author=u'Piotr Szymański',
    author_email=u'niedakh@gmail.com',
    license=u'BSD',
    long_description=readme,
    url=u'http://scikit-multilearn.github.io/',
    description=u'A set of python modules for multi-label classification',
    classifiers=[
        u'Development Status :: 5 - Production/Stable',
        u'Environment :: Console',
        u'Environment :: Web Environment',
        u'Intended Audience :: Developers',
        u'Intended Audience :: Education',
        u'Intended Audience :: Science/Research',
        u'License :: OSI Approved :: BSD License',
        u'Operating System :: MacOS :: MacOS X',
        u'Operating System :: Microsoft :: Windows',
        u'Operating System :: POSIX',
        u'Programming Language :: Python',
        u'Topic :: Scientific/Engineering',
        u'Topic :: Scientific/Engineering :: Information Analysis',
        u'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)

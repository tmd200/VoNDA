#!/usr/bin/env python
from __future__ import division, print_function, absolute_import
"""
VoNDA Setup
===========

Written by TR Maarleveld, Amsterdam, The Netherlands
E-mail: t.r.maarleveld@cwi.nl
Last Change: Augustus 28, 2014
"""

__doc__ = "VoNDA (Visualization of Network DAta) allows for interactive visualization of heterogeneous data"
__version__ = '0.6'

import os

try:
    from numpy.distutils.core import setup
except Exception as ex:
    print(ex)
    os.sys.exit(-1)

local_path = os.path.dirname(os.path.abspath(os.sys.argv[0]))		# Get the dir of setup.py
os.chdir(local_path)

mydata_files = [] 
mymodules = []
mydata_files.append((os.path.join('vonda','colormaps'), [os.path.join(local_path,'vonda','colormaps','rainbow.svg'),os.path.join(local_path,'vonda','colormaps','redgreen.svg'),os.path.join(local_path,'vonda','colormaps','yellowblue.svg'),os.path.join(local_path,'vonda','colormaps','yellowcyan.svg'),os.path.join(local_path,'vonda','colormaps','cyanyellow_white.svg')]))
   

mypackages = ['vonda', 'vonda.modules','vonda.networks','vonda.colormaps','vonda.data_examples','vonda.models']	# My subpackage list

setup(name="VoNDA",
    version = __version__,
    description = __doc__,
    long_description = """
    Welcome to the installation procedure of VoNDA
    
    VoNDA (Visualization of Network DAta) allows for interactive visualization of heterogeneous data
    """,
    author = "T.R. Maarleveld",
    author_email = "tmd200@users.sourceforge.net",
    maintainer = "T.R. Maarleveld",
    maintainer_email = "tmd200@users.sourceforge.net",
    url = "http://vonda.sourceforge.net",
    download_url = "http://vonda.sourceforge.net/files",
    license = " BSD License ",
    keywords = " Bioinformatics, Computational Systems Biology, Bioinformatics, Modeling, Visualization", 
    zip_safe = False,
    requires = ['NumPy'],
    platforms = ["Windows", "Linux", "Mac OS-X"],
    classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: OS Independent',    
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Topic :: Scientific/Engineering :: Visualization'],
    packages = mypackages,
    data_files = mydata_files
    )

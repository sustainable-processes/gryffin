#!/usr/bin/env python 

# import versioneer
# import numpy as np

from setuptools import setup, find_packages
from distutils.extension import Extension
from distutils.command.build import build as build_orig
import pathlib

#===============================================================================

def readme():
	with open('README.md', 'r') as content:
		return content.read()

#===============================================================================

ext_modules = [
	Extension('gryffin.bayesian_network.kernel_evaluations',
		['src/gryffin/bayesian_network/kernel_evaluations.c']),
	Extension('gryffin.bayesian_network.kernel_prob_reshaping',
		['src/gryffin/bayesian_network/kernel_prob_reshaping.c']),]

# Preinstall numpy
from setuptools import dist
dist.Distribution().fetch_build_eggs(['numpy<1.19.0,>=1.16.0'])
import numpy as np

def requirements():
	with open('requirements.txt', 'r') as content:
		return content.readlines()

cwd = pathlib.Path(__file__).parent.absolute()
#===============================================================================

setup(name='gryffin',
	#version=versioneer.get_version(),
	version='0.1.0',
    # cmdclass=versioneer.get_cmdclass(),
	description='Bayesian optimization for categorical variables', 
	long_description=readme(),
	long_description_content_type='text/markdown',
	classifiers=[
		'Intended Audience :: Science/Research',
		'Operating System :: Unix', 
		'Programming Language :: Python',
		'Topic :: Scientific/Engineering', 
	],
	url='https://github.com/aspuru-guzik-group/gryffin',
	author='Florian Hase',
	packages = ['gryffin'],
	package_dir  = {"": "src"},
	zip_safe=False,
	ext_modules=ext_modules,
	tests_require=['pytest'],
	include_dirs=np.get_include(),
	install_requires=requirements(),
	python_requires='>=3.6',
)

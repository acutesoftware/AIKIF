#from distutils.core import setup
from setuptools import setup

setup(
    name='AIKIF',
    version='0.1.2',
    author='Duncan Murray',
    author_email='djmurray@acutesoftware.com.au',
    packages=['aikif', 'aikif.agents','aikif.agents.aggregate','aikif.agents.explore','aikif.agents.gather','aikif.agents.learn','aikif.dataTools','aikif.environments','aikif.examples','aikif.lib', 'aikif.ontology','aikif.toolbox', 'aikif.web_app'],
    url='https://github.com/acutesoftware/AIKIF',
    license='GNU General Public License v3 (GPLv3)',
    description='Artificial Intelligence Knowledge Information Framework',
    long_description=open('README.txt').read(),
    install_requires=[
          'nose >= 1.0',
          'pyaixi >= 1.0'
    ],
    classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Programming Language :: Python :: 3.4',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Software Development :: Documentation',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],

)



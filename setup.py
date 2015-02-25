from distutils.core import setup

setup(
    name='AIKIF',
    version='0.0.5',
    author='Duncan Murray',
    author_email='djmurray@acutesoftware.com.au',
    packages=['aikif', 'aikif.agents','aikif.agents.aggregate','aikif.agents.explore','aikif.agents.gather','aikif.agents.learn','aikif.dataTools','aikif.environments','aikif.examples','aikif.lib', 'aikif.ontology','aikif.toolbox', 'aikif.web_app'],
    url='https://github.com/acutesoftware/AIKIF',
    license='LICENSE.txt',
    description='Artificial Intelligence Knowledge Information Framework',
    long_description=open('README').read(),
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
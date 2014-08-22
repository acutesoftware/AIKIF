from distutils.core import setup

setup(
    name='AIKIF',
    version='0.0.3',
    author='Duncan Murray',
    author_email='djmurray@acutesoftware.com.au',
    packages=['aikif', 'aikif.agents','aikif.dataTools','aikif.environments','aikif.lib', 'aikif.ontology','aikif.toolbox', 'aikif.web_app'],
    url='https://github.com/acutesoftware/AIKIF',
    license='LICENSE.txt',
    description='Artificial Intelligence Knowledge Information Framework',
    long_description=open('README.txt').read(),
    classifiers = [
    'Programming Language :: Python',
    'Development Status :: 2 - Pre-Alpha',
    'Natural Language :: English',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],

)
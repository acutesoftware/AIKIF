from distutils.core import setup

setup(
    name='AIKIF',
    version='0.0.2',
    author='Duncan Murray',
    author_email='djmurray@acutesoftware.com.au',
    packages=['AI', 'tests', 'AI.agents','AI.dataTools','AI.environments','AI.lib','AI.ontology','AI.toolbox'],
    url='https://github.com/acutesoftware/AIKIF',
    license='LICENSE.txt',
    description='Artificial Intelligence Knowledge Information Framework',
    long_description=open('README.txt').read(),
)
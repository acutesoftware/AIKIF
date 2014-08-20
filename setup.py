from distutils.core import setup

setup(
    name='AIKIF',
    version='0.0.1',
    author='Duncan Murray',
    author_email='djmurray@acutesoftware.com.au',
    packages=['AI', 'tests', 'AI.agents','AI.dataTools','AI.environments','AI.lib','AI.ontology','AI.toolbox'],
    url='http://pypi.python.org/pypi/aikif/',
    license='LICENSE.txt',
    description='Artificial Intelligence Knowledge Information Framework',
    long_description=open('README.txt').read(),
)
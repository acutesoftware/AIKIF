AIKIF - Artificial Intelligence Knowledge Information Framework
*NOTE - this is very much an experimental work in progress* 
- the code runs, but wont do anything useful at this stage

Overview
This is an example framework to capture the flow of information initially for personal data management, but ultimately useful for AI applications.
Initially it will be populated and tested for human use, but includes tests and verification process for future ‘General AI’s.
Functions (Octave, Python, SQL) are called at set stages of the AI process which log the results into a standard database schema.


Quick Start
The goal is to get any set of information and parse it into a consistent format so a machine can read it.
For example:
	Project Management
    Code Management
    Personal Information Management

Programs
========
Main Programs
AI.py			- sample main program to show a trivial example of logging data
view.py			- simple command driven procedure to show various details of the system
index.py		- creates text indexes of all the files
search.py		- searches, using both indexes and ontologies
go_web_aikif.bat- starts the web server for the AIKIF admin interface

Toolbox
Various modules which contain generic functions

DataTools
collection of modules to manage data transformations

Standard Library Programs
AIKIF_utils.py	- standard utils for the filelists
fileMapping.py	- main routine that decides what the output files will be called
security.py		- manages security, which will allow users to have private data (not the norm for this)

Data Load programs
These programs are used to load a specific dataset, the code used to parse each file is in a separate load procedure
processRawData.py			- this calls all data load programs and logs results
create_word_lists.py		- loads a list of nouns, verbs, adjectives from web into local structures
loadCountry_Gdeltproject.py	- loads a country reference file
loadPIM_Filelist.py			- loads a list of local files into objects, events, photos
loadPIM_shopping.py			- sample to show how a personal shopping list is loaded






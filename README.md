#AIKIF
#####Artificial Intelligence Knowledge Information Framework

##Overview
This is an example framework to capture the flow of information initially for personal data management, but ultimately useful for AI applications.<br />

The intent is to allow any type of raw data to be machine understandable using data collectors, ontologies, business mapping rules and embedded tags in programs.

###Progress
Area | status
 --- | --- |
| Code base version            | Pre-Alpha    |
| Public package version | 0.0.4        |
| Date notes updated     | 25/02/2015   |


###Quick Start
This github repository [https://github.com/acutesoftware/AIKIF](https://github.com/acutesoftware/AIKIF) contains the latest code, but the current public release is available via

`pip install aikif`

There are some basic examples shown in the aikif/examples folder:<br />
	Project Management<br/>
    Code Management<br/>
    Personal Information Management<br/>

To start the web interface use `aikif/web_app/web_aikif.py` or the batch file `aikif\go_web_aikif`
 
![screenshot of web interface](https://github.com/acutesoftware/AIKIF/blob/master/doc/web-if-v01.jpg "Screenshot of web interface") 
 


##Data Structures
Data type | description |
 --- | ---                
| events     | any time or date based subset of information gets logged here  |
| facts      | the text of the information |
| contacts   | person details extracted and linked from text or column in table |
| locations  | physical location in world, or virtual location on network / computer disk |
 
 
##Programs
###Main Programs
|Filename | description |
 --- | ---      
|go_web_aikif.bat | starts the web server for the AIKIF admin interface|
|index.py		| creates text indexes of all the files|
|search.py		| searches, using both indexes and ontologies|
|mapper.py       | applies business rules to map raw input to aikif data structures|
|context.py      | determines user context|
|bias.py         | user defined ranking of raw data by source / type / person / date|

###Toolbox
Various modules which contain generic functions

This section is where developers add their own programs to be logged and mapped.


###DataTools
collection of modules to manage data transformations

###Standard Library Programs
AIKIF_utils.py	- standard utils for the filelists<br />
file_mapping.py	- main routine that decides what the output files will be called<br />
security.py		- manages security, which will allow users to have private data (not the norm for this)<br />



###Agents
Most processes are run via the `agent.py` class to allow for the logging and management.

These programs are used to load a specific dataset, the code used to parse each file is in a separate load procedure<br />
processRawData.py			- this calls all data load programs and logs results<br />
create_word_lists.py		- loads a list of nouns, verbs, adjectives from web into local structures<br />
loadCountry_Gdeltproject.py	- loads a country reference file<br />
loadPIM_Filelist.py			- loads a list of local files into objects, events, photos<br />
loadPIM_shopping.py			- sample to show how a personal shopping list is loaded<br />






#AIKIF
#####Artificial Intelligence Knowledge Information Framework
*NOTE - this is very much an experimental work in progress* - the code runs, but wont do anything useful at this stage

##Overview
This is an example framework to capture the flow of information initially for personal data management, but ultimately useful for AI applications.<br />
Initially it will be populated and tested for human use, but includes tests and verification process for future ‘General AI’s.<br />
Functions (Octave, Python, SQL) are called at set stages of the AI process which log the results into a standard database schema.<br /><br />

This allows you to easily search and compare previous batch runs.<br />

###Quick Start
The goal is to get any set of information and parse it into a consistant format so a machine can read it.<br />
For example:<br />
	TODO<br />

##Programs
###Main Programs
AI.py			- sample main program to show a trivial example of logging data<br />
view.py			- simple command driven procedure to show various details of the system<br />
index.py		- creates text indexes of all the files<br />
search.py		- searches, using both indexes and onotologies<br />



###Standard Library Programs
AIKIF_utils.py	- standard utils for the filelists<br />
fileMapping.py	- main routine that decides what the output files will be called<br />
security.py		- manages security, which will allow users to have private data (not the norm for this)<br />

###Data Load programs
These programs are used to load a specific dataset, the code used to parse each file is in a separate load procedure<br />
processRawData.py			- this calls all data load programs and logs results<br />
create_word_lists.py		- loads a list of nouns, verbs, adjectives from web into local structures<br />
loadCountry_Gdeltproject.py	- loads a country reference file<br />
loadPIM_Filelist.py			- loads a list of local files into objects, events, photos<br />
loadPIM_shopping.py			- sample to show how a personal shopping list is loaded<br />

###Experimental programs - probably wont be used
addRawData.py	- using word lists, this experiments with parsing information as a bag of words<br />
AIKIF_create.py	- creates default set of filelists and data files (DONT run this if you start using the software)<br />


##Data                  
Raw Data        - raw information from any source<br />
BIAS tables     - weightings to rank data based on various criteria (source, person, format)<br />
Weighted Data   - data ranked according to weightings / human verification results<br />
Algorithms      - database of algorithms, split into componants <br />
Concepts        - generic concepts about information<br />
Concepts_Data   - links to concepts and data<br />
New_Concepts    - randomly generated possible concept links based on ratings<br />

##Tracking generic AI concepts / Logging
###Goal Management
goal_types      - 0=supergoal:{'Be Friendly to humans'}, 1=endgoals ['assist', 'solve', 'learn'], 2=goals [], 3=subgoals []<br />
goals           - list of goals to achieve<br />
preferences     - ranked order of topics to focus on<br />

###Decision Making
commands        - requested commands from human operator<br />
action          - list of actions (AI plans) <br />
outcomes        - list of possible outcomes with impacts, liklihood, past stats, ratings<br />

###Source Data
-----------
rawData         - raw text feed of data from datasets, web, social media<br />
websites        - reference file on websites with biases<br />
people          - reference file on people / usernames with biases<br />

###Data Processing Tables
----------------------
bias            - details on bias's for a given source of rawData<br />
feedback        - human reasoning behind various BIAS weightings and human votes (+/-) on rawData<br />
facts          - result of processed rawData taking into account sources, biases and feedback<br />
knowledge      - understanding of facts *(no idea how this will be implemented)<br />





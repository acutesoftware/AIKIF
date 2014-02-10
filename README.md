#AIKIF
#####Artificial Intelligence Knowledge Information Framework
*NOTE - this is very much an experimental work in progress* - the code runs, but wont do anything useful at this stage

##Overview
This is an example framework to capture the flow of information in AI applications.
Initially it will be populated and tested for human use, but includes tests and verification process for future ‘General AI’s
Functions (Octave, Python, SQL) are called at set stages of the AI process which log the results into a standard database schema.

This allows you to easily search and compare previous batch runs

##Processes
GetCommand      - get input from human operator on what goal/task to work on
ChooseGoal      - initially tied directly to GetCommand, otherwise choose a Goal based on preferences
CreatePlan      - make a plan based on the current goal
GetPlanFeedback - publish the plan to humans for review and safety checks
CollectData     - function to collect raw data from the web and local disks
ProcessData     - function to process raw data using Bias tables to get a comprehension of the information
Play            - random learning, pick random problem to solve, test existing knowledge, practice something

##Data                  
Raw Data        - raw information from any source
BIAS tables     - weightings to rank data based on various criteria (source, person, format)
Weighted Data   - data ranked according to weightings / human verification results
Algorithms      - database of algorithms, split into componants 
Concepts        - generic concepts about information
Concepts_Data   - links to concepts and data
New_Concepts    - randomly generated possible concept links based on ratings

##Tracking generic AI concepts / Logging
###Goal Management
goal_types      - 0=supergoal:{'Be Friendly to humans'}, 1=endgoals ['assist', 'solve', 'learn'], 2=goals [], 3=subgoals []
goals           - list of goals to achieve
preferences     - ranked order of topics to focus on

###Decision Making
commands        - requested commands from human operator
action          - list of actions (AI plans) 
outcomes        - list of possible outcomes with impacts, liklihood, past stats, ratings

###Source Data
-----------
rawData         - raw text feed of data from datasets, web, social media
websites        - reference file on websites with biases
people          - reference file on people / usernames with biases

###Data Processing Tables
----------------------
bias            - details on bias's for a given source of rawData
feedback        - human reasoning behind various BIAS weightings and human votes (+/-) on rawData
facts          - result of processed rawData taking into account sources, biases and feedback
knowledge      - understanding of facts *(no idea how this will be implemented)





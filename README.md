#AIKIF
#####Artificial Intelligence Knowledge Information Framework
*NOTE - this is very much an experimental work in progress* - the code runs, but wont do anything useful at this stage

##Overview
This is an example framework to capture the flow of information in AI applications.<br />
Initially it will be populated and tested for human use, but includes tests and verification process for future ‘General AI’s.<br />
Functions (Octave, Python, SQL) are called at set stages of the AI process which log the results into a standard database schema.<br /><br />

This allows you to easily search and compare previous batch runs.<br />

##Processes
GetCommand      - get input from human operator on what goal/task to work on<br />
ChooseGoal      - initially tied directly to GetCommand, otherwise choose a Goal based on preferences<br />
CreatePlan      - make a plan based on the current goal<br />
GetPlanFeedback - publish the plan to humans for review and safety checks<br />
CollectData     - function to collect raw data from the web and local disks<br />
ProcessData     - function to process raw data using Bias tables to get a comprehension of the information<br />
Play            - random learning, pick random problem to solve, test existing knowledge, practice something<br />

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





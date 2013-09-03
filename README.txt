AIKIF = Artificial Intelligence Knowledge Information Framework
[Planning stage] 22/8/2013
This is an example framework of tables to capture the flow of 
information ready for an AI to utilise it.
Initially it will be populated and tested for a human 


===========================================================================================
    Processes
===========================================================================================
GetCommand      - get input from human operator on what goal/task to work on
ChooseGoal      - initially tied directly to GetCommand, otherwise choose a Goal based on preferences
CreatePlan      - make a plan based on the current goal
GetPlanFeedback - publish the plan to humans for review and safety checks
CollectData     - function to collect raw data from the web and hard drive[ currently using documents on disk instead of web ]
ProcessData     - function to process raw data using Bias tables to get a comprehension of the information
Play            - random learning, pick random problem to solve, test existing knowledge, practice something


===========================================================================================
    Data                  
===========================================================================================

Goal Management
---------------
goal_types      - 0=supergoal:{'Be Friendly to humans'}, 1=endgoals ['assist', 'solve', 'learn'], 2=goals [], 3=subgoals []
goals           - list of goals to achieve
preferences     - ranked order of topics to focus on

Decision Making
---------------
commands        - requested commands from human operator
action          - list of actions (AI plans) 
outcomes        - list of possible outcomes with impacts, liklihood, past stats, ratings

Source Data
-----------
rawData         - raw text feed of data from datasets, web, social media
websites        - reference file on websites with biases
people          - reference file on people / usernames with biases

Data Processing Tables
----------------------
bias            - details on bias's for a given source of rawData
feedback        - human reasoning behind various BIAS weightings and human votes (+/-) on rawData
facts          - result of processed rawData taking into account sources, biases and feedback
knowledge      - understanding of facts *(no idea how this will be implemented)





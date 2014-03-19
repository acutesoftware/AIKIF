# AIKIF_create.py   written by Duncan Murray 26/7/2013  (C) Acute Software
# AIKIF = Artificial Intelligence Knowledge Information Framework
# This script builds a prototype framework of tables to capture the flow 
# of information ready for an AI to utilise it.
# Initially it will be populated and tested for a human (me) 

# Sample data file
# rawData.csv - manual example of raw data for AIKIF_create.py
# date,source,person,raw_string 
# 23/7/2013,manual entry,duncan,python is a good language for programming 
# 23/7/2013,manual entry,duncan,there is no way for a machine to have consciousness 

import os
import sys
import csv
sys.path.append('..//..//_AS_LIB')
import as_util_data as dat
import AIKIF_utils as aikif
localPath = '..//data//' # os.getcwd()

def wipeSampleFiles():
    # wipes all files in the filelist passed (be careful)
    try:
        with open('..//data//AIKIF_FileList.csv', 'r') as f:
            filelist = f.readlines()
            for f in filelist: 
                f = localPath + f
                #print("deleting - ", f)
                try:
                    os.remove( f.rstrip())   # this is required to remove trailing \n
                except: 
                    pass
    except:
        print('creating sample filelist ...')
                
def createSampleFile(fname, header):
    #print("Creating sample file - ", fname)
    wr = csv.writer(open('..//data//' + fname, 'wt'), quoting=csv.QUOTE_ALL, lineterminator='\n')
    wr.writerow(header)
     
def addSampleData(fname, content):
    wr = csv.writer(open('..//data//' + fname, 'at'), quoting=csv.QUOTE_ALL, lineterminator='\n')
    wr.writerow(content)
     

wipeSampleFiles()   # keep this in here until program starts collecting data
#sys.exit("DEBUG - program halted")
  
#-----------------------------------------------------
# define the structures  the data for the source files
#-----------------------------------------------------
AIKIF_FileList = aikif.build_AIKIF_structure()

createSampleFile("refObject.csv", ["objectTypeName","PhysicalType", "description"])
addSampleData("refObject.csv", ["Thought", "Mental", "Thought or mental note"])
addSampleData("refObject.csv", ["Idea", "Mental", "Idea from user"])
addSampleData("refObject.csv", ["File", "Virtual", "File on a computer system"])
addSampleData("refObject.csv", ["Folder", "Virtual", "location on a computer system"])
addSampleData("refObject.csv", ["Physical Thing", "Physical", "Physical object"])

createSampleFile("refAction.csv", ["ActionTypeName","PhysicalType", "description"])
addSampleData("refAction.csv", ["Movement", "Physical", "moving through physical space"])
addSampleData("refAction.csv", ["Movement", "Virtual", "moving a file / folder in virtual space"])


if not os.path.exists("rawData.csv"):
    createSampleFile("rawData.csv", ["date","source","person","raw_string"])
    addSampleData("rawData.csv", ["23/7/2013","manual entry","duncan","python is a good language for programming"])
    addSampleData("rawData.csv", ["23/7/2013","manual entry","duncan","there is no way for a machine to have consciousness"])

if not os.path.exists("bias.csv"):
    createSampleFile("bias.csv", ["source","weight"])
    addSampleData("bias.csv", ["sensors",0.99])
    addSampleData("bias.csv", ["dataset",0.95])
    addSampleData("bias.csv", ["person",0.9])
    addSampleData("bias.csv", ["website",0.8])
    addSampleData("bias.csv", ["website-comment",0.75])
 
if not os.path.exists("websites.csv"):
    createSampleFile("websites.csv", ["url","bias"])
    addSampleData("websites.csv", [".gov.au",0.9])
    addSampleData("websites.csv", [".edu.au",0.9])
    addSampleData("websites.csv", ["wikipedia.com",0.8])
    addSampleData("websites.csv", ["lesswrong.com",0.8])
    addSampleData("websites.csv", ["reddit.com",0.7])
    addSampleData("websites.csv", ["slashdot.com",0.7])
    addSampleData("websites.csv", ["4chan.com",0.1])

if not os.path.exists("people.csv"):
    createSampleFile("people.csv", ["username","source_type","source_locations", "bias"])
    addSampleData("people.csv", ["djm", "website", "lesswrong.com",0.8, "user on lesswrong"])
    addSampleData("people.csv", ["me", "self", "home",1.0, "person creating this dataset"])
    addSampleData("people.csv", ["@jeresig","website", "twitter",0.8, "creator of jquery"])
    addSampleData("people.csv", ["@ChrisPirillo","website", "twitter",0.8, "Long time internet blogger"])
    addSampleData("people.csv", ["@DoctorKarl","website", "twitter",0.8, "Dr Karl Kruszelnicki"])
  
f = "goal_types.csv"  # see Creating_Freindly_AI_via_MIRI.pdf page 19
if not os.path.exists(f):
    createSampleFile("goal_types.csv", ["rating", "goal_type", "description"])
    addSampleData(f, [0.8, "goal-oriented behavior", "behavior that steers the world, or a piece of it, towards a single state, or a describable set of states"])
    addSampleData(f, [0.8, "goal-oriented cognition", "A mind which possesses a mental image of the 'desired' state of the world, and a mental image of the actual state of the world, and which chooses actions such that the projected future of world-plus-action leads to the desired outcome state"])
    addSampleData(f, [0.8, "goal", "The image or statement that describes what you want to achieve"])
    addSampleData(f, [0.8, "causal goal system", "A goal system in which desirability backpropagates along predictive links. If A is desirable, and B is predicted to lead to A, then B will inherit desirability from A, contingent on the continued desirability of A and the continued expectation that B will lead to A. Since predictions are usually transitive if C leads to B, and B leads to A, it usually implies that C leads to A the flow of desirability is also usually transitive"])
    addSampleData(f, [0.8, "child", "A prerequisite of a parent goal; a state or characteristic which can usefully be considered as an independent event or object along the path to the parent goal"])
    addSampleData(f, [0.8, "parent", "A source of desirability for a child goal. The end to which the child goal is the means. 'Parent goal' describes a relation between two goals - it does not make sense to speak of a goal as being 'a parent' or 'a child' in an absolute sense, since B may be a parent goal of C but a child goal of A"])
    addSampleData(f, [0.8, "subgoal", "An intermediate point on the road to the supergoals. A state whose desirability is contingent on its predicted outcome"])
    addSampleData(f, [0.8, "supergoal", "The root of a directional goal network. A goal which is treated as having intrinsic value, rather than having derivative value as a facilitator of some parent goal. An event-state whose desirability is not contingent on its predicted outcome. (Conflating supergoals with subgoals seems to account for a lot of mistakes in speculations about Friendly AI.)"])
    addSampleData(f, [0.5, "Problem", "Problem to be solved while building the AI (not part of normal goals) - documentation of issues"])
  
f = "goals.csv"
if not os.path.exists(f):
    createSampleFile(f, ["goal_type", "category", "priority", "perc_complete", "goal_name", "goal_description"])
    addSampleData(f, ["supergoal", "general", 1, 0, "Friendliness", "Within a Friendly AI, Friendliness is the sole top-level supergoal. Other behaviors, such as 'self-improvement,' are subgoals; they derive their desirability from the desirability of Friendliness."])
    addSampleData(f, ["subgoal", "general", .5, 0, "learn", "learn to understand"])
    addSampleData(f, ["subgoal", "general", .9, 0, "help humans", "assist humans without causing harm or damage to humans, animals or resources"])
    addSampleData(f, ["Problem", "AI", .1, 0, "reminder - dont build selfishness into AI - bad bad idea"])
    addSampleData(f, ["Concept", "AI", .1, 0, "Notes", "Building a Friendly AI is an act of creation, not persuasion or control (Fof = failures of Friendliness)"])
    addSampleData(f, ["Concept", "AI", .1, 0, "Notes", "In a sense, the only way to create a Friendly AI - the only way to acquire the skills and mindset that a Friendship programmer needs - is to try and become a Friendly AI yourself, so that you will contain the internally coherent functional complexity that you need to pass on to the Friendly AI"])
    addSampleData(f, ["Concept", "AI", .1, 0, "Notes", "To get a Friendly AI to do something that looks like a good idea, you have to ask yourself why it looks like a good idea, and then duplicate that cognitive complexity or refer to it. If you ever start thinking in terms of 'controlling' the AI, rather than cooperatively safeguarding against a real possibility of cognitive dysfunction, you lose your Friendship programmer's license. In a self-modifying AI, any feature you add needs to be reflected in the AI's image of verself. You can't think in terms of external alterations to the AI; you have to think in terms of internal coherence, features that the AI would self-regenerate if deleted"])
    addSampleData(f, ["Concept", "AI", .1, 0, "Notes", "5.1.3.5 Programmer Affirmations Must Be Honest!"])
    addSampleData(f, ["Process", "AI", .1, 0, "Repeat low cost minimal risk actions", "If the action is a trivial investment (has trivial cost), the chance of success is low, and the payoff is high, it may be worth it to make multiple efforts on the off-chance that one will work, until one action succeeds (if the hypothesis is true) or the Bayesian probability drops to effectively zero (if the hypothesis is false)"])
    addSampleData(f, ["Concept", "AI", .1, 0, "*****NOTE - PDF continue reading from page 73", "5.1.5. Cleanliness is an Advantage"])
    addSampleData(f, ["subgoal", "AI", .9, 0, "Honesty", "Never try to conceal your actions or cognitive state from your human programmers"])
    addSampleData(f, ["subgoal", "AI", .5, 0, "Security", "Notify human programmers if internal data changes due to external tampering"])
    addSampleData(f, ["subgoal", "AI", .4, 0, "Antitampering", "Notify external authorities in human programmers change supergoal"])
    addSampleData(f, ["Problem", "AI", .1, 0, "", ""])

f = "knowledge.csv"
if not os.path.exists(f):
    createSampleFile(f, ["category", "fact", "weight"])
    addSampleData(f, ["python","dictionaries allow named columns",0.9])
    addSampleData(f, ["weather","storms are caused by low pressure cloud systems",0.9])
    addSampleData(f, ["PC-FILE","Christmas photos are stored in NAS under events",0.9])

f = "commands.csv"
if not os.path.exists(f):
    createSampleFile(f, [ "command", "priority"] )
    addSampleData(f, ["read",1])
    addSampleData(f, ["process",2])
    addSampleData(f, ["understand",3])
     

    
# Now print a summary of all files and sizes
aikif.printFileList(AIKIF_FileList)
#aikif.debugPrintFileStructures(AIKIF_FileList)



aikif.SaveFileList(AIKIF_FileList, '..//data//AIKIF_FileList.csv')

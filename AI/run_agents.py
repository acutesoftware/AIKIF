# run_agents.py	written by Duncan Murray  20/4/2014
# manages the agents schedules and calls programs as needed


import sys, os

schedule_types = ['once', 'year', 'month', 'fortnight', 'week', 'weekday', 'day', 'hour', 'minute', 'second', 'always']

agentCodeFolder = os.path.dirname(os.path.abspath(__file__)) + os.sep 

agent_list = [
	{'name': 'Browser history', 
	 'file': agentCodeFolder + 'agents\\gather\\log_browser_history.py', 
	 'schedule_type':'week'
	},
	{'name': 'PC Usage', 
	 'file': agentCodeFolder + 'agents\\gather\\log_PC_usage.py', 
	 'schedule_type':'minute'
	},
	{'name': 'Aggregate PC usage', 
	 'file': agentCodeFolder + 'agents\\aggregate\\load_PC_usage.py', 
	 'schedule_type':'hour'
	},
	{'name': 'Aggregate Context', 
	 'file': agentCodeFolder + 'agents\\aggregate\\agg_context.py', 
	 'schedule_type':'hour' 
	}
]


import os, sys
#sys.path.append(os.path.split(sys.argv[0])[0])
print(os.path.split(sys.argv[0])[0])
import AIKIF_utils as aikif
import fileMapping as filemap 


			
def main():
	if verify_agents() == True:
		print('Agents verified')

	for i in agent_list:
		if is_agent_scheduled_to_start(i) is True:
			run(i['file'], True)

def verify_agents():
	all_good = True
	for i in agent_list:
		if i['schedule_type'] not in schedule_types:
			all_good = False
			print('ERROR - ', i['name'], 'has invalid schedule type', i['schedule_type'])
		if not os.path.isfile(i['file']):
			all_good = False
			print('ERROR - ', i['name'], 'program does not exist', i['file'])

def run(scriptFile, logUsage='Y'):
	from subprocess import call
	print('  ... running ' + scriptFile)
	aikif.LogProcess(scriptFile)
	try:
		retcode = call(scriptFile + ' Q', shell=True)   # Q tells program to run in silent mode
		if retcode < 0:
			#print("Child was terminated by signal", -retcode, file=sys.stderr)
			aikif.LogResult(scriptFile + ' terminated by signal')
		else:
			#print("Child returned", retcode, file=sys.stderr)
			aikif.LogResult(scriptFile + ' success')
	except OSError as e:
		#print("Execution failed:", e, file=sys.stderr)	
		aikif.LogResult(scriptFile + ' error')
	
			
def is_agent_scheduled_to_start(agt):
	# todo
	if agt['schedule_type'] == 'minute':
		return True
	else:
		print('Not scheduled to run ', agt['name'])
		return False
			
if __name__ == '__main__':
    main()	
	



# run_agents.py	written by Duncan Murray  20/4/2014
# manages the agents schedules and calls programs as needed

schedule_types = ['once', 'year', 'month', 'fortnight', 'week', 'weekday', 'day', 'hour', 'minute', 'second', 'always']

agent_list = [
	{'name': 'Browser history', 
	 'file': 'gather//log_browser_history.py', 
	 'schedule_type':'week'
	},
	{'name': 'PC Usage', 
	 'file': 'gather//log_PC_usage.py', 
	 'schedule_type':'always'
	},
	{'name': 'Aggregate PC usage', 
	 'file': 'aggregate//load_PC_usage.py', 
	 'schedule_type':'hour'
	},
	{'name': 'Identify Context', 
	 'file': 'aggregate//context.py', 
	 'schedule_type':'minute' 
	}
]


import os
			
def main():
	if verify_agents() == True:
		print('Agents verified')
		

def verify_agents():
	all_good = True
	for i in agent_list:
		if i['schedule_type'] not in schedule_types:
			all_good = False
			print('ERROR - ', i['name'], 'has invalid schedule type', i['schedule_type'])
		if not os.path.isfile(i['file']):
			all_good = False
			print('ERROR - ', i['name'], 'program does not exist', i['file'])
	
if __name__ == '__main__':
    main()	
	



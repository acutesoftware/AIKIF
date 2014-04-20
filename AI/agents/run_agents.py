# run_agents.py	written by Duncan Murray  20/4/2014
# manages the agents schedules and calls programs as needed

agent_list = [
	{'name': 'Browser history', 'file': 'gather//log_browser_history.py', 'schedule_type':'week', 'last_run':'20/4/2014'},
	{'name': 'PC Usage', 'file': 'gather//log_PC_usage.py', 'schedule_type':'always', 'last_run':'20/4/2014'},
	{'name': 'Aggregate PC usage', 'file': 'aggregate//load_PC_usage.py', 'schedule_type':'hour', 'last_run':'20/4/2014'},
	{'name': 'Identify Context', 'file': 'aggregate//context.py', 'schedule_type':'minute', 'last_run':'20/4/2014'}
]
	
for i in agent_list:
	print('running agent', i['name'])

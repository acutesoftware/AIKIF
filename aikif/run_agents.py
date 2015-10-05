# run_agents.py written by Duncan Murray  20/4/2014
# manages the agents schedules and calls programs as needed


import os
import aikif.cls_log as mod_log

schedule_types = ['once', 'year', 'month', 'fortnight', 'week', 'weekday', 'day', 'hour', 'minute', 'second', 'always']

#print('run_agents imported')

agentCodeFolder = os.path.dirname(os.path.abspath(__file__)) + os.sep 

agent_list = [
    {'name': 'Browser history', 
     'file': os.path.join(agentCodeFolder,'agents','gather','log_browser_history.py'), 
     'schedule_type':'week'
    },
    {'name': 'PC Usage', 
     'file': os.path.join(agentCodeFolder,'agents','gather','log_PC_usage.py'), 
     'schedule_type':'second'
    },
    #{'name': 'Aggregate PC usage', 
    # 'file': os.path.join(agentCodeFolder,'agents','aggregate','load_PC_usage.py'), 
    # 'schedule_type':'minute'
    #},
    {'name': 'File Usage', 
     'file': os.path.join(agentCodeFolder,'agents','gather','agent_filelist.py'), 
     'schedule_type':'hour'
    },
    #{'name': 'Aggregate Context', 
    # 'file': os.path.join(agentCodeFolder,'agents','aggregate','agg_context.py'), 
    # 'schedule_type':'minute' 
    #}
]

        
def main():
    if verify_agents(agent_list) == True:
        print('Agents verified')
    for i in agent_list:
        if is_agent_scheduled_to_start(i) is True:
            run(i['file'], True)

def get_agent_list():
    print('RETURNING AGENT LIST\n\n')
    return agent_list
            
def verify_agents(l_agent_list):
    all_good = True
    for i in l_agent_list:
        if i['schedule_type'] not in schedule_types:
            all_good = False
            print('ERROR - ', i['name'], 'has invalid schedule type', i['schedule_type'])
        if not os.path.isfile(i['file']):
            all_good = False
            print('ERROR - ', i['name'], 'program does not exist', i['file'])
    return all_good

def run(scriptFile, logUsage='Y'):
    from subprocess import call
    print('  ... running ' + scriptFile)
    lg = mod_log.Log(os.getcwd())
    lg.record_process(scriptFile)
    try:
        retcode = call(scriptFile + ' Q', shell=True)   # Q tells program to run in silent mode
        if retcode < 0:
            if logUsage=='Y':
                lg.record_result(scriptFile + ' terminated by signal')
        else:
            if logUsage=='Y':
                lg.record_result(scriptFile + ' success')
    except OSError as e:
        #print("Execution failed:", e, file=sys.stderr) 
        lg.record_result(scriptFile + ' error' + str(e))
    
            
def is_agent_scheduled_to_start(agt):
    # todo
    if agt['schedule_type'] == 'minute':
        return True
    else:
        print('Not scheduled to run ', agt['name'])
        return False
            
if __name__ == '__main__':
    main()  
    



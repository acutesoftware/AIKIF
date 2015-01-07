# run_dummy_learn_1.py      # written by Duncan Murray 7/1/2015

import os
import sys
import random

"""
Steps to run and Log an external AI program
"""

# 1. Setup AIKIF for logging
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." ) 
sys.path.append(root_folder)
import aikif.agents.agent as mod_agt
import aikif.cls_log as mod_log
import aikif.config as mod_cfg

lg = mod_log.Log(root_folder)


# 2. Record details
your_param1 = 999.999
your_param2 = 'test17'
your_param3 = [12,54,23,65,987]
lg.record_command('Initialise Dummy Learning algorithm', 'dummy_learn_1.py')
lg.record_source('PARAM: your_param1 = ' + str(your_param1), 'dummy_learn_1.py')
lg.record_source('PARAM: your_param2 = ' + your_param2, 'dummy_learn_1.py')
lg.record_source('PARAM: your_param3 = ' + str(your_param3), 'dummy_learn_1.py')



# 3. Import and run your algorithm
import dummy_learn_1 as your_ai 
result = your_ai.main(your_param1, your_param2, your_param3)


# 4. Finish log timing and Show results
lg.record_result('result = ' + str(result), 'dummy_learn_1.py')
sum = mod_log.LogSummary(lg, root_folder)
sum.summarise_events()
print(sum)

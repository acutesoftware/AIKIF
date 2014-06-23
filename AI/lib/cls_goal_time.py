# cls_goal_time.py

from cls_goal import Goal

class GoalTime(Goal):
    """ 
    goals around time - eg maximise use of object / minimize time of task
    """
    def __init__(self, maximise=True, current_val=0, target_val=0):
        """
        set maximise = True for class to find maximum time (usage) or
        set to False to minimise the amount of time (eg reduce task time)
        """
        self.current_val = current_val
        self.target_val = target_val
        self.maximise = maximise
        self.strategy = [
            {'name':'Travel_walk', 'speed':1, 'max_km_day':30, 'dest_flexibility':100, 'money_cost':0, 'environ_cost':0},
            {'name':'Travel_bike', 'speed':5, 'max_km_day':200, 'dest_flexibility':50, 'money_cost':0, 'environ_cost':0},
            {'name':'Travel_car', 'speed':60, 'max_km_day':1500, 'dest_flexibility':30, 'money_cost':50, 'environ_cost':50},
            {'name':'Travel_bus', 'speed':60, 'max_km_day':1500, 'dest_flexibility':20, 'money_cost':10, 'environ_cost':15}
        ]
        
        
	def check_for_success(self):
		return False

    def run_plan(self, strategy):
        """ 
        executes a plan by running the passed strategy
        and then updates the local results
        """
        print ("running strategy : " + strategy['name'])
        

    def find_best_plan(self):
        """
        try each strategy with different amounts
        """
        for plan in self.plans:
            for strat in self.strategy:
                run_plan(strat)
                
# cls_context.py    written by Duncan Murray 6-Sep-2014

import os

#####################################################
# Change User Settings below (currently hard coded)
hosts = [
    dict(type='Work PC', name='xxxxxxxxx'),
    dict(type='Home PC', name='Treebeard'),
    dict(type='Laptop', name='Ent'),            
    dict(type='Server', name='Fangorn'),       
    dict(type='Phone',  name='GT-19001T'),       
]

users = [
    dict(type='Developer', name='Duncan'),
    dict(type='User',      name='murraydj'),
    dict(type='Tester',    name='test'),
    dict(type='web_user',  name='web*'),
]

transport = [
    dict(type='None',  name='inside'),
    dict(type='Walk',  name='Walk'),
    dict(type='Car',   name='Car'),
    dict(type='Public',name='Tram'),  # <-- edit your preferred public transport
]


#####################################################

physical = ['home', 'work', 'travelling']

files = []
usage = []

mode = ['work', 'business', 'email', 'web', 'games', 'media', 'nonPC']
tpe = ['passive', 'typing', 'clicking']

class Context(object):
    """
    This class does a best guess to return a plain english version 
    of what the user (you), this software (aikif) and the computer is doing.
    
    """
    def __init__(self):
        self.user, self.username = self.get_user()
        self.host, self.hostname = self.get_host()
        self.transport = self.inspect_phone()
        self.summary = self.summarise()
        self.host_cpu_pct, self.host_num_processes, self.host_mem_available, self.host_mem_total = self.get_host_usage()
        
    def __str__(self):  
        return 'Hello, ' + self.username + '! You are a ' + self.user + ' using the ' + self.host + ' "' + self.hostname + '"'
    
    def dump_all(self, silent='NO'):
        """ 
        prints all attributes and returns them as a dictionary 
        (mainly for testing how it will all integrate)
        """
        all_params = []
        all_params.append(dict(name='phone', val=self.transport))
        all_params.append(dict(name='username', val=self.username))
        all_params.append(dict(name='user', val=self.user))
        all_params.append(dict(name='hostname', val=self.hostname))
        all_params.append(dict(name='host', val=self.host))
        all_params.append(dict(name='cpu_pct', val=self.host_cpu_pct))
        all_params.append(dict(name='num_proc', val=self.host_num_processes))
        all_params.append(dict(name='mem_avail', val=self.host_mem_available))
        all_params.append(dict(name='mem_total', val=self.host_mem_total))
        if silent != 'NO':
            for a in all_params:
                print(a['name'].ljust(14) + '= ' + a['val'])
    
        return all_params
        
    def summarise(self):
        """ extrapolate a human readable summary of the contexts """
        if self.user == 'Developer': 
            if self.host == 'Home PC':
                res = 'At Home'
            else:
                res = 'Away from PC'
        elif self.user == 'User' and self.host == 'Home PC':
            res = 'Remote desktop into home PC'
        res += '\n'
        res += self.transport
        return res
    

    def is_user_busy(self):
        """ determines from user details if user is busy or not """
        if self.phone_on_charge is True and self.user == 'Developer':
            return False
        else:
            return True
    
    def is_host_busy(self):
        """ determines from host details if computer is busy or not """
        if self.host_cpu_pct > '25' or self.host_mem_available < '500000':
            return False
        else:
            return True
    
    def get_host(self):
        """ 
        returns the host computer running this program 
        """
        import socket
        host_name = socket.gethostname()
        for h in hosts:
            if h['name'] == host_name:
                return h['type'], h['name']
        
    def get_user(self):
        """ 
        returns the username on this computer 
        """
        for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
            user = os.environ.get(name)
            if user:
                break     
        for u in users:
            if u['name'] == user:
                return u['type'], u['name']
    
    def inspect_phone(self):
        """
        FUNCTION STUB - TODO
        The intention is to get data from the mobile in the format:
            gps_lat         = 137.000
            gps_lng         = 100.000
            moving          = True | False
            move_dist_10_sc = 0
            move_dist_2_mn  = 4
            move_dist_10_mn = 4
            move_dist_2_hr  = 4
            screen_saver    = True | False
            on_charge       = True | False
        """
        self.phone_gps_lat = 137.0000
        self.phone_gps_lng = 100.0000
        self.phone_moving = False
        self.phone_move_dist_2_mn = 4
        self.phone_on_charge = True
        self.screen_saver = False
        #-------------------------------
        phone_status = ''
        if self.phone_on_charge is True:
            phone_status += 'Phone is charging'
            if self.phone_moving is True:
                phone_status += ', driving in Car'
            else:
                phone_status += ', sitting still'
        else:
            if self.screen_saver is False:
                phone_status += 'Phone is being used'
            else:
                phone_status += 'Phone is off'
            if self.phone_moving is True:
                if self.phone_move_dist_2_mn < 5:
                    phone_status += ', going for Walk'
                elif  self.phone_move_dist_2_mn > 500:
                    phone_status += ', flying on Plane'
                else:    
                    phone_status += ', riding on public transport'
        return phone_status

    def get_host_usage(self):
        """ get details of CPU, RAM usage of this PC """
        import psutil
        process_names = [proc.name for proc in psutil.process_iter()]
        cpu_pct = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        return str(cpu_pct), str(len(process_names)), str(mem.available), str(mem.total)
        
def TEST():
    """ self testing context class """
    where_am_i = Context()
    #print(where_am_i)
    #print(where_am_i.summarise())
    where_am_i.dump_all('yes')
    print(where_am_i.get_host())
    for k,v in os.environ.items():
        print(k,v)
    print(where_am_i.get_user()[0])
    where_am_i.get_host_usage()
       
if __name__ == '__main__':
    TEST()
            
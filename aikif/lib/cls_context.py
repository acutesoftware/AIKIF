#!/usr/bin/python3
# -*- coding: utf-8 -*-
# cls_context.py

import os

#####################################################
# Change User Settings below (currently hard coded)
hosts = [
    dict(type='Work PC', name='xxxxxxxxx'),
    dict(type='Home PC', name='treebeard'),
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

logged_ssids = [
    dict(location='Home', name='AcuteSoftware', owned_by='Me'),
    dict(location='Home', name='Netcomm Duplicate Name', owned_by='Unknown'),
    dict(location='Home', name='Blah Modem', owned_by='Unknown'),
    dict(location='Work', name='123NETCOM', owned_by='Unknown'),
    dict(location='Work', name='Tesltra 3G', owned_by='Unknown'),
    dict(location='Work', name='Netcomm Duplicate Name', owned_by='Unknown'),
    dict(location='Work', name='Cafe Awesome', owned_by='Unknown'),
    dict(location='Work', name='my_3G', owned_by='Me')
]    
    
#####################################################

physical = ['home', 'work', 'travelling']

files = []
usage = []

mode = ['work', 'business', 'email', 'web', 'games', 'media', 'nonPC']
tpe = ['passive', 'typing', 'clicking']



def where_am_i():
    """
    high level function that can estimate where user is based 
    on predefined setups.
    """
    locations = {'Work':0, 'Home':0}
    for ssid in scan_for_ssids():
        #print('checking scanned_ssid ', ssid)
        for l in logged_ssids:
            #print('checking logged_ssid ', l)
            if l['name'] == ssid:
                locations[l['location']] += 1
                #print('MATCH')
    print('Where Am I: SSIDS Matching Home = ', locations['Home'], ' SSIDs matching Work = ', locations['Work'])
    if locations['Home'] > locations['Work']:
        return 'Home'
    else:
        return 'Work'
       
    
    
def scan_for_ssids():
    """
    this currently returns a list but should use the wifi
    module to scan for local ssids - not quite sure how this
    will work on CI
    """
    return ['AcuteSoftware', 'Netcomm Duplicate Name', 'Some other SSID']


class Context(object):
    """
    This class does a best guess to return a plain english version 
    of what the user (you), this software (aikif) and the computer is doing.
    """
    def __init__(self):
        self.user = ''
        self.username = ''
        self.host = ''
        self.hostname = ''
        try:
            self.user, self.username = self.get_user()
        except Exception as ex:
            print('Error:cls_context cant identify user ' + str(ex))
        try:
            self.host, self.hostname = self.get_host()
        except Exception as ex:
            print('Error:cls_context cant identify host ' + str(ex))
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
        """ 
        extrapolate a human readable summary of the contexts 
        """
        res = ''
        if self.user == 'Developer': 
            if self.host == 'Home PC':
                res += 'At Home'
            else:
                res += 'Away from PC'
        elif self.user == 'User' and self.host == 'Home PC':
            res += 'Remote desktop into home PC'
        res += '\n'
        res += self.transport
        return res
    

    def is_user_busy(self):
        """ 
        determines from user details if user is busy or not 
        """
        if self.phone_on_charge is True and self.user == 'Developer':
            return False
        else:
            return True
    
    def is_host_busy(self):
        """ 
        determines from host details if computer is busy or not 
        """
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
        return dict(type='Unknown', name=host_name)
        
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
    
    def inspect_phone(self, gps_lat_long = [137.0000,100.0000], moving = False, move_dist_2_mn = 4, on_charge = True, screen_saver = False):
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
        
        
        self.phone_gps_lat = gps_lat_long[0]
        self.phone_gps_lng = gps_lat_long[1]
        self.phone_moving = moving
        self.phone_move_dist_2_mn = move_dist_2_mn
        self.phone_on_charge = on_charge
        self.screen_saver = screen_saver
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
        """ 
        get details of CPU, RAM usage of this PC 
        """
        import psutil
        process_names = [proc.name for proc in psutil.process_iter()]
        cpu_pct = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        return str(cpu_pct), str(len(process_names)), str(mem.available), str(mem.total)
        


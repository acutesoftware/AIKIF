#!/usr/bin/python3
# -*- coding: utf-8 -*-
# core_data.py
import os

core_data_types = [ 'Character',    # Who
                    'Object',       # What
                    'Location',     # Where
                    'Event',        # When
                    'Process',      # How
                    'Fact'          # Why
                  ]
        
core_process =    [ 'List',
                  ]
        
class CoreData(object):
    """
    Base class for all core data objects
    """
    def __init__(self, name, data=None, parent=None):
        """ 
        define an object with a name
        """
        self.name = name
        self.data = data    # can be as detailed or simple as needed
        self.parent = parent
        self.child_nodes = []
        self.links = []
        self.data_type = ''
        self.type_desc = ''
        
    def __str__(self):
        if self.data_type == '':
            return self.name
        else:
            return self.name +  ' (type=' + self.data_type + ')'
    
        
    def format_csv(self, delim=',', qu='"'):
        """
        Prepares the data in CSV format
        """
        res = qu + self.name + qu + delim
        if self.data:
            for d in self.data:
                res += qu + str(d) + qu + delim
        return res + '\n'
        
    def format_dict(self, delim=':', qu="'"):
        """
        Prepares the data as a dictionary with column headers
        TODO - get variable names of data[] as strings for hdr
        """
        res = 'name' + delim + qu + self.name + qu + ','
        for num, d in enumerate(self.data):
            res += 'col' + str(num) + delim + qu + str(d) + qu + ','
        return res
    
    def format_all(self):
        """
        return a trace of parents and children of the obect
        """
        res = '\n--- Format all : ' + str(self.name) + ' -------------\n'
        res += ' parent = ' + str(self.parent) + '\n'
        res += self._get_all_children()    
        res += self._get_links()
            
        return res

    def _get_all_children(self,):
        """ 
        return the list of children of a node
        """
        res = ''
        if self.child_nodes:
            for c in self.child_nodes:
                res += ' child = ' + str(c) + '\n'
                if c.child_nodes:
                    for grandchild in c.child_nodes:
                        res += '   child = ' + str(grandchild) + '\n'
        else:
            res += ' child = None\n'
        return res
        
    def _get_links(self,):
        """ 
        return the list of links of a node
        """
        res = ''
        if self.links:
            for l in self.links:
                res += ' links = ' + str(l[0]) + '\n'
                if l[0].child_nodes:
                    for chld in l[0].child_nodes:
                        res += '   child = ' + str(chld) + '\n'
                if l[0].links:
                    for lnk in l[0].links:
                        res += '   sublink = ' + str(lnk[0]) + '\n'
        else:
            res += ' links = None\n'
            
        return res
        
    
    
    
    def drill_down(self):
        """ 
        this WALKS down the tree to get the LIST of 
        nodes at the detail level (see expand to actually
        add the list of nodes
        
        TODO = processes need to be recalculated
        """
        return self.child_nodes
        
    def drill_up(self):  
        """
        returns the parent note - opposite of drill down
        TODO = processes need to be recalculated
        """
        return self.parent
    
    def expand(self, process, child_nodes):
        """
        this expands a current node by defining ALL the 
        children for that process
        TODO = processes need to be recalculated
        """
        #print('TODO: process check = ', process)
        #print(self.name, ' expanded to ->', child_nodes)
        self.child_nodes = []  
        for n in child_nodes:
            self.child_nodes.append(CoreData(n, parent=self))

    def contract(self, process):
        """
        this contracts the current node to its parent and 
        then either caclulates the params and values if all 
        child data exists, OR uses the default parent data.
        (In real terms it returns the parent and recalculates)
        TODO = processes need to be recalculated
        """
        print('TODO: process check = ', process)
        print(self.name, ' contracted to ->', self.parent)
        return self.parent
    
    def get_child_by_name(self, name):
        """
        find the child object by name and return the object
        """
        for c in self.child_nodes:
            if c.name == name:
                return c
        return None
        
    def links_to(self, other, tpe):
        """
        adds a link from this thing to other thing
        using type (is_a, has_a, uses, contains, part_of)
        """
        if self.check_type(tpe):
            self.links.append([other, tpe])
        else:
            raise Exception('aikif.core_data cannot process this object type')
        
    def check_type(self, tpe):
        """
        TODO - fix this, better yet work out what the hell
        you are trying to do here.
        returns the type of object based on type string
        """
        for v in core_data_types:
            if tpe == v:
                return True
        return False
        

class CoreDataWho(CoreData):
    def __init__(self, name, data=None, parent=None):
        """
        WHO
        Characters are physical people, or software agents
        data = ['Name', 'Phys|Virt', rights]
        """
        
        CoreData.__init__(self, name, data, parent)
        self.data_type = 'who'
        self.type_desc = 'Character'
        
    def __str__(self):
        return CoreData.__str__(self)
    
        
class CoreDataWhat(CoreData):
    def __init__(self, name, data=None, parent=None):
        """
        WHAT
        Objects currently dont have any additional 
        data properties
        """
        CoreData.__init__(self, name, data, parent)
        self.data_type = 'what'
        self.type_desc = 'Object'
    
    def __str__(self):
        return CoreData.__str__(self)
        
    
class CoreDataWhere(CoreData):
    def __init__(self, name, data=None, parent=None):
        """
        WHERE
        Locations are physical or virtual places
        data = ['Name', 'Phys|Virt', 'Location']
        """
        
        CoreData.__init__(self, name, data, parent)
        self.data_type = 'where'
        self.type_desc = 'Location'
        
    def __str__(self):
        return CoreData.__str__(self)
    
class CoreDataWhen(CoreData):
    def __init__(self, name, data=None, parent=None):
        """
        WHEN
        Events have a simple data structure
        date, category, remind_time, event
        """
        #data = [date, category, details]
        
        CoreData.__init__(self, name, data, parent)
        self.data_type = 'when'
        self.type_desc = 'Event'

    def __str__(self):
        return CoreData.__str__(self)
    
class CoreDataHow(CoreData):
    def __init__(self, name, data=None, parent=None):
        """
        HOW
        Processes are the act of doing things physically
        such as 'build a boat', 'hammer a nail', 'go to shops',
        or software processes (BAT runs , etc)
        data = ['Name', 'Phys|Virt', start_name]
        """
        
        CoreData.__init__(self, name, data, parent)
        self.data_type = 'how'
        self.type_desc = 'Process'
        
    def __str__(self):
        return CoreData.__str__(self)
        
class CoreDataWhy(CoreData):
    def __init__(self, name, data=None, parent=None):
        """
        WHY
        Facts are all other information or generally LINKS
        between other types, eg 
            John ate an Apple => Who.John How.Ate What.Apple
            Mars is heavy => What.Mars Process.PropertyEquals 'heavy' <--- how to classify this
        
        data = ['Name', 'Phys|Virt', start_name]
        """
        
        CoreData.__init__(self, name, data, parent)
        self.data_type = 'why'
        self.type_desc = 'Fact'
        
    def __str__(self):
        return CoreData.__str__(self)
    
class CoreTable(object):
    """
    Class to manage the collection of multiple CoreData 
    objects. Keeps everything as a list of objects such
    as Events, Locations, Objects, etc and handles the 
    saving, loading and searching of information.
    """
    def __init__(self, fldr, tpe, user, header):
        self.type = tpe
        self.user = user
        self.fldr = fldr
        self.table = []    # list of data - eg events, locations, etc
        self.header = header # mod_core.Event('Name', 'Date', 'Journal', 'Details')
        
    def __str__(self):
        res = ''
        res += ' type = ' + self.type + '\n'
        res += ' user = ' + self.user + '\n'
        res += ' fldr = ' + self.fldr + '\n'
        for e in self.table:
            res += e.format_csv()
        return res
    
    def get_filename(self, year):
        """
        returns the filename
        """
        res = self.fldr + os.sep + self.type + year + '.' + self.user 
        return res
    
    def add(self, e):
        self.table.append(e)

    def find(self, txt):
        result = []
        for e in self.table:
            print('find(self, txt) e = ', e)
            if txt in str(e):
                result.append(e)
                #print(e)
        return result
    
    def save(self, file_tag='2016', add_header='N'):
        """
        save table to folder in appropriate files
        NOTE - ONLY APPEND AT THIS STAGE - THEN USE DATABASE
        """
        fname = self.get_filename(file_tag)
        with open(fname, 'a') as f:
            if add_header == 'Y':
                f.write(self.format_hdr())
                
            for e in self.table: 
                    f.write(e.format_csv())

    def format_hdr(self, delim=',', qu='"'):
        """
        Prepares the header in CSV format
        """
        res = ''
        if self.header:
            for d in self.header:
                res += qu + str(d) + qu + delim
        return res + '\n'

                
    def generate_diary(self):
        """
        extracts event information from core tables into diary files
        """
        print('Generate diary files from Event rows only')
        for r in self.table:
            print(str(type(r)) + ' = ', r)
        

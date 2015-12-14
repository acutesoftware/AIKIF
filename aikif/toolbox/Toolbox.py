#!/usr/bin/python3
# coding: utf-8
# toolbox.py   

import os
import sys
import aikif.cls_log as mod_log
import aikif.config as mod_cfg

class Toolbox(object):
    """
    Class to manage the functional tools (programs or functions) that the AI can use 
    The toolbox starts as a subset of the Programs class (Programs manage the users 
    list of written programs and applications), and its purpose is to have an interface
    that an AI can use to run its own tasks.
    The toolbox is basically detailed documentation and interfaces for any program or 
    function that is robust enough to be used.
    The first use of this will be the dataTools 'identify columns' function which calls
    a solver from this managed list
    
    """
    
    def __init__(self, fldr=None, lst=None):
        self.fldr = fldr
        self.lg = mod_log.Log(mod_cfg.fldrs['log_folder'])
        if lst is None:
            self.lstTools = [] 
        else:
            self.lstTools = lst 
        self.lg.record_command('Toolbox')
        self.lg.record_source(fldr)

    def __str__(self):
        """ 
        returns list of tools 
        """
        res = ''
        for tool in self.lstTools:
            res += self._get_tool_str(tool)
        return res
    
    def _get_tool_str(self, tool):
        """
        get a string representation of the tool
        """
        res = tool['file'] 
        try:
            res += '.' + tool['function']
        except Exception as ex:
            print('Warning - no function defined for tool ' + str(tool))
        res += '\n'
        return res
        
        
    def add(self, tool):
        """
        Adds a Tool to the list, logs the reference and TODO
        """
        self.lstTools.append(tool)
        self.lg.record_process(self._get_tool_str(tool))
        
    def list(self):
        """
        Display the list of items 
        """
        for i in self.lstTools:
            print (i)
        return self.lstTools
    
    def tool_as_string(self, tool):
        """
        return the string of the filename and function to call
        """
        return self._get_tool_str(tool)
    
    def save(self, fname=''):
        """
        Save the list of tools to AIKIF core and optionally to local file fname
        """
        if fname != '':
            with open(fname, 'w') as f:
                for t in self.lstTools:
                    self.verify(t)
                    f.write(self.tool_as_string(t))
 
    def verify(self, tool):
        """
        check that the tool exists
        """
        if os.path.isfile(tool['file']):
            print('Toolbox: program exists = TOK  :: ' + tool['file'])
            return True
        else:
            print('Toolbox: program exists = FAIL :: ' + tool['file'])
            return False

    def run(self, tool, args, new_import_path=''):
        """
        import the tool and call the function, passing the args.
        """
        if new_import_path != '':
            #print('APPENDING PATH = ', new_import_path)
            sys.path.append(new_import_path)
        
        #if silent == 'N':
        #    print('main called ' + tool['file'] + '->' + tool['function'] + ' with ', args, ' = ', tool['return'])
        mod = __import__( os.path.basename(tool['file']).split('.')[0]) # for absolute folder names
        # mod = __import__( tool['file'][:-2]) # for aikif folders (doesnt work)
        func = getattr(mod, tool['function'])
        tool['return'] = func(args)
        return tool['return']
        
        
        

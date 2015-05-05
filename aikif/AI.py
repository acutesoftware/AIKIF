# AI.py     written by Duncan Murray 2/5/2015

import os
import sys

# commands are structured as [lst_VALID_PROMPTS, str_FUNCTION_TO_CALL, str_DESCRIPTION]
all_commands = {}  
all_commands['exit'] = [[':q', '/q', 'exit', 'quit'], 'Exit the application']
all_commands['help'] = [[':h', '/h', 'help'], 'Show help']
all_commands['cmd'] =  [[':!', '/!', 'cmd', 'command'], 'Return to Command mode']
all_commands['add'] =  [[':a', '/a', 'add'], 'Enter Add mode']
all_commands['query'] =  [[':s', '/s', 'query', 'find', 'search'], 'Enter Query mode']

modes = ['COMMAND', 'ADD', 'QUERY']


def main():
    cmd = '?'
    mode = 'COMMAND'
    welcome()
    while cmd not in all_commands['exit'][0]:
        cmd = get_command(mode)
        #print('MAIN - cmd, mode = ', cmd, mode)
        result, mode = process(cmd, mode)
        show_output(result)

def get_command(mode):
    """
    Takes a raw user input, initially from command line
    Later: 
        - check user credentials
        - rate bias
        - check for malicious commands
    """
    if mode == 'COMMAND':
        prompt = '> '
    elif mode == 'ADD':
        prompt = 'ADD > '
    elif mode == 'QUERY':
        prompt = '?? > '
    txt = input(prompt)
    return txt 
 
def show_output(txt, device='Console'):
    """
    Output the data to the current device (usually
    screen via print statements but can be file or
    network / API
    """
    if device == 'Console':
        print(txt)
    elif device == 'File':
        raise ('show_output to File not implemented')

def process(txt, mode):
    """
    Top level function to process the command, mainly
    depending on mode.
    This should work by using the function name defined
    in all_commamnds
    """
    result = ''
    if mode == 'ADD':  # already in add mode, so add data
        if txt in all_commands['cmd'][0]:
            show_output('Returning to Command mode')
            mode = 'COMMAND'
            prompt = '> '
        else:
            show_output('Adding Text : ', txt)
            result = cmd_add(txt)
    elif mode == 'QUERY':
        if txt in all_commands['cmd'][0]:
            show_output('Returning to Command mode')
            mode = 'COMMAND'
            prompt = '> '
        else:
            show_output('Query : ', txt)
            result = cmd_query(txt)
    else:   
        if txt in all_commands['exit'][0]:
            cmd_exit()
            
        elif txt in all_commands['help'][0]:
            cmd_help()
            
        elif txt in all_commands['cmd'][0]:
            result = 'Returning to Command mode'
            mode = 'COMMAND'
            prompt = '> '
            
        elif txt in all_commands['add'][0]:
            result = 'Entering Add mode'
            mode = 'ADD'
            prompt = 'ADD > '
        
        elif txt in all_commands['query'][0]:
            result = 'Entering Query mode'
            mode = 'QUERY'
            prompt = '?? > '
        else:
            result = 'Unknown command - type help for list of commands'

    return result, mode
    
#####################################################
#  COMMAND PROCESSING FUNCTIONS
#####################################################  
  
def welcome():
    show_output('Welcome to the AIKIF Command Line Interface')
    
def cmd_exit():
    show_output('Bye')
    exit(0)
    

def cmd_help():
    txt = '\n'
    for k,v in all_commands.items():
        txt += k.ljust(6) + '= ' 
        txt += v[1].ljust(25)
        for cmd in v[0]:
            txt += cmd + ', '
        txt += '\n'
    show_output(txt)


def cmd_add(txt):
    """
    Enter add mode - all text entered now will be 
    processed as adding information until cancelled
    """
    show_output('Adding ', txt)
    return 'Added ' + txt
    

def cmd_query(txt):
    """
    search and query the AIKIF
    """
    show_output('Searching for ', txt)
    return 'Search results for ' + txt
    
if __name__ == '__main__':        
    main()
                
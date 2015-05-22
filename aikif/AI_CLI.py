# AI.py     written by Duncan Murray 2/5/2015

import aikif.knowledge

#modes = ['COMMAND', 'ADD', 'QUERY']

class AICLI(object):
    """
    main class for the CLI
    """
    def __init__(self, nme, auto_start = True):
        # commands are structured as [lst_VALID_PROMPTS, str_FUNCTION_TO_CALL, str_DESCRIPTION]
        self.all_commands = {}  
        self.nme = nme
        self.all_commands['exit'] = [[':q', '/q', 'exit', 'quit'], 'Exit the application']
        self.all_commands['help'] = [[':h', '/h', 'help'], 'Show help']
        self.all_commands['cmd'] =  [[':!', '/!', 'cmd', 'command'], 'Return to Command mode']
        self.all_commands['add'] =  [[':a', '/a', 'add'], 'Enter Add mode']
        self.all_commands['query'] =  [[':s', '/s', 'query', 'find', 'search'], 'Enter Query mode']
        self.cmd = '?'
        self.mode = 'COMMAND'
        self.raw = aikif.knowledge.RawData('test')
        self.welcome()
        if auto_start is True:
            self.start()
    
    def start(self):
        while self.cmd not in self.all_commands['exit'][0]:
            self.cmd = self.get_command(self.mode)
            result, self.mode = self.process(self.cmd, self.mode)
            self.show_output(result)
    
        
    def get_command(self, mode, txt=''):
        """
        Takes a raw user input, initially from command line
        Later: 
            - check user credentials
            - rate bias
            - check for malicious commands
        """
        if mode == 'COMMAND':
            self.prompt = '> '
        elif mode == 'ADD':
            self.prompt = 'ADD > '
        elif mode == 'QUERY':
            self.prompt = '?? > '
        if txt == '':
            txt = input(self.prompt)
        return txt 
     
    def show_output(self, txt, device='Console'):
        """
        Output the data to the current device (usually
        screen via print statements but can be file or
        network / API
        """
        if device == 'Console':
            print(txt)
        elif device == 'File':
            raise ('show_output to File not implemented')
        elif device == 'Function_Return':  # hacky, to run test_AI_CLI.py
            return txt   

    def process(self, txt, mode):
        """
        Top level function to process the command, mainly
        depending on mode.
        This should work by using the function name defined
        in all_commamnds
        """
        result = ''
        if mode == 'ADD':  # already in add mode, so add data
            if txt in self.all_commands['cmd'][0]:
                self.show_output('Returning to Command mode')
                mode = 'COMMAND'
                self.prompt = '> '
            else:
                self.show_output('Adding Text : ', txt)
                result = self.cmd_add(txt)
        elif mode == 'QUERY':
            if txt in self.all_commands['cmd'][0]:
                self.show_output('Returning to Command mode')
                mode = 'COMMAND'
                self.prompt = '> '
            else:
                self.show_output('Query : ', txt)
                result = self.cmd_query(txt)
        else:   
            if txt in self.all_commands['exit'][0]:
                self.cmd_exit()
                
            elif txt in self.all_commands['help'][0]:
                self.cmd_help()
                
            elif txt in self.all_commands['cmd'][0]:
                result = 'Returning to Command mode'
                mode = 'COMMAND'
                self.prompt = '> '
                
            elif txt in self.all_commands['add'][0]:
                result = 'Entering Add mode'
                mode = 'ADD'
                self.prompt = 'ADD > '
            
            elif txt in self.all_commands['query'][0]:
                result = 'Entering Query mode'
                mode = 'QUERY'
                self.prompt = '?? > '
            else:
                result = 'Unknown command - type help for list of commands'

        return result, mode
        
    #####################################################
    #  COMMAND PROCESSING FUNCTIONS
    #####################################################  
      
    def welcome(self):
        self.show_output('Welcome to the AIKIF Command Line Interface')
        
    def cmd_exit(self):
        self.show_output('Bye')
        exit(0)
        

    def cmd_help(self):
        txt = '\n'
        for k,v in self.all_commands.items():
            txt += k.ljust(6) + '= ' 
            txt += v[1].ljust(25)
            for cmd in v[0]:
                txt += cmd + ', '
            txt += '\n'
        self.show_output(txt)


    def cmd_add(self, txt):
        """
        Enter add mode - all text entered now will be 
        processed as adding information until cancelled
        """
        self.show_output('Adding ', txt)
        self.raw.add(txt)
        print(self.raw)
        return 'Added ' + txt
        

    def cmd_query(self, txt):
        """
        search and query the AIKIF
        """
        self.show_output('Searching for ', txt)
        res = self.raw.find(txt)
        for d in res:
            self.show_output(d)
        return str(len(res)) + ' results for ' + txt
    
if __name__ == '__main__':        
    cli = AICLI('test')

                
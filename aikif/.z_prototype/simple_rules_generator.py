# simple_rules_generator.py

"""
testing if simple semi english rule base commands can be used
to generate ontology rules.    
Predefined Rules
----------------
[files] use toolbox.file_tools
[photos] use toolbox.image_tools
[emails] use rawdata.gather.

General Rules
-------------
[files] live in T:\\user
[photos] live in P:\\

Specific Rules
--------------
copy photos to Gdrive\backup
copy files to Dropbox

Tasks
-----
Backup [files] daily to U:

"""

predefined_rules = [
    {'name':'backup', 'toolbox':'aikif.toolbox.file_tools'},
    {'name':'email', 'toolbox':'rawdata.gather.email'},
]

general_rules = [
    {'name':'files',  'folder':'T:\\user'},
    {'name':'photos', 'folder':'P:\\'},
]    

aliases = {
    'email':'email',
    'emails':'email',
    'mail':'email',
    'download':'download',
    'get':'download',
    'backup':'backup',
    'copy':'backup',
    'save':'backup',
}    


required_parameters = [
    {'process':'backup', 'params':['source', 'dest', 'schedule']},
    {'process':'download', 'params':['source', 'dest', 'type']},
]

   
def main():
    """
    Results = 
{'cmd': 'backup', 'toolbox': 'aikif.toolbox.file_tools', 'ask': 'copy files each day to dropbox'}
{'cmd': 'email',  'toolbox': 'rawdata.gather.email',     'ask': 'save emails to U:'}
{'cmd': 'email',  'toolbox': 'rawdata.gather.email',     'ask': 'get emails each day'}    
    """

    print((generate_rules('copy files each day to dropbox')))
    print((generate_rules('save emails to U:')))
    print((generate_rules('get emails each day')))

     
    
def generate_rules(txt):
    """
    takes a sentence and uses rules to determine intent
    and task generated.
    In case of duplicate / conflicting results it will 
    ask user to choose (or for now, return error message)
    
    """
    
    # Step 1 - get the list of words (not at all NLP but ok if we write it)
    res = {}
    res['ask'] = txt
    words = txt.split(' ')
    
    # Step 2 - find commands in phrase 
    found = []
    for word in words:
        for k,v in list(aliases.items()):
            if word == k:
                found.append(v)
                res['cmd'] = v
    
    # Step 3 - get the toolboxes that will be used for this
    for rule in predefined_rules:
        if rule['name'] in found:
            res['toolbox'] = rule['toolbox']
            
    # Step 4 - for the command, ensure required parameters are passed.
    #print('res = ', res)
    for param in required_parameters:
        #print('    param = ', param)
        if param['process'] == res['cmd']:
            print((' you need to check for these params :' , param['params']))
            #for num, p in enumerate(param['params']):
            #    res['param' + str(num+)] = p # param['params']
            res['params'] = param['params']    
    return res


if __name__ == '__main__':
    main()

        
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

   
def main():
    print(generate_rules('copy files each day to dropbox'))
    print(generate_rules('save emails to U:'))
    print(generate_rules('get emails each day'))

     
    
def generate_rules(txt):
    """
    takes a sentence and uses rules to determine intent
    and task generated.
    In case of duplicate / conflicting results it will 
    ask user to choose (or for now, return error message)
    
    """
    res = {}
    res['ask'] = txt
    words = txt.split(' ')
    
    found = []
    for word in words:
        for k,v in aliases.items():
            if word == k:
                found.append(v)
                res['cmd'] = v
    
    for rule in predefined_rules:
        if rule['name'] in found:
            res['toolbox'] = rule['toolbox']
    return res


if __name__ == '__main__':
    main()

        
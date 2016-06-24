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

aliases = []    
for k,v in predefined_rules:
    aliases.append(v)

print('aliases = ', aliases)    
    
def main():
    backup1 = generate_rules('Backup files each day to dropbox')

def generate_rules(txt):
    """
    takes a sentence and uses rules to determine intent
    and task generated.
    In case of duplicate / conflicting results it will 
    ask user to choose (or for now, return error message)
    
    """
    res = ''
    words = txt.split(' ')
    for word in words:
        if word in aliases:
            print('found ', word)
    
    return res


if __name__ == '__main__':
    main()

        
# program.py	written by Duncan Murray 18/4/2014
# part of AIKIF
# standard set of programs used for each interface in ccd
# each having the same functions (at this stage for proof
# of concept) which allow you to call things as a normal
# command

import os
import cls_log as mod_log
import config as mod_cfg
import cls_file_mapping as mod_filemap 
import aikif.lib.cls_file as mod_file

def TEST():
    """
    local test function - see \tests\test_programs.py for full coverage
    """
    prg = Programs()
    print(prg)

class Programs(object):
    """
    Class to manage a list of programs for AIKIF
    """
    def __init__(self, name=None, fldr=None, lst=None):
        self.name = name
        self.fldr = fldr
        if lst is None:
            self.lstPrograms = [] 
        else:
            self.lstPrograms = lst 
        self.log_folder = mod_cfg.fldrs['log_folder']    
        self.lg = mod_log.Log(self.log_folder)
        self.lg.record_command('program', 'generating program list in - ' + self.log_folder)
     
    def __str__(self):
        """
        return a summary of programs
        """
        return 'list of programs in AIKIF'
        
        
    def add(self, nme, desc):
        """
        Adds a program to the list, logs the reference and TODO - adds core link to processes
        """
        self.lstPrograms.append(nme)
        #aikif.LogProcess(desc, nme)
        self.lg.record_process('program - generating program list in - ' + self.log_folder)

        
    def list(self):
        """
        Display the list of items 
        """
        for i in self.lstPrograms:
            print (i)
        return self.lstPrograms
        
    def save(self, fname=''):
        """
        Save the list of items to AIKIF core and optionally to local file fname
        """
        if fname != '':
            with open(fname, 'w') as f:
                f.write('\n'.join([i for i in self.lstPrograms]))

        
        # save to standard AIKIF structure
        filemap = mod_filemap.FileMap(mod_filemap.dataPath)
        location_fileList = filemap.get_full_filename(filemap.find_type('LOCATION'), filemap.find_ontology('FILE-PROGRAM')[0])   	
        object_fileList = filemap.get_full_filename(filemap.find_type('OBJECT'), filemap.find_ontology('FILE-PROGRAM')[0])   	

        self.lstPrograms.sort()
        
        with open(object_fileList, 'a') as f:
            f.write('\n'.join([i for i in self.lstPrograms]))
        
        uniqueFolders = set([os.path.dirname(i) for i in self.lstPrograms])
        sortSet = sorted(uniqueFolders)
        #print(sortSet)
        with open(location_fileList, 'a') as f:
            for i in sorted(uniqueFolders):
                f.write(i + '\n')

    def collect_program_info(self, fname):
        """
        gets details on the program, size, date, list of functions
        and produces a Markdown file for documentation
        """
        md = '#AIKIF Technical details\n'
        for i in self.lstPrograms:
            f = mod_file.File(i)
            md += f.name + ' | ' + str(f.size) + ' | \n'
        
        
        # save the details an Markdown file 
        with open(fname, 'w') as f:
            f.write(md)
 
if __name__ == '__main__': 
    TEST()
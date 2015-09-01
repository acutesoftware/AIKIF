# program.py	written by Duncan Murray 18/4/2014
# part of AIKIF
# standard set of programs used for each interface in ccd
# each having the same functions (at this stage for proof
# of concept) which allow you to call things as a normal
# command

import os
import aikif.cls_log as mod_log
import aikif.config as mod_cfg
import aikif.cls_file_mapping as mod_filemap 
import aikif.lib.cls_filelist as mod_fl
import aikif.lib.cls_file as mod_file

root_folder = os.path.abspath(mod_cfg.fldrs['root_path'] + os.sep  ) 


class Programs(object):
    """
    Class to manage a list of programs for AIKIF
    """
    def __init__(self, name, fldr):
        self.name = name
        self.fldr = fldr
        self.lstPrograms = [] 
        self.log_folder = mod_cfg.fldrs['log_folder']    
        self.lg = mod_log.Log(self.log_folder)
        self.lg.record_command('program', 'generating program list in - ' + self.log_folder)
        self.list_all_python_programs()
        
    def __str__(self):
        """
        return a summary of programs
        """
        return 'list of programs in AIKIF'
        
    
    def list_all_python_programs(self):
        """
        collects a filelist of all .py programs
        """
        self.tot_lines = 0
        self.tot_bytes = 0
        self.tot_files = 0
        self.tot_loc = 0
        self.lstPrograms = []
        fl = mod_fl.FileList([self.fldr], ['*.py'], ["__pycache__", ".git"])
        for f in fl.get_list():
            if '__init__.py' not in f:
                self.add(f, 'TODO - add comment')
                f = mod_file.TextFile(f)
                self.tot_lines += f.count_lines_in_file()
                self.tot_loc += f.count_lines_of_code()
                self.tot_bytes += f.size
                self.tot_files += 1
 
        print('All Python Program Statistics')
        print('Files = ', self.tot_files, ' Bytes = ', self.tot_bytes, ' Lines = ', self.tot_lines, ' Lines of Code = ', self.tot_loc)
            
         
    def add(self, nme, desc):
        """
        Adds a program to the list, with default desc
        """
        self.lstPrograms.append([nme,desc])
        #self.lg.record_process('program - generating program list in - ' + self.log_folder)

    def comment(self, nme, desc):
        """
        Adds a comment to the existing program in the list, 
        logs the reference and TODO - adds core link to processes
        """
        
        if nme != '':
            program_exists = False
            for i in self.lstPrograms:
                print(i)
                if nme in i[0]:
                    i[1] = desc
                    program_exists = True
            
            if program_exists is False: # not there?
                self.lstPrograms.append([nme,desc + ' - <I>FILE DOESNT EXIST</I>'])
            
            self.lg.record_process('adding description to - ' + nme)


        
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
                for i in self.lstPrograms:
                    f.write(self.get_file_info_line(i, ','))

        
        # save to standard AIKIF structure
        
        filemap = mod_filemap.FileMap([], [], mod_filemap.dataPath)
        #location_fileList = filemap.get_full_filename(filemap.find_type('LOCATION'), filemap.find_ontology('FILE-PROGRAM')[0])   	
        object_fileList = filemap.get_full_filename(filemap.find_type('OBJECT'), filemap.find_ontology('FILE-PROGRAM')[0])   	
        print('object_fileList = ' + object_fileList + '\n')
        try:
            os.remove(object_fileList)
        except Exception:
            pass
        self.lstPrograms.sort()

        try:
            with open(object_fileList, 'a') as f:
                f.write('\n'.join([i[0] for i in self.lstPrograms]))
        except Exception:
            print('ERROR = cant write to object_filelist ' , object_fileList)

    def get_file_info_line(self, fname, delim):
        """
        gathers info on a python program in list and formats as string
        """
        txt = ''
        f = mod_file.File(fname[0])
        txt += '"' + f.fullname + '"' + delim 
        txt += '"' + f.name + '"' + delim 
        txt += '"' + f.path + '"' + delim
        txt += '"' + f.GetDateAsString(f.date_modified)[2:10] + '"' + delim
        txt += '"' + str(f.size) + '"' + delim
        return txt  + '\n'
     
    def get_file_info_web(self, fname, delim):
        """
        gathers info on a python program in list and formats as string
        """
        txt = ''
        f = mod_file.File(fname[0])
        txt += '<sup>' + f.name + '</sup>'  + delim 
        txt += '<sup>' + fname[1] + '</sup>' + delim
        txt += '<sub><sup><span white-space:nowrap;>' + f.GetDateAsString(f.date_modified)[2:10] + '</span></sup></sub>' + delim
        txt += '<sup><sup>' + str(f.size) + '</sup></sup>' + delim
        return txt  + '\n'
     
        
    def collect_program_info(self, fname):
        """
        gets details on the program, size, date, list of functions
        and produces a Markdown file for documentation
        """
        md = '#AIKIF Technical details\n'
        md += 'Autogenerated list of programs with comments and progress\n'
        md += '\nFilename | Comment | Date | Size\n'
        md += '--- | --- | --- | ---\n'
        for i in self.lstPrograms:
            md += self.get_file_info_line(i, ' | ')
        
        # save the details an Markdown file 
        with open(fname, 'w') as f:
            f.write(md)
 

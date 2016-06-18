#!/usr/bin/python3
# coding: utf-8
# cls_file.py
# Other modules that inherit from this class:
#   toolbox.xml_tools.XmlFile  (in progress)
#   toolbox.image_tools.ImageFile  (TODO)

import os
import sys
import codecs
from datetime import datetime

#img_file = ImageFile('..\\..\\doc\\web-if-v02.jpg')
#print(img_file)

#aud_file = AudioFile(r"E:\backup\music\Music\_Rock\Angels\Red Back Fever\07 Red Back Fever.mp3")
#print(aud_file)
        
class File(object):
    """
    handles various file conversions, reading, writing 
    as well as  general file operations (delete, copy, launch)
    """
    
    def __init__(self, fname):
        self.fullname = os.path.abspath(fname)
        self.name = fname
        self.path = ''
        self.size = 0
        self.date_modified = None  # self.GetDateAsString(os.path.getmtime(fname))
        try:
            self.fullname = os.path.abspath(fname)
            self.name = os.path.basename(self.fullname)
            self.path = os.path.dirname(self.fullname)
            self.size = os.path.getsize(self.fullname)
            self.date_modified = os.path.getmtime(self.fullname)  # self.GetDateAsString(os.path.getmtime(fname))
        except Exception as ex:     
            print('problem accessing ' + fname + ' ' + str(ex))

    def __str__(self):
        # when printing a file class it should print the name, size, date
        # as well as top 10 lines (first 80 chars in each line)
        txt =  '=============================================\n'
        txt += '| name     = ' + self.name + '\n'
        txt += '| size     = ' + str(self.size) + ' bytes\n'
        txt += '| folder   = ' + self.path + '\n'
        txt += '| modified = ' + self.GetDateAsString(self.date_modified) + '\n'
        txt += '=============================================\n'
        
        return txt
        
    def exists(self):
        if os.path.exists(self.fullname):
            return True
        return False
        
    def launch(self):
        """ launch a file - used for starting html pages """
        #os.system(self.fullname) # gives permission denied seeing it needs to be chmod +x
        import subprocess
        try:
            retcode = subprocess.call(self.fullname, shell=True)
            if retcode < 0:
                print("Child was terminated by signal", -retcode, file=sys.stderr)
                return False
            else:
                print("Child returned", retcode, file=sys.stderr)
                return True
        except OSError as e:
            print("Execution failed:", e, file=sys.stderr)
            return False
        
        
        
 
    def delete(self):
        """ delete a file, don't really care if it doesn't exist """
        if self.fullname != "":
            try:
                os.remove(self.fullname)
            except IOError:
                print("Cant delete ",self.fullname)

    def GetDateAsString(self, t):
        res = ''
        try:
            res = str(datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S"))
        except Exception as ex:     
            print('problem converting time ' + str(t) + ' ' + str(ex))
        return res    
        
class TextFile(File):
    """
    handles various file conversions, reading, writing 
    as well as  general file operations (delete, copy, launch)
    """
    
    def __init__(self, fname):
        super(TextFile, self).__init__(fname)
        self.lines = self.count_lines_in_file(fname)

    def __str__(self):
        """ display the text file sample """
        txt = super(TextFile, self).__str__()
        txt += 'TextFile contains ' + str(self.lines) + ' lines\n'
        txt += self.get_file_sample()
        return txt
        
    def count_lines_in_file(self, fname=''):
        """ you wont believe what this method does """
        i = 0
        if fname == '':
            fname = self.fullname
        try:
            #with open(fname, encoding="utf8") as f:
            with codecs.open(fname, "r",encoding='utf8', errors='ignore') as f:    
                for i, _ in enumerate(f):
                    pass
            return i + 1    
        except Exception as ex:
            print('cant count lines in file in "', fname, '":', str(ex))
            return 0
    
    def count_lines_of_code(self, fname=''):
        """ counts non blank lines """
        if fname == '':
            fname = self.fullname
        loc = 0    
        try:
            with open(fname) as f:
                for l in f:
                    if l.strip() != '':
                        loc += 1
            return loc    
        except Exception as ex:
            print('cant count lines of code in "', fname, '":', str(ex))
            return 0
    
    
    def get_file_sample(self, numLines=10):
        """ retrieve a sample of the file """
        res = ''
        try:
            with open(self.fullname, 'r') as f:
                for line_num, line in enumerate(f):
                    res += str(line_num).zfill(5) + ' ' + line 
                    if line_num >= numLines-1:
                        break
            return res
        except Exception as ex:
            print('cant get_file_sample in "', self.fullname, '":', str(ex))
            return res
        
    
    def append_text(self, txt):
        """ adds a line of text to a file """
        with open(self.fullname, "a") as myfile:
            myfile.write(txt)

            
    def convert_to_csv(self, op_csv_file, delim):
        # function to simply convert the diary files to csv - testing
        import csv
        in_txt = csv.reader(open(self.fullname, "r"), delimiter = delim)
        ofile  = open(op_csv_file, 'w', newline='')
        out_csv = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        if in_txt != "":
            out_csv.writerows(in_txt)
        ofile.close()
        #in_txt.close()

    def load_file_to_string(self):
        """ load a file to a string """
        try:
            with open(self.fullname, 'r') as f:
                txt = f.read()
            return txt
        except IOError:
            return ''
        
    def load_file_to_list(self):
        """ load a file to a list """
        lst = []
        try:
            with open(self.fullname, 'r') as f:
                for line in f:
                    lst.append(line) 
            return lst  
        except IOError:
            return lst
        
class ImageFile(File):
    """
    handles various image file metadata collection
    (by calling toolbox/image_tools.py)
    """
    
    def __init__(self, fname):
        import aikif.toolbox.image_tools as img
        super(ImageFile, self).__init__(fname)
        self.meta = img.get_metadata_as_dict(fname)
        
    def __str__(self):
        """ display the text file sample """
        #txt = self.name + '\n'
        txt = super(ImageFile, self).__str__()
        txt += 'Image size =  ' + str(self.meta['width']) + ' x ' + str(self.meta['height']) + '\n'
        return txt
        
class AudioFile(File):
    """
    handles various audio file metadata collection
    (by calling toolbox/audio_tools.py)
    """
    
    def __init__(self, fname):
        import aikif.toolbox.audio_tools as aud
        super(AudioFile, self).__init__(fname)
        self.meta = aud.get_audio_metadata(fname)
        #print(self.meta)
        
    def __str__(self):
        """ display the meta data from the audio file """
        txt = super(AudioFile, self).__str__()
        txt += 'Song = ' + str(self.meta['title'][0]) + ' by ' + str(self.meta['artist'][0]) + '\n'
        return txt
        
        

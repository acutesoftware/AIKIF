# cls_file.py

import os
import sys
import time
from datetime import datetime
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "..") 
sys.path.append(root_folder)

def TEST():
    """ test routines during development - will be part of unittest 
    Call from command line:
        python cls_file.py cls_filelist.py
    """
    print(sys.argv)
    if len(sys.argv) > 1:
        user_file = TextFile(sys.argv[1])
        print(user_file)
    else:
        txt_file = TextFile('cls_file.py')
        print(txt_file)
        
        img_file = ImageFile('..\\..\\doc\\web-if-progs-v01.jpg')
        print(img_file)

        aud_file = AudioFile(r"E:\backup\music\Music\_Rock\Angels\Red Back Fever\07 Red Back Fever.mp3")
        print(aud_file)
        
class File(object):
    """
    handles various file conversions, reading, writing 
    as well as	general file operations (delete, copy, launch)
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
        except:
            pass

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
        
    def launch(self, params=''):
        """ launch a file using os.system() - used for starting html pages """
        os.system("start " + self.fullname)    

    def delete(self):
        """ delete a file, don't really care if it doesn't exist """
        if self.fullname == "":
            pass
        else:
            try:
                os.remove(self.fullname)
            except:
                print("Cant delete ",self.fullname)

    def GetDateAsString(self, t):
        res = ''
        try:
            res = str(datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S"))
        except:
            pass
        return res    
        
class TextFile(File):
    """
    handles various file conversions, reading, writing 
    as well as	general file operations (delete, copy, launch)
    """
    
    def __init__(self, fname):
        super().__init__(fname)
        self.lines = self.count_lines_in_file(fname)

    def __str__(self):
        """ display the text file sample """
        txt = super().__str__()
        txt += 'TextFile contains ' + str(self.lines) + ' lines\n'
        txt += self.get_file_sample()
        return txt
        
    def count_lines_in_file(self, fname):
        """ you wont believe what this method does """
        try:
            with open(fname) as f:
                for i, l in enumerate(f):
                    pass
            return i + 1    
        except:
            return 0
    
    def get_file_sample(self, numLines=10):
        """ retrieve a sample of the file """
        res = ''
        try:
            with open(self.fullname, 'r') as f:
                for line_num, line in enumerate(f):
                    res += str(line_num).zfill(5) + ' ' + line 
                    if line_num > numLines:
                        break
        except:
            pass
        return res
        
    
    def append_text(self, txt):
        """ adds a line of text to a file """
        with open(self.fullname, "a") as myfile:
            myfile.write(txt)

    def convert_to_csv(self, op_csv_file, delim):
        """ function to simply convert the diary files to csv - testing """
        in_txt = csv.reader(open(self.fullname, "r"), delimiter = delim)
        ofile  = open(op_csv_file, 'w', newline='')
        out_csv = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        if in_txt != "":
            out_csv.writerows(in_txt)


    def load_file_to_string(self):
        """ load a file to a string """
        try:
            with open(self.fullname, 'r') as f:
                txt = f.read()
            return txt
        except:
            return ''
        
    def load_file_to_list(self):
        """ load a file to a list """
        lst = []
        try:
            with open(self.fullname, 'r') as f:
                for line in f:
                    lst.append(line) 
            return lst	
        except:
            return lst
        
class ImageFile(File):
    """
    handles various image file metadata collection
    (by calling toolbox/image_tools.py)
    """
    
    def __init__(self, fname):
        import AI.toolbox.image_tools as img
        super().__init__(fname)
        self.meta = img.get_metadata_as_dict(fname)
        
    def __str__(self):
        """ display the text file sample """
        #txt = self.name + '\n'
        txt = super().__str__()
        txt += 'Image size =  ' + str(self.meta['width']) + ' x ' + str(self.meta['height']) + '\n'
        return txt
        
class AudioFile(File):
    """
    handles various audio file metadata collection
    (by calling toolbox/audio_tools.py)
    """
    
    def __init__(self, fname):
        import AI.toolbox.audio_tools as aud
        super().__init__(fname)
        self.meta = aud.get_audio_metadata(fname)
        print(self.meta)
        
    def __str__(self):
        """ display the meta data from the audio file """
        txt = super().__str__()
        txt += 'Song = ' + str(self.meta['title'][0]) + ' by ' + str(self.meta['artist'][0]) + '\n'
        return txt
        
        
if __name__ == "__main__":
    TEST()
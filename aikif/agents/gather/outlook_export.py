# -*- coding: utf-8 -*-
# outlook_export.py   written by Duncan Murray 15/1/2015
import sys
import codecs
import win32com

def TEST():
    print('Testing Outlook - ', sys.version)
    #op_file = 'D:\\py\\emails\\outlook_emails.csv' 
    op_file = 'E:\\backup\\MAIL\\outlook_emails.csv'
    
    
    with open(op_file, 'w', encoding='utf-8', errors="surrogateescape") as f:
        export_all_emails(f)



def get_mails(folder, path = ''):
    for mail in folder.Items:
        yield mail, path
    for subfolder in folder.Folders:
        for mail, subpath in get_mails(subfolder, path + [subfolder]):
            yield mail, subpath

def export_all_emails(f):
    """
    Walks through all stores and folders in Outlook and extracts 
    emails to a CSV file
    """
    outlook = win32com.client.Dispatch('Outlook.Application')
    mapi = outlook.GetNamespace('MAPI')
    tot_folders = 0
    tot_emails = 0
    num_emails = 0
    old_path = ''
    for store in mapi.Stores:
        if not store.IsDataFileStore: continue
        tot_stores += 1
        print (store)
        for mail, path_list in get_mails(store.GetRootFolder()):
            path_str = str(store) + '/' + '/'.join([p.Name for p in path_list])
            if path_str != old_path:
                old_path = path_str
                print(path_str + ' (' + str(num_emails) + ' emails)')
                tot_folders += 1
                num_emails = 0
            tot_emails += 1
            num_emails += 1
            #print (mail.size, path_str, mail.subject.encode('utf8'))
            m = Message(mail, path_str)
            try:
                f.write(m.convert_csv())
            except IOError:
                print('ERROR writing email #' + str(tot_emails) + ' in ' + path_str)
        
    print('Found ' , tot_emails , ' emails in ', tot_folders, ' folders')

class Message(object):
    def __init__(self, msg, path):
        self.msg = msg
        self.path = path
         
    def __str__(self):
        return self.convert_csv()
        
    def convert_csv(self):
        delim = '","'
        txt = '"' + self.path + delim
        txt += str(self.msg.size) + delim
        
        
        try:
            txt += str(self.msg.ReceivedTime) + delim
        except UnicodeError:
            txt += delim

        try:
            txt += str(self.msg.SenderEmailAddress) + delim
        except UnicodeError:
            txt += delim

        try:
            txt += self.msg.SenderName + delim
        except UnicodeError:
            txt += delim
            
        try:
            txt += self.msg.To + delim
        except UnicodeError:
            txt += delim
        
        txt += self.msg.Categories + delim
        
        try:
            txt += self.msg.Subject.decode("utf-8") + delim  # encode('utf8')
        except UnicodeError:
            try:
                txt += str(self.msg.Subject) + delim
            except UnicodeError:
                txt += delim
        try:
            for attach in self.msg.Attachments:
                #print(attach.FileName )
                if attach:
                    txt += attach.FileName + '; '
                    attach.SaveASFile('E:\\backup\\MAIL\\_EXPORTED\\' + attach.FileName)
            txt += delim   
        except UnicodeError:
            txt += delim   
        """
        TODO - save attachments
        attach.SaveASFile( C:\\folder\\' + attach.FileName)
        """
        

        return txt + '"\n'
 
if __name__ == '__main__':
    TEST()	

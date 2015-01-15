# -*- coding: utf-8 -*-
# outlook_export.py   written by Duncan Murray 15/1/2015
import os, sys
import codecs, win32com.client
import win32com

def TEST():
    print('Testing Outlook - ', sys.version)
    with open('E:\\backup\\MAIL\\outlook_emails.csv', 'w') as f:
        export_all_emails(f)



def get_mails(folder, path=[]):
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
    tot_stores = 0
    tot_folders = 0
    tot_emails = 0
    num_emails = 0
    old_path = ''
    for store in mapi.Stores:
        if not store.IsDataFileStore: continue
        tot_stores += 1
        print (store)
        for mail, path_list in get_mails(store.GetRootFolder()):
            path_str = '/'.join([p.Name for p in path_list])
            if path_str != old_path:
                old_path = path_str
                print(path_str + ' (' + str(num_emails) + ' emails)')
                tot_folders += 1
                num_emails = 0
            tot_emails += 1
            num_emails += 1
            #print (mail.size, path_str, mail.subject.encode('utf8'))
            m = Message(mail, path_str)
            f.write(m.convert_csv())
            
    print('Found ' , tot_emails , ' emails in ', tot_folders, ' folders')

class Message:
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
        except:
            txt += delim

        try:
            txt += str(self.msg.SenderEmailAddress) + delim
        except:
            txt += delim

        try:
            txt += self.msg.SenderName + delim
        except:
            txt += delim
            
        try:
            txt += self.msg.To + delim
        except:
            txt += delim
        
        txt += self.msg.Categories + delim
        
        try:
            txt += self.msg.Subject.decode("utf-8") + delim  # encode('utf8')
        except:
            try:
                txt += str(self.msg.Subject) + delim
            except:
                txt += delim
        try:
            for attach in self.msg.Attachments:
                #print(attach.FileName )
                if attach:
                    txt += attach.FileName + '; '
            txt += delim   
        except:
            txt += delim   
        """
        TODO - save attachments
        attach.SaveASFile( C:\\folder\\' + attach.FileName)
        """
        
        try:
           # txt += self.msg.Body.strip('\n').encode("utf-8") + delim
            txt += self.msg.Body.strip('\n')[0:55] + delim
           # txt += body + delim
        except:
            txt += delim
                
                
                
        #print(txt.encode('utf8')  )  
        return txt + '"\n'
    
    
if __name__ == '__main__':
    TEST()	

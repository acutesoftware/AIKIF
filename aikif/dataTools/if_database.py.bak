# cls_database.py		written by Duncan Murray 28/4/2014
# 



class Database(object):
    """
    Base class to handle database functions
    cred = [server, database, username, password]
    """
    def __init__(self, cred, name=None):
        self.name = name
        self.server = cred[0]
        self.database = cred[1]
        self.username = cred[2]
        self.password = cred[3]
        self.connection = None
    def save(self):
        print('saving')
        
    def getData(self, sqlText):
        lst = []
        print('extracting data - ', sqlText)
        return lst
        
    def get_info(self):
        return '\nserver='+self.server + '\ndatabase=' + self.database + '\nusername='+ self.username + '\npassword=' + self.password
        
    def connect(self):
        print(self.get_info())
        
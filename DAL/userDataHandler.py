from TrueDate.DAL.baseDataHandler import *

class userDataHandler(baseDataHandler):
    '''Data handler class for users.
    static, singletone.
    handles all data of users and persons'''

    def appendRowToFile(object):
        print ("user appended to a file")
        return super(userDataHandler).appendRowToFile()




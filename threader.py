from threading import Thread
from dbManager import DBManager
import time
import pickle


class myThread(Thread):
    def __init__(self, cli):
        Thread.__init__(self)
        self.cli = cli
        self.db = DBManager()


    def run(self):
        user = self.cli.recv(1024)
        data = pickle.loads(user)

        if data[0] == "add":
            self.db.addUser(data[1], data[2], data[3], data[4], data[5])
            msg = "USER has beed added to DATABASE successfully..."
            msgOkay = pickle.dumps(msg)
            self.cli.send(msgOkay)
        
        if data[0] == "validate":
            result = self.db.validateUser(data[1], data[2])
            if result == "False":
                errorMsg = "Invalid user"
            else:
                errorMsg = "Valid user"
            
            msgOkay = pickle.dumps(errorMsg)
            self.cli.send(msgOkay)

        if data[0] == "display":
            data = self.db.display()
            data = pickle.dumps(data)
            self.cli.send(data)

        if data[0] == "auth":
            res = self.db.authorize(data[1], data[2], data[3])
            data = pickle.dumps(res)
            self.cli.send(data)   

            



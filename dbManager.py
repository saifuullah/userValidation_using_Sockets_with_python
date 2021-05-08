import psycopg2 as p

class DBManager():

    def __init__(self):
        self.conn = p.connect(
            host = "localhost",
            database = "USER",
            user = "admin",
            password = "admin")
    
    def addUser(self, uname, upass, r1, r2, r3):
        cur = self.conn.cursor()
        cur.execute("insert into users (username, password, accessR1, accessR2, accessR3) values     (%s, %s, %s, %s, %s)", (uname, upass, r1, r2, r3) )

        print("New user has been added to the DATABASE.....")
        
        # Commit chnages
        self.conn.commit()
        self.conn.close()        

    def validateUser(self, uname, upass):
        
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()

        for user in users:
            if user[1] == uname and user[2] == upass:
                return "True"
        return "False"

    def display(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        return users




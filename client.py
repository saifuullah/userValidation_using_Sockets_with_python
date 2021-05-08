import socket
import pickle
import time


ADDRESS = '127.0.0.1'
PORT = 5551

cli = socket.socket()
cli.connect((ADDRESS,PORT))

print("Connected with the server on IP : ", str(ADDRESS) + " PORT " + str(PORT) )

n=0
while(n==0):
    n+=1
    print("\n1. For create user....")
    print("2. For Validate user....")
    print("3. For Authenticate user....")
    print("4. For Display all users.....")

    choice = int(input("Choice :  ") )

    if choice == 1:
        dataList = []
        uname = input("Enter username : ")
        upass = input("Enter password : ")
        r1 = input("Please confirm, this user can access Resource 1 ?? (yes or no)")
        r2 = input("Please confirm, this user can access Resource 2 ?? (yes or no)")
        r3 = input("Please confirm, this user can access Resource 3 ?? (yes or no)")
        
        r1, r2, r3 = r1.lower(), r2.lower(), r3.lower()
        flag = "add"
        dataList.append(flag)
        dataList.append(uname)
        dataList.append(upass)
        dataList.append(r1)
        dataList.append(r2)
        dataList.append(r3)
        
        print("Sending data to the server.....")
        
        time.sleep(1)
        buff = pickle.dumps(dataList)
        cli.send(buff)
        
        print("Data has been successfully sent to the server...")
        time.sleep(1)
        messg = cli.recv(1024)
        decodeMsg = pickle.loads(messg)
        print(decodeMsg)
        print("\n \n")

        
    elif choice == 2:
        uname = input("Enter username : ")
        upass = input("Enter password : ")
        dataList = []
        flag = "validate"
        dataList.append(flag)
        dataList.append(uname)
        dataList.append(upass)

        print("Sending data to the server for validation.....")
        buff = pickle.dumps(dataList)
        cli.send(buff)
        print("Data has been successfully sent to the server...Please wait for results")
        time.sleep(2)
        messg = cli.recv(1024)
        decodeMsg = pickle.loads(messg)
        print(decodeMsg)

    elif choice == 4:
        flag = "display"
        dataList = []
        dataList.append(flag)
        buff = pickle.dumps(dataList)
        cli.send(buff)
        print("Fetching users data from DATABASE......")
        time.sleep(2)
        user = cli.recv(1024)
        data = pickle.loads(user)

        for user in data:
            print("Name : " + user[1] + "\n" + "Pass : " + user[2] + "\n" + "Access R1 : " + user[3] + "\n" + "Access R2 : " + user[4] + "\n" + "Access R3 : " + user[5])
            print("\n")












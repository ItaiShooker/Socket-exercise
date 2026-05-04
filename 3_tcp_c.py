# import the socket package
import socket

# define s as the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# define the dest as me
dest_ip = '127.0.0.1'
# define the port
dest_port = 12345
# connect the src and the dest
s.connect((dest_ip, dest_port))
# get an input
msg = input("Message to send: ")
# get an input until the input is quit
while not msg == 'quit':
    # Convert it to bytes
    s.send(bytes(msg, 'utf-8'))
    # define data as the return fron the server
    data = s.recv(4096)
    # Convert to string and print it
    print("Server sent: ", data.decode('utf-8'))
    msg = input("Message to send: ")

# close the socket
s.close()
# import the socket package
import socket

# define server as a socket by tcp 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get every client
server_ip = ''
# define the port
server_port = 12345
# connect between src and dest
server.bind((server_ip, server_port))
# wait only for 5 details
server.listen(5)

# infinity loop
while True:
    # get the client details 
    client_socket, client_address = server.accept()
    print('Connection from: ', client_address)
    # define data as the client msg
    data = client_socket.recv(1024)
    # while the msg is not finish
    while not data.decode('utf-8') == '':
        # print the string
        print('Received: ', data.decode('utf-8'))
        # Convert to upper case
        client_socket.send(data.lower())
        # get the next
        data = client_socket.recv(1024)


    print('Client disconnected')
    # close the socket
    client_socket.close()

     # I made a chenge and now it returns a lower case
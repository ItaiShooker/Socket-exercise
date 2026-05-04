# Import the socket pakage
from socket import socket, AF_INET, SOCK_DGRAM

# define s as a socket
s = socket(AF_INET, SOCK_DGRAM)

# Empty IP address to listen every IP
src_ip = ''
# The port of the server
src_port = 12345
# define s as the server and connect it to the port and the client
s.bind((src_ip, src_port))

# Infinity loop
while True:
    # Save the data and the IP of the client from what we get
    data, sender_info = s.recvfrom(2048)
    # Convert to string
    print(data.decode('utf-8'))
    # Print the client details
    print(sender_info)

    # Make the string capital letters and send it back
    s.sendto(data.lower(), sender_info)

    # I made a chenge and now it returns a lower case
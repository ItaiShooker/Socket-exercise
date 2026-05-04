# Import the socket package
from socket import socket, AF_INET, SOCK_DGRAM

# define s as a socket
s = socket(AF_INET, SOCK_DGRAM)

# define the IP as "me"
dst_ip = '127.0.0.1'
# define the server IP
dst_port = 12345

# Send a request from me to the server
s.sendto(b'Hello', (dst_ip,dst_port))

# define the data and the details as what we get from the server 
data, sender_info = s.recvfrom(2048)
# Convert to string and print
print(data.decode('utf-8'))
# print the details
print(sender_info)

# close the socket
s.close()

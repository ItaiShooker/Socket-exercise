#include <iostream>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>

using namespace std;

int main() {
    // define the port
    const int server_port = 5555;
    // define sock as the socket, it returns an int
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        perror("error creating socket");
    }

    // struct to convert to machine language
    struct sockaddr_in sin;
    memset(&sin, 0, sizeof(sin));
    sin.sin_family = AF_INET;
    sin.sin_addr.s_addr = INADDR_ANY;
    sin.sin_port = htons(server_port);

    // connct it to the client
    if (bind(sock, (struct sockaddr *) &sin, sizeof(sin)) < 0) {
        perror("error binding socket");
    }
    // if there are more than 5 listeners in the line
    if (listen(sock, 5) < 0) {
        perror("error listening to a socket");
    }
    // struct to define the client
    struct sockaddr_in client_sin;
    unsigned int addr_len = sizeof(client_sin);
    int client_sock = accept(sock,  (struct sockaddr *) &client_sin,  &addr_len);

    if (client_sock < 0) {
        perror("error accepting client");
    }
    // read the data fron the client and print it
    char buffer[4096];
    int expected_data_len = sizeof(buffer);
    int read_bytes = recv(client_sock, buffer, expected_data_len, 0);
    if (read_bytes == 0) {
    // connection is closed
    }
    else if (read_bytes < 0) {
    // error
    }
    else {
        cout << buffer;
    }
    // sent the data back to the client
    string full_msg = "Server received: " + string(buffer, read_bytes);
    int sent_bytes = send(client_sock, full_msg.c_str(), full_msg.length(), 0);
    if (sent_bytes < 0) {
        perror("error sending to client");
    }

    close(client_sock);
    close(sock);


    return 0;
}

// I change the return of the server
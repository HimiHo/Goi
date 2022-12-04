import socket

HOST = "127.0.0.1"
PORT = 53210

def client_sock():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((HOST, PORT))
    client_sock.sendall(b'Hello, world')
    data = client_sock.recv(1024)
    client_sock.close()
    print('Received: ', repr(data))

import socket

s=socket.socket()

port=3115

s.connect(('127.0.0.1',port))
while True:

    z=input()

    s.sendall(z.encode())

    print("server-",s.recv(100))
    s.close()
import socket

s=socket.socket()
print ("socket  created")

port=3115

s.bind(('',port))
print( "socket binded to ",port)

s.listen(3)
print ("socket  listening")

while True:
    c,add=s.accept()
    print( "Got connection from ",add)


    print("client-",c.recv(100))
    x=input()
    c.sendall(x.encode())
    c.close()
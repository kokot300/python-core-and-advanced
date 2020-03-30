import socket

s=socket.socket()

s.connect(("localhost",6767))

iii="C:\\Users\\kokot\\PycharmProjects\\untitled\\python-core-and-advanced/python.html" #input("enter filename: \n")

s.send(iii.encode())
content=s.recv(1024)
print(content.decode())

'''
msg=s.recv(1024)

while msg:
    print("received: ",msg.decode())
    msg = s.recv(1024)
'''

s.close()
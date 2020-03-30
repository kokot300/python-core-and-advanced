import socket

host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET is using IP v4 #TCP IP SOCK_STEAM
s.bind((host, port))
print("listening from port ", port)
s.listen(1)
print("listening")
c,addr = s.accept()
print("connection from: ", str(addr))
c.send(b"hello")  # converts into binary
c.send("bye".encode())
print("message sent")
c.close()

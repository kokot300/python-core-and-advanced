import socket

host = 'localhost'
port = 6767

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET is using IP v4 #TCP IP SOCK_STEAM
    s.bind((host, port))
    print("listening from port ", port)
    s.listen(1)
    print("listening")
    c,addr = s.accept()
    print("connection from: ", str(addr))
    #c.send(b"hello")  # converts into binary
    #c.send("bye".encode())
    #print("message sent")

    fileName=c.recv(1024)
    print(fileName.decode())
    print("sending file")
    try:
        f=open(fileName.decode(),"rb")
        content=f.read()
        print(content)
        print("sending file")
        c.send(content)
        f.close()
    except FileNotFoundError:
        c.send(b"file does not exist!")

    c.close()
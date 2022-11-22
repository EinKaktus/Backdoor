import socket

host = "127.0.0.1"
port = 22

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(3)
connection, addr = s.accept()
print("Verbunden mit" + addr[0])
data = connection.recv(2024)
print(data)

while True:
    cmd = input("Befehl: ")
    connection.send(str.encode(cmd))
    data = connection.recv(2024)
    print(data.decode("utf-8"))

connection.close()

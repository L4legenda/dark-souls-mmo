import socket

soc = socket.socket()
soc.connect(("192.168.71.213", 4000))

soc.send(b"hello socket")
data = soc.recv(4096)
data_srt = data.decode("utf-8")
print(data_srt)

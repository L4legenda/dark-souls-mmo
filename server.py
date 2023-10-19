import socket

soc = socket.socket()
soc.bind(('192.168.71.213', 4000))
soc.listen(1)

while True:
    con, address = soc.accept()
    data = con.recv(4096)
    data_str = data.decode("utf-8")
    data_up = data_str.title()
    data = data_up.encode("utf-8")
    con.send(data)
    con.close()

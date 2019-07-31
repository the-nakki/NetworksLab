import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_host = socket.gethostname()
tcp_port = 1235

s.connect((tcp_host, tcp_port))

msg = s.recv(1024)
print(msg.decode("utf-8"))
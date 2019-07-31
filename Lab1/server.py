import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_host = socket.gethostname()
tcp_port = 1235
s.bind((tcp_host, tcp_port))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print("Connection from {} has been established.".format(address))
    clientsocket.send(bytes("Hey guys Bhai Vlogs coming at ya from the SERVERSIDE!!! Woohoo that's wassup y'all!!!"))
    clientsocket.close()
    print("Connection closed. Waiting for client...")

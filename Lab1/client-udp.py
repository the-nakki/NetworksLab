import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      

udp_host = socket.gethostname()		        
udp_port = 12345

msg = "Hello Python!"
print("UDP target IP: {}".format(udp_host))
print("UDP target Port: {}".format(udp_port))

s.sendto(msg,(udp_host,udp_port))		
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     

udp_host = socket.gethostname()		        
udp_port = 12345	

s.bind((udp_host,udp_port))
while True:
	print("Waiting for client...")
	data,addr = s.recvfrom(1024)	        #receive data from client
	print("Received Messages: {} from {}".format(data, addr))
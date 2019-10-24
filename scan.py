import socket

print("TCP")
for porta in range(1,5001):
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.settimeout(0.3)
	resultTcp = tcp.connect_ex((ip, porta))
	
	if resultTcp == 0:
		print("porta %s: %s" % (porta, "aberta"))

	tcp.close()

print("UDP")
for porta in range(1,1025):
	udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	udp.settimeout(0.3)

	resultUdp =  udp.connect_ex((ip, porta))
	if  resultUdp == 0:
		print("porta %s: %s" % (porta, "aberta"))
	udp.close()




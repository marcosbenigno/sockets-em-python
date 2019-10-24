import socket
HOST = 'localhost'              
PORT = 1027           
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
print ('IP:', HOST)
print ('Porta:', PORT)
while True:
	conn, cliente = tcp.accept()
	print ('Concetado por', cliente)
	while True:
		#msg = con.recv(1024)
		msg = "aa"
		if not msg: break
		print (cliente, msg)
	print ('Finalizando conexao do cliente', cliente)
	conn.close()

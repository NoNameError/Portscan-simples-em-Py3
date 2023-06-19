import socket

ports = [20,21,22,2222,25,80,8080,443,445,53,57] #mude as portas aqui

for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.1)
	code = client.connect_ex(("www.host.com.br", port))  #mude seu host aqui
	if code == 0:	
		print(port, "OPEN  ---  1")
	else:
		print(port, "CLOSED  ---  0")

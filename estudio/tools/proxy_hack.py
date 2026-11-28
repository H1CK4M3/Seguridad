import socket

ip = "127.0.0.1"
port = ""
enlace = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Logica principal del proxy_app

def logic_proxy():
	crear_socket()
	print ("Solicitudes:\n")
	control_trafico()
	
## Creacion del socket para reciver los paquetes
def crear_socket():
	port = int(input("\n Defina el puerto de escucha:"))

	## Definiendo la conexion y estableciendolo en escucha
	
	enlace.bind ((ip, port))
	enlace.listen(10)

## Creando la captura del trafico y el reenvio del mismo

def control_trafico():	
	while True:
		enlace_client, ip_client = enlace.accept()
		connet = enlace_client.recv(4096)
		solicitud = connet.decode("utf-8", errors = "ignore")
		print (solicitud)
		text_div = solicitud.split("\n")

		for text_div in text_div:
			if text_div.startswith("Host:"):
				ip_dst = text_div.replace("Host: ", "").strip()
				print (ip_dst)
				break

		ip_div = ip_dst.split(":")
		ip_envio = ip_div[0]
		if len(ip_div) > int(ip_div[1]):
			puerto_reenvio = int(ip_div[1])
		else:
			puerto_reenvio = 80
		
		reenvio_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		reenvio_soc.connect((ip_dst, puerto_reenvio))
		reenvio_soc.send(connet)
		respuesta = reenvio_soc.recv(4096)
		enlace_client.send(respuesta)
		print (respuesta)
		reenvio_soc.close()
		enlace_client.close()

logic_proxy()


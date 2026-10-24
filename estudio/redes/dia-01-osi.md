#Modelos OSI TCP/IP

##Capas del Modelo OSI (Modelo de referencia para protocolos de red)

El mismo se encuentra conformado por 7 capas las cuales se definen de la inferior a la superior.

### Capas Fisica

Se encarga de la transmicion de los bits asegurandose que los bit transmitidos sean un 1 y que al receptor le llegue un 1 y no un 0.

Ejemplos: Cable UTP, cable Coaxial, Fibra Optica, NIC, Pares Trenzados de cobre, conectores RJ45

### Capa de Enlace

Permite el control de errores, garantiza el acceso al medio. En la misma comienza a conformarce el PDU agregando las direcciones MAC y es llamado (trama)

Ejemplos: ARP, Switch L2, Modems, ADSL, MAC

### Capa de Red

En esta capa es donde se establece la comunicacion con otras redes, para lograr esto realiza 2 de los procesos mas fudamentales en las redes actuales el direccionamiento y el enrutamiento. En esta capa el PDU es denominado (paquete), ademas en esta capa se realiza la fragmentacion de los paquetes
lo que impide que se sobrepase el MTU (Unidad Maxima de Transferencia) de la red impidiendo un posible desbordamiento de la misma

Ejemplos: IP, RIP, BGP, ICMP

### Capa de Transporte

Esta es la capa encargada de definir como se realizaria la comunicacion estableciendo si el segmento que es el nombre que lleva el PDU en esta capa es necesario que llege a su destino o no lo cual es garantizado mediante los protocolos: Protocolo de Control de Transferencia (TCP) y el Protocolo de Datagrama de Usuario (UDP) de los cuales el primero esta orientado a la conexion y el segundo no en esta capa el PDU
es denominado segmento o datagrama

Ejemplos: TCP UDP

TCP (Confiable, Ordenado, controla el flujo y controla la congestion)
UDP (No confiable, sin orden, ligero, sin control)

### Capa de sesion

Funciona como especie de interlocutor el cual define cuando comienza la comunicacion, cuando debe de hablar cada uno.

Ejemplo: SSH Telnet NetBIOS 

### Capa de Presentacion 

Es la encargada de estandarizar los datos para su transmicion soporta formatos jpg, mpeg y mas, ademas de comprimir los datos y de realizar el cifrado de los mismos

Ejemplo: SSL y TLS

### Capa Aplicacion

Esta es la capa mas alta del modelo en la misma el usuario interactua con las aplicaciones las cuales utilizan los protocolos para comunicarse en la red

Ejemplo: DNS, Correo, HTTP, HTTPs


#Modelos OSI TCP/IP

##Capas del Modelo OSI (Modelo de referencia para protocolos de red)

El mismo se encuente conformado por 7 capas las cuales se definen de la inferior a la superior.

### Capas Fisica

Esta es la encargada de transmitir las senales fisicas entre los equipos.

Ejemplos: Cable UTP, cable Coaxial, Fibra Obtica, NIC, Pares Trenzados de cobre

### Capa de Enlace

Actua como enlace entre las 2 capas (Fisica - Red) , permite el control de errores, garantiza el acceso al medio. En la misma comienza a conformarce el PDU agregando las direcciones MAC y es llamado (trama)

Ejemplos: ARP, Switch L2, Modems, ADSL, MAC

### Capa de Red

En esta capa es donde se establece la comunicacion con otras redes, para lograr esto realiza 2 de los procesos mas fudamentales en las redes actuales el direccionamiento y el enrutamiento. En esta capa el PDU es denominado (paquete)

Ejemplos: IP, RIP, BGP

### Capa de Transporte

Esta es la capa encargada de definir como se realizaria la comunicacion definiendo si el segmento que es el nombre que lleva el PDU en esta capa es necesario que llege a su destino o no lo cual es garantizado mediante los protocolos: Protocolo de Controll de Transferencia (TCP) y el Protocolo de Datagrama de usuario (UDP) de los cuales el primero esta orientado a la conexion y el segundo no en esta capa el PDU
es denominado segmento o datagrama

Ejemplos: TCP UDP

### Capa de sesion

Funciona como especie de interlocutor el cual define cuando comienza la comunicacion, cuando debe de hablar cada uno.

Ejemplo: SSH Telnet NetBIOS 

### Capa de Presentacion 

Es la encargada de estandarizar los datos para su transmicion soporta formatos jpg, mpeg y mas, ademas de comprimir los datos, ademas de realizar el cifrado de los datos

Ejemplo: SSL y TLS

### Capa Aplicacion

Esta es la capa con la que interactua al usuario es decir el servicio que sea necesario consumir por el usuario

Ejemplo: DNS, Correo, HTTP, HTTPs


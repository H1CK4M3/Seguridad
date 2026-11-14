# Pickle Rick VM

# Pickle Rick VM

## Metodología de Ataque

1 - Búsqueda de superficie de ataque
2 - Búsqueda de información pública
3 - Explotación de Vulnerabilidad
4 - Escalada de privilegios
5 - Intentos fallidos

## Explicación 

1 - Escaneo de puertos abiertos para identificar posibles servicios activos.
`nmap -sT -Pn -n --open --top-ports 50 -oX`

2 - Se realiza un ataque básico de fuzzing de directorios a través del puerto 80 (HTTP) de la VM.
`dirb <victima>`

  - Se realiza ataque de fuzzing para identificar archivos PHP.
  `dirb <victima> -X .php`
 
  - Se descargó el fichero robots.txt para analizarlo de forma más sencilla.
  `wget <ruta/robots.txt>`

  - Se inspeccionó el código fuente de index.html.
  `curl <victima/index.html>`

3 - Se accedió al sistema desde la ruta `<victima>/login.php` con el usuario `R1ckRul3s` y la contraseña `Wubbalubbadubdub`.

4 - Desde el sitio es posible la ejecución de código remoto (RCE), lo que me permitió ejecutar comandos en el servidor.
  - Se copió el fichero clue.txt al directorio web para leerlo.
  `cp clue.txt /var/www/html/`

4.1 - Se conoció el usuario con el que estábamos interactuando en el sistema.
`whoami`

4.2 - Se identificaron los permisos que poseía el usuario.
`sudo -l`

4.3 - Se logró escalar privilegios debido a una vulnerabilidad de configuración que permite al usuario ejecutar cualquier comando sin solicitud de contraseña (`(ALL) NOPASSWD: ALL`).

4.4 - Se copió el fichero de la segunda flag hacia una ruta donde pudiera leerse.
`sudo cp /home/rick/<nombre_archivo> /var/www/html/`

4.5 - Se conoció el valor de la segunda flag:
`jerry tear`

4.6 - Se revisó qué existía dentro del directorio de root.
`sudo ls /root/`

4.7 - Se identificó un fichero llamado `3rd.txt` y se copió al directorio del servidor web.
`sudo cp /root/3rd.txt /var/www/html/`

4.8 - Se leyó el contenido y se identificó la tercera y última flag:
`fleeb juice`

## Resultados

1 - El escaneo devuelve que solo se encuentran disponibles los puertos 80 (HTTP) y 22 (SSH).

2 - Se lograron identificar directorios interesantes como `/robots.txt`, `/server-status`, `/index.html`.
  - En el análisis de `robots.txt` se identificó el texto `Wubbalubbadubdub` el cual puede estar vinculado a un usuario o contraseña.
  - Se logró identificar en el código HTML el nombre de usuario `R1ckRul3s`.
  - Se logró identificar la ruta `<victima>/login.php`.

3 - Se accedió a la web.

4 - Se pudo obtener el primer ingrediente: `mr. meeseek hair`.

4.1 - El usuario utilizado era `www-data`, el cual es el usuario por defecto que genera el servidor web.

4.2 - La salida de `sudo -l` indica que puede ejecutar cualquier comando sin contraseña.

5 - Se pudo obtener el fichero `clue.txt` que delata que otro ingrediente está en el filesystem.

## Vulnerabilidades

- **Mala configuración del servidor web:** Permite listar directorios y el acceso a ficheros importantes como `robots.txt`. Además, existe una mala práctica de programación al dejar el nombre de usuario en un comentario del código fuente.

- **RCE (Ejecución de código remoto):** Permite la ejecución de comandos del sistema operativo donde se encuentra hospedada la web. Ocurre porque el programador ejecuta funciones del sistema (como `system()` o `exec()`) sin sanitizar la entrada del usuario, permitiéndonos aprovechar esto a nuestro favor.

- **Permisos de usuarios mal declarados:** El usuario `www-data` posee más permisos de los necesarios para realizar sus funciones (puede ejecutar todo como root sin contraseña).


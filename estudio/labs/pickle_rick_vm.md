# Pickle Rick VM

## Metodologia de Ataque

1 - Busqueda de superficie de ataque
2 - Busqueda de informacion publica
3 - Explotacion de Vulnerabilidad

## Explicacion 

1 - Escaneo de puertos abiertos para identificar posibles servicios activos.

nmap -sT -Pn -n --open --top-ports 50 -oX 

2 - Se realiza en ataque basico de fuzzing de directorios a  traves del puerto 80 (HTTP) de la VM.

dirb <victima>

  - Se realiza ataque de fuzzing pero para identificar archivos de php

dirb <victima> -X .php
 
  - Se descargo el fichero robots.txt para analizarlo mas sencillo.

wget <ruta/robots.txt>

  - Se inspecciono el codigo fuente de index.html

curl <victima/index.html>

3 - Se accedio al sistema desde la ruta <victima/login.php> con el usurio R1ckRul3s y la contrasena Wubbalubbadubdub 

4 - Desde el sitio es posible la ejecucion de codigo remoto permitiendome la copia de el fichero clue.txt

cp clue.txt /var/www/html 

## Resultados

1 - Me devuelve que solo se encuentran disponibles los puertos 80 (HTTP) y 22 (SSH).

2 - Se lograron identificar directorios interesantes como el /robots.txt, /server-status, /index.html

  - En el analisis de robots.txt se identifico el texto Wubbalubbadubdub el cual puede estar vinculado a un usuario o contrasena

  - Se logro identificar en el codigo HTML el nombre de usuario R1ckRul3s

  - Se logra identificar la ruta <victima/login.php>

3 - Se accedio a la web

4 - Se puedo obtener el primer ingrediente mr. meeseek hair 

5 - Se pudo obtener el fichero clue.txt que delata que otro ingrediente esta en el filesystem

## Vulnerabilidades

RCE (Ejecucion de codigo remoto)

La misma permite la ejecucion de codigos del sistema donde se encuentra hospedado desde la propia web.

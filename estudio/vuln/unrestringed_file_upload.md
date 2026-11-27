# Unrestringed File Upload

## Descripcion

Esta vulnerabilidad consiste en la posibilidad de subir ficheros sin las restricciones o validaciones adecuadas en una web.

## Identificador CWE/CVE

CWE-434: Unrestricted Upload of File with Dangerous Type

## ?Como funciona?

1 - En la web se identifica un formulario el cual solicita la subida de ficheros los que pueden ser una imagen, documento o un 
compactado. 
	1.1 - Este formulario puede ser que no posea ningun nivel de validacion de lado del cliente
	1.2 - O esta validacion no incluye los tipos de ficheros que se pueden subir a la misma

2 - Lo cual permite a un atacante utilizar esta brecha para subir al sitio un script malisioso
	2.1 - Que pueda contener una reverse shell que brinde acceso al servidor (victima)

## Impacto

El atacante mediante esto puede ganar acceso al servidor que corre el servicio permitiendo incluso modificarlo, apagarlo o incluso
exfiltrar datos.

## Prevencion

### Web

- Realizar en la validacion del formulario una lista blanca la cual solo permita la subida de ficheros correspondientes como jpg,
pdf, doc.

	- Cabe destacar que en los pdf y doc se debe de tener cuidado debido a los elementos macro que los mismos pudieran poseer.

- Identificar el hash del archivo y realizar una busqueda del mismo que nos permita identificar si es malisioso.
 
- Renombrar el archivo a la hora de subierce el sistema para el servidor y almacenarlo en una ruta externa al servicio web.

### Servidor

- Montar sistema antivirus y disenar script que permita el analisis sistematico de los ficheros en la ruta creada para identificar 
posibles amenazas.

- Validar sistematicamente en BD que los ficheros posean las caracteristicas requeridas.


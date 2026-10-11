#Errores 

##Problemas

### Errores de typeo

Error: el error estaba dado porque no podia cambiar el idioma del teclado para poner acentos y determindas letras

Solucion: 

Pasos:

1 - Declarar con que vas a hacer el cambio de layout

setxkbmap -layout es,gb -option grp:alt_shift_toggle

Lo cual le dice al sistema que debe de cambiar entre los layouts es y gb cada vez que presione alt+shift

2 - Agregar esto al bspwmrc

Lo que permite que cada vez que inicie el sistema esa tarea se ejecute y sea posible hacer los cambios 

### Errores al iniciar 

Error: al solucionar el problema anterior borro sin querer el contenido del fichero bspwmrc y no lo tenia guardado en los dotfiles por lo que tuve
que rehacer el fichero.

Error 2: durante la realizacion el documento no escribo el #!/bin/bash por lo que al reinicial el PC no levantaba el PC

Error 3: en la reparacion declaro !#/bin/bash por lo que el PC no levantaba aun

## Aprendizaje

1 - Realizar salvas de los archivos de configuracion en dotfiles cada vez que realice algun cambio pudiendo levantar de los viejos cualquier error
2 - Fijarme mas a la hora de escribir en los ficheros de configuracion para no cometer errores que dañen el sistema

## Pendientes

1- Realizar script para backup automatico de dotfiles
2- Verificar el shebang antes de guardar cambio y reiniciar

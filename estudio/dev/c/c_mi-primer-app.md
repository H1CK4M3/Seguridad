# Introduccion a C

## Tarea crear una app que me diga mi edad y la direccion de memoria en la que fue almacenada

### Llamado a recursos necesarios 

#include <stdio.h>

#include - permite la utilizacion de funciones existentes en el archivo llamado

Ejemplo 

printf - permite imprimir por pantalla 

### Declaracion de funciones (funcion principal)

int main (){


}

int - devuelve un valor entero
main - funcion principal

### Declaracion de Variables

int nombre = 0;

tipo <nombre> = <valor>

### Otros importantes 

%d - devuelve el valor de la variable entero
%s - devuelve el valor de un string
%c - devuelve el valor de un chart
%p - devuelve la direccion de memoria
   - ,&<variable> - Devuelve el valor de memoria de la variable
\n - Imprime un salto de linea 

## Ejemplo 

#include <stdio.h>

int main(){
	int edad = 32;
	printf ("La edad es de %d\n",edad);
	printf ("Esta almacenada en %p",&edad);	
} 

## Modificar la variable en memoria

### Punteros

### Declaracion de punteros

	int *edad_ptr = &edad;

Lo que hace es almacenar en un puntero la direccion de memoria de esa variable.

### Ejemplo

#include <stdio.h>

int main (){
	int edad = 32;
	int *edad_ptr = &edad;

	*edad_ptr = 33;

printf ("Nunca sabras mi edad real para ti es de %d y esta almecenada en %p", edad, &edad);
}

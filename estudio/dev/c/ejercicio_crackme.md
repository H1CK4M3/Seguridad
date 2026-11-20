# Reto Crackme

## Ejercicio

Crear una app en C que simule una autenticacion

## Logica

- Se declaro la funcion main.
- Se realizo la declaracion de variables declarando 4 variables de 2 para el user y pass por defecto y 2 en las que se 
almacenaran las que introduzca el usuario.
- Las variables tipo strings se declararon de la siguiente forma char variable[] = ""
- Se utilizaron los recursos stdio.h y string.h
- Utilice las funciones printf, scanf y strcmp para mostrar por pantalla
solicitar rellenar textos y comparar strings

## Codigo

#include <stdio.h>
#include <string.h>

int main (){

	char user[20] = "admin";
	char pass[20] = "admin*2026";
	char input_user[20] = "";
	char input_pass[20] = "";

	printf ("El nombre de usuario y la contrasena son \n %s \n %s \n",user, pass);
	printf ("Diga su nombre de usuario \n");
	scanf ("%s",input_user);
	printf ("Diga su contrasena \n");
	scanf ("%s",input_pass);
	
	printf ("%s \n", input_user);
	printf ("%s \n", input_pass);
	
	if (strcmp(input_user, user) == 0 && strcmp(input_pass, pass) == 0){
		printf ("Has accedido");
		return 0;
	}
	else {
		printf ("Accedo Denegado");
		return 1;
	}
}

## Errores

- Me dio problema el uso del salto de linea \n en la funcion de scanf, no conocia que el en si aplica un salto de linea
al final
- Al comparar con strcmp
	- Hice la comparacion como si la estuviera realizando en java condicion = valor y como se realiza es 
	igualando a 0 si es real u otro valor entero si es falso.
	- Hice las condiciones con true o false en vez de utilizar 0 y 1.

## Notas

- La funcion main siempre va a devolver un entero

int main()

- Dentro de los scanf no se declaran saltos de linea
- Las comparaciones de string con strcmp devuelven 0 si se cumple la condicion 
o cualquier otro valor entero en caso de no cumplirse.
- Los string se declaran como un arreglo de caracteres char[]
- Para almacenar elementos en una variable no tengo que usar ningun operador
solo "," y el nombre de la variable en la cual voy a almacenar esto solo aplica en los scanf.
- La declaracion de un string en C se realiza declarando un arreglo de caracteres.

Ejemplo:

char nombre[] = "";

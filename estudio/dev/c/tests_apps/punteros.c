#include <stdio.h>

int main (){

	int edad = 32;
	int *edad_ptr = &edad;
	
 	*edad_ptr = 33;
	printf ("Mi edad es de %d y en memoria %p", edad, edad_ptr);
}

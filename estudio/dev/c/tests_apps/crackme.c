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

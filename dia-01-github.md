# Como utilizar github para subir repos y demas

Para subir elementos a github a partir de versiones mas recientes es necesario utilizar el protocolo SSH para esto es necesario seguir los 
siguientes pasos:


1- Generamos un key ssh en nuestro PC
ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519_github -C "ssh key for github"
2- Iniciamos el agente de SSH
eval "$(ssh-agent -s)"
3- Agregamos nuestra llave generada
ssh-add ~/.ssh/id_ed25519_github
4-Copiamos la key generada
5- Probamos las conexion
ssh -T git@github.com
6- Anademos esta clave generada a nuestra cuenta github
cat ~/.ssh/id_ed25519_github.pub
7- Probamos la conexion
ssh -T git@github.com
8- Debe decirnos que la autenticacion ha sido correcta
9- Configuramos git para ssh
git remote set-url origin git@github.com:username/repository.git
10- Crear una cuenta en github y acceder a ella
11- Buscar en la seccion de configuracion la seccion SSH y GPG keys
12- Pegamos la key generada de nuestro PC

Para subir actualizar nuestros repos seria de la siguente manera

1- Generamos una captura  
git commit -m "<nombre>"
2- Agregamos la ruta de la carpeta que vamos a anadir 
git add <ruta de la carpeta a anadir>
3- Subimos lo nuevoc
git push git@github.com:<username>/<nombre_repo.git>


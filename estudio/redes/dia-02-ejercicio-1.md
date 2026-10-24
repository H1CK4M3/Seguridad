# Tema 1 - Ejercicio 1

1 - Realizar una captura de trafico, abrir un navegador desde el acceder
a Google eh identificar mi servidor DNS y la IP de Google
2 - Identificar capura de handshake eh identificar a que puerto se
conecto

# Respuesta

Ejercicio 1

- Se logra captar la direccion IP de mi DNS: 192.168.1.1
- Se logran identificar 1 paquetes con la conexion con el servidor autoritativo ns1.google.com
- Se logra identidicar otra paquete con las direcciones un clase A fonts.gstatic.com 142.251.210.67
- Se logra identificar 4 servidores DNS ns4.google.com ns3.google.com ns2.google.com ns1.google.com 
con las direcciones IP 216.239.34.10, 216.239.36.10, 2001:4860:4802:36::a, 216.239.38.10

Ejercicio 2



## Obsevaciones

Extras

- En el analisis de captura se identifica un grupo de paquetes consecutivos de TCP que envian ACK
- Se logra identificar que el seq es el mismo, el valor de ACK sigue en crecimiento lo que significa que esta constantemente reportando que el paquete llego a su destino
- Se identifica que el valon del len es 0 lo que indica que no se estan enviando 
nuevos datos.
- Se identfica que el ACK si se encuentra en aumento lo cual notifica
que recivio los datos que el siguien que espera es X 

Ejercicio 1

- Solo se obseva trafico de DNS de mi IP con la 192.168.1.1 (router)
- La 192.168.1.1 es la que esta haciendo funcion de servidor de DNS es 
decir y es esta la que realiza las peticiones hacia mi proveedor de servicio
- Para identificar la IP de google es necesario un analisis del paquete
directo contra google sino que pasan a traves de mi router y este le responde a mi PC
- En el paquete de respuesta si debe de venir la direccion IP de google
- No se va a observar MAC de DNS de google debido a que la esta solo es visible en comunicaciones a nivel local
y el intercambio y asignacion de MAC es en capa 2

Ejercicio 2


## Notas

Seq - es el numero de identificacion del primer byte de datos es el valor que posibilita armar luego
la informacion.
Len - es el tamano del payload del paquete.

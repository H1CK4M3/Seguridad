#Dia 1 Reconocimiendo del equipo

## Objetivo 

Conocer los recursos del pc

## Comandos utilizados

Para conocer la cantidad de RAM que posee y la restante

free me lo sugirieron

free -h - el cual me da las capacidades en GB 
free -m - da las capacidades en MB

fdisk ya lo conocia de antes

fdisk -l - da la info del disco incluso el tipo de tabla de particiones y mas
fdisk -x - da la info del disco con aun mas detalles

ifconfig lo aprendi hace anos cuando empece mis primeros pasos en linux
ip es el estandar actual para ver los caracteristicas de nuestra conexon

nmcli lo conoci recientemente por una IA para gestionar todo el tema de la conectividad

nmcli device wifi list - permite ver las redes wifi existentes
nmcli device disconnect <interfaz> - permite desconectarme de la red activa
nmcli device wifi connect "SSID" "KEY" - para conectarme a una red especifica
nmcli device down - apaga le interfaz de red

## Salidas

free -h

               total       usado       libre  compartido   búf/caché  disponible
Mem:           3,6Gi       939Mi       1,2Gi       129Mi       1,9Gi       2,7Gi
Inter:         4,0Gi          0B       4,0Gi

free -m
               total       usado       libre  compartido   búf/caché  disponible
Mem:            3734         939        1229         129        1917        2795
Inter:          4081           0        4081

fdsik

Disco /dev/sda: 931,51 GiB, 1000204886016 bytes, 1953525168 sectores
Modelo de disco: TOSHIBA MQ04ABF1
Unidades: sectores de 1 * 512 = 512 bytes
Tamaño de sector (lógico/físico): 512 bytes / 4096 bytes
Tamaño de E/S (mínimo/óptimo): 4096 bytes / 4096 bytes
Tipo de etiqueta de disco: gpt
Identificador del disco: DDB6ED40-5869-4A50-B070-D3DB8493B913
Primera LBA utilizable: 34
Última LBA utilizable: 1953525134
LBA alternativa: 1953525167
LBA inicial de las entradas de las particiones: 2
Particiones asignadas: 128
LBA final de las entradas de las particiones: 33

Disposit.  Comienzo      Final   Sectores Tipo-UUID                            UUID                                 Nombre               Atributos
/dev/sda1      2048    1050623    1048576 C12A7328-F81F-11D2-BA4B-00A0C93EC93B B0C277F1-F355-4E76-80DE-6C55DB54A154 EFI System Partition 
/dev/sda2   1050624 1953523711 1952473088 0FC63DAF-8483-4772-8E79-3D69D8477DE4 3BED5660-AB8D-4F34-A82D-9CD753B0F9D1   

ip a

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:e9:3a:f4:73:f9 brd ff:ff:ff:ff:ff:ff
    altname wlp2s0
    inet 192.168.1.109/24 brd 192.168.1.255 scope global dynamic noprefixroute wlo1
       valid_lft 84335sec preferred_lft 84335sec
    inet6 fe80::7f1:859f:8e92:c0f7/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever

nmcli device wifi list

IN-USE  BSSID              SSID                  MODE   CHAN  RAT>
*       30:B5:C2:B2:CF:6B  Home_Internet         Infra  9     130>
        6E:63:F8:D4:35:A4  Loco5AC:6C63F8D435A4  Infra  1     130>

## Interpretacion

free Me muestra el total de capacidad de memoria, la contidad utilizada y la cantidad libre diferenciando que -h en GB y -m en MB ademas de especificar la capacidad fisica total de RAM y la que reserva necesaria para el funcionamiento del kernel

En el momento de la captura tenia una capacidad total de 4 GB, capacidad utilizable por el kernel 3.6 GB, en uso 939 MB y libres 1.2GB utilizado por buffer/cache 1.9 GB y disponible 2.7 GB 

fdisk Me mostro la capacidad total de almacenamiento, donde se encuentra montado y modelo, id y demas de mi almacenamiento

En la conectividad  me muestra que solo tengo una interfaz de red y el direccionamiento del mismo ademas de otras caracteristicas como la direccion MAC y la IP 

nmcli 

IN-USE - Es la red a la que me encuentro conectado actualmente
BSSID - Es la MAC del dispositivo por el cual estoy accediendo a dicha red
SSID - Es el nombre de la red
MODE - Este especifica si la conexion es un punto a punto o es a traves de un router intermediario 
CHAN - Es el canal por el cual esta viajando la senal
RATE - Es la la velocidad de transmicion negociada entre los dispositivos

ip a

Interfaces:

lo - Es la interfaz de bucle o loopback permite la comunicacion del propio host con el mismo sin intermedicion de una red externa esta direccion no es accesible desde fuera del propio host su direccion ip en IPv4 127.0.0.1 IPv6 ::1 es muy usado para la realizacion de pruebas de servicios en local
antes de ser desplegados en la red o por desarrolladores para probar sus aplicaciones. Al enviar un paquete a esta direcciones la pila TCP/IP reonoce que es una direccion local y reenvia esos paquetes a traves de la pila TCP/IP del dispositivo  

/8 - Significa que la mascara es 255.0.0.0

wlo1 - Es la otra interfaz de red que contiene mi dispositivo en este caso una interfaz inalambrica fisica

altname - es un nombre alternativo para la interfaz en cuestion yo pudiera llamar a mi interfaz por wlo1 o wlp2s0 

inet - es la direccion IP actual de la interfaz

up - indica que la interfaz se encuentra activa


broadcast (flags) - la interfaz tiene capacidad para enviar broadcast 

multicast (flags) - la interfaz tiene capaciada para enviar multicast

LOWER_UP - indica que la capa de enlace esta activa

mtu (Maximum Transmition Unit) - Indica el tamano maximo del payload de la trama ethernet sin fragmentarse

inet - indica la direccion IP del mi dispositivo actualmente

/24 - indica que la mascara de la subred 255.255.255.0 y hay 256 direcciones ip 254 utilizables y la de red y broadcast

broadcast 192.168.1.255  Esta es la direccion de dificion o de broadcast su funcion es el envio de paquetes a todos los equipos de la subred
 
## No entendi

free no entendi que es el buf/cache

Memoria Libre

La mememoria libre es la memoria que no se encuenta asignada a ningun proceso en ejecucion 

La memoria disponible esta compuesta por la memoria libre + una porcion de la memoria de buffer y de cache que puede ser vaciada rapidamente para ser nuevamente utilizada

buff/cache

Para entenderlo mejor vamos a dividir los conceptos porque realmente son conceptos distinto

buffer - es un espacio intermedio en la RAM (rapido) entre el CPU (rapido) y el almacenamiento (lento) lo cual funciona de la siguente forma la CPU necesita acceder al algo en el disco este no va a buscarlo directo al disco sino que el disco lo almacene en la RAM y la CPU accede a el desde la RAM y cuando muere el proceso el archivo no es liberado por si algun otro proceso necesita de el, es liberado cuando otro proceso necesita ese espacio.  

cache - este es una porcion de la memoria donde se almacenan archivos frecuentemente utilizables permitiendo una lectura mas rapidas de los mismos ya que no se hace necesaria acceder al disco mucho mas lento 


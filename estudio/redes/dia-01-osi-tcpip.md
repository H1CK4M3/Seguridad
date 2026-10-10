#OSI  TCP/IP

##Capas del Modelo OSI (Modelo de referencia para protocolos de red)

Su funcion principal es definir estandares que permitan la comunicacion entre diferentes hardware, aplicaciones y sistemas que existen
establece las caractaristicas que debe de poseer cada uno de estos elementos para que sea posible una comunicacion efectiva entre los mismos esto permite que las capas superiores puedan utilizar tecnologias de las capas inferiores sin necesidad de una implementacion

###Fisica 

Esta capa organiza y establece estandares para los medios de transmicion de informacion y sus tecnologias

- cables UTP, cables Fibra 
- las tecnologias de transmision inalambrica bluetooth, wifi, 
- equipos de comunicacion switches, routers

Ejemplo: Esto es lo que permite que dispositivos como con diferentes versiones de antenas wifi ej. WiFi 5 y WiFi 7 puedan comunicarse perfectamente asi como con el resto de tecnologias y equipos
Resumiendo: Esta capa dicta las metricas que deben de poseer el hardware para que sea compatible entre todos y no exista la necesidad de cambiarlo cada vez que se actualicen o salgan mas modernos o con mayores prestaciones 

!!! Senales

###Enlace a Datos

Esta capa existe una vez que esta implementada la capa fisica su principal funcion es controlar que las senales recividas de la capa fisica y los paquetes recividos de la capa logica vengan con las caracteristicas necesarias que permitan
una comunicacion lo mas correcta posible ya a partir de esta capa es que existen los protocolos de redes

- Procolo ADSL: Controla que la senal telefonica no venga con ruido y con la intensidad necesaria ademas que permite verificar el estado de la capa fisica
- Protocolo Ethernet: Este se subdivide en 2 capas la capa MAC y la LLC  entre las cosas que define son los elementos que son agregados a la trama de red
- Protocolo ARP: Este almacena en cada equipo una tabla con las direcciones MAC/IP de cada dispositivo con el que se ha comunicado
permitiendo buscar rapidamente el nombre real del equipo para realizar la transmision de datos. 

Ejemplo: Esta capa es la que actua como traductor entre la capa fisica y la capa de red adem
Resumiendo: Este protocolo su principal funcion es la de controlar la tranferencia de los datos

!!! Frames

###Capa de Red

Esta capa es la que posibilita la conectividad entre dos redes fisicamente aisladas utilizando las caracteristicas de las capas inferiores

- Protocolo BGP
- Protocolo IP
- Protocolo ICMP
- Protocolo IGMP
- Protocolo OCPF

!!! Packets

##Protocolos Multicapas

ADSL: Fisica, Enlace a Datos
Bluetooth: Fisica, Enlace a Datos
Wifi: Fisica, Elace a Datos
IP: Enlace a Datos, Red
ARP: Enlace a Datos, Red

### Capa de Transporte


Transporte -
Session - 
Aplicacion
Presentacion 

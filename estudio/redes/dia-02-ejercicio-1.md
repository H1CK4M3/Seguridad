# Tema 1 - Ejercicios de Captura (Wireshark/Tcpdump)

## Ejercicio 1: Análisis DNS y de Red

### Respuesta
- **DNS Local:** Se captó la IP de mi servidor DNS: `192.168.1.1`.
- **Servidores Autoritativos:** Se identificaron 4 servidores DNS de Google:
  - `ns4.google.com` (216.239.34.10)
  - `ns3.google.com` (216.239.36.10)
  - `ns2.google.com` (2001:4860:4802:36::a)
  - `ns1.google.com` (216.239.38.10)
- **Registros A:** Se identificó un registro A para `fonts.gstatic.com` con IP `142.251.210.67`.

### Observaciones
- Solo se observa tráfico DNS de mi IP (`192.168.1.109`) hacia mi router (`192.168.1.1`).
- Mi router actúa como intermediario (DNS local). Él es quien consulta a internet y luego me responde.
- **Aclaración MAC vs IP:** No se observa la MAC de Google porque la MAC solo existe en la red local (Capa 2). El único salto de Capa 2 es entre mi PC y mi router. La comunicación hacia Google se hace por IP (Capa 3).

---

## Ejercicio 2: Análisis de Handshake y ACKs (TCP)

### Respuesta
- Se identifica el handshake TCP entre mi PC y la IP `104.21.54.91`.
- La comunicación es **HTTPS** porque se realiza por el puerto `443`.
- La comunicación se inició correctamente: se capturó el paquete `SYN` (solicitud), seguido del `SYN/ACK` (respuesta del servidor) y el `ACK` final.

### Observaciones (Control de Flujo)
- Se identifica un grupo de paquetes consecutivos TCP enviando ACK.
- El `Seq` se mantiene fijo, mientras el valor de `Ack` va en aumento. Esto significa que se está confirmando la recepción de datos.
- Se identifica que el valor de `Len` es `0`, lo que indica que no se están enviando nuevos datos de aplicación.
- El `Ack` en aumento notifica que se recibieron los datos y el siguiente que se espera es X.

---

## Notas Técnicas (Conceptos Clave)

- **Seq (Sequence Number):** Es el número de identificación del primer byte de datos. Es el valor que posibilita el **reensamblado** de la información (saber cuál es el primero y cuál el último). En el handshake inicial (SYN), el `Seq` es 0 al no haber datos previos.
- **Len (Length):** Es el tamaño del **payload** (carga útil o datos reales de la aplicación). No incluye las cabeceras. Si es 0, no hay información de aplicación en el paquete.
- **Ack (Acknowledgment):** Es el número del siguiente byte que el receptor espera recibir. Confirma la recepción de los datos anteriores.

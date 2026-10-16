PLAN DE ESTUDIO: RED TEAMER — DE CERO A EXPERTO
Formato: Markdown exportable. Guárdalo en ~/estudio/plan-red-team.md.
Uso: Marca [x] cuando cumplas cada tema. Envía los ejercicios al terminar cada tema.

ÍNDICE
FASE 0: PREPARACIÓN DEL ENTORNO

FASE 1: FUNDAMENTOS (4-6 meses)

Tema 1: Redes

Tema 2: Linux

Tema 3: Windows

Tema 4: Programación

Tema 5: Criptografía

FASE 2: SEGURIDAD OFENSIVA BASE (3-4 meses)

Tema 6: Metodología de Pentesting

Tema 7: Reconocimiento y Enumeración

Tema 8: Vulnerabilidades Web

Tema 9: Explotación de Servicios

Tema 10: Post-Explotación

FASE 3: RED TEAM AVANZADO (6-12 meses)

Tema 11: Active Directory

Tema 12: Evasión y Payloads

Tema 13: C2 Frameworks

Tema 14: Exploit Development

Tema 15: Reversing

Tema 16: Cloud Red Team

FASE 4: MAESTRÍA (12+ meses)

<a name="fase-0"></a>

FASE 0: PREPARACIÓN DEL ENTORNO
Tema 0.1: Laboratorio de trabajo
Objetivo: Tener un entorno controlado para practicar sin riesgo legal.

Subtemas:

□ Virtualización: VirtualBox/VMware/Proxmox
□ Máquina atacante: Kali Linux
□ Máquinas víctima: Metasploitable2, DVWA, Windows 10/Server
□ Red aislada (host-only o NAT)
□ Snapshots y backups
Ejercicios:

Básico:

Instala Kali Linux en una VM.
Instala Metasploitable2 en otra VM.
Configura una red host-only para que se comuniquen.
Verifica conectividad con ping y nmap.
Intermedio:

Añade una VM Windows 10 y una Windows Server.
Crea una red interna aislada con 4 VMs.
Toma snapshots antes de cada práctica.
Avanzado:

Monta un laboratorio con Proxmox o ESXi.
Configura VLANs para segmentar el laboratorio.
Documenta todo el setup en tu GitHub.
Recursos: VirtualBox Docs, Kali Docs, VulnHub.

<a name="fase-1"></a>

FASE 1: FUNDAMENTOS (4-6 meses)
<a name="tema-1"></a>

Tema 1: Redes desde cero
Objetivo: Entender cómo se comunican los sistemas, desde el cable hasta la aplicación.

Subtemas
□ 1.1 Modelo OSI (7 capas)
□ 1.2 Modelo TCP/IP (4 capas)
□ 1.3 Mapeo OSI ↔ TCP/IP
□ 1.4 PDU por capa (bit, trama, paquete, segmento, datos)
□ 1.5 Direccionamiento IPv4
□ 1.6 Direccionamiento IPv6
□ 1.7 Subnetting (CIDR, máscaras, cálculo)
□ 1.8 VLSM
□ 1.9 Protocolo ARP
□ 1.10 Protocolo IP (IPv4/IPv6)
□ 1.11 Protocolo ICMP
□ 1.12 Protocolo TCP (handshake, flags, control)
□ 1.13 Protocolo UDP
□ 1.14 Protocolo DNS
□ 1.15 Protocolo DHCP
□ 1.16 Protocolo HTTP/HTTPS
□ 1.17 Protocolo TLS/SSL
□ 1.18 Routing (estático y dinámico)
□ 1.19 Switching y VLANs
□ 1.20 NAT y PAT
□ 1.21 Firewalls y ACLs
□ 1.22 Wireshark (captura y análisis)
□ 1.23 tcpdump
□ 1.24 Nmap (tipos de escaneo)
Ejercicios
Nivel 1 — Básico:

Explica con tus palabras qué ocurre paso a paso cuando escribes google.com en el navegador.

Dibuja el modelo OSI con 2 protocolos por capa.

Calcula máscara, red, broadcast y rango de IPs para 192.168.10.0/26.

Calcula lo mismo para 10.0.0.0/8, 172.16.0.0/16, 192.168.1.0/24.

Captura con Wireshark un handshake TCP y describe SYN, SYN-ACK, ACK.

Nivel 2 — Intermedio:

Configura manualmente IP, máscara y gateway en Linux.

Usa tcpdump para capturar solo DNS y explica qué ves.

Explica diferencia entre switch, router, hub y en qué capa OSI opera cada uno.

Captura un DHCP completo (DORA) y describe los 4 paquetes.

Analiza una tabla ARP y explica cómo funciona ARP spoofing.

Configura una VLAN en un switch virtual.

Escanea una máquina con Nmap: -sS, -sT, -sU, -sV, -O, -A.

Nivel 3 — Avanzado:

Divide 172.16.0.0/16 en 4 subredes con al menos 500 hosts cada una.

Captura y analiza tráfico TLS: identifica Client Hello, Server Hello, certificado.

Configura un firewall con iptables o nftables y bloquea tráfico específico.

Simula ARP spoofing en tu laboratorio con arpspoof.

Configura un servidor DNS local con dnsmasq y resuelve dominios personalizados.

Analiza un ataque MITM contra HTTP y documenta el proceso.

Usa Nmap NSE para detectar vulnerabilidades en una máquina vulnerable.

Recursos: Cisco Networking Academy, Wireshark User's Guide, subnettingpractice.com, RFC 791, 793, 826, 2131, 768.

<a name="tema-2"></a>

Tema 2: Linux para seguridad
Objetivo: Dominar la línea de comandos, administración y hardening.

Subtemas
□ 2.1 Jerarquía del sistema de archivos (FHS)
□ 2.2 Permisos (chmod, chown, umask)
□ 2.3 Usuarios y grupos
□ 2.4 Procesos (ps, top, htop)
□ 2.5 Servicios y systemd
□ 2.6 Logs (journalctl, dmesg, /var/log)
□ 2.7 Gestión de paquetes (apt, dpkg)
□ 2.8 Bash scripting
□ 2.9 Cron y tareas programadas
□ 2.10 Redes en Linux (ip, ss, nmcli)
□ 2.11 Firewall (ufw, iptables, nftables)
□ 2.12 Hardening (lynis, fail2ban, AppArmor)
□ 2.13 Cifrado de disco (LUKS)
□ 2.14 Gestión de claves SSH
□ 2.15 Compilación y gestión de software
Ejercicios
Nivel 1 — Básico:

Crea usuario pentester con home y shell /bin/bash.

Explica -rwxr-xr-- vs -rw-r--r--.

Busca en /var/log intentos fallidos de SSH.

Lista procesos que escuchan en puertos TCP.

Crea 5 archivos y cambia sus permisos.

Nivel 2 — Intermedio:

Configura ufw para bloquear todo excepto SSH y HTTP.

Corre lynis y documenta 3 hallazgos.

Script Bash: backup de /home a /backup con cron.

Configura fail2ban para SSH y verifica baneos.

Audita permisos de /etc y busca archivos world-writable.

Configura claves SSH sin contraseña.

Nivel 3 — Avanzado:

Configura AppArmor para un script propio.

Cifra una partición con LUKS.

Escribe un script que detecte cambios en archivos críticos (/etc/passwd, etc.).

Configura un servidor SSH con autenticación por clave y 2FA.

Audita un sistema con chkrootkit y rkhunter.

Escribe un script de hardening completo para un servidor.

Recursos: man, Arch Wiki, "Linux Basics for Hackers" (OccupyTheWeb).

<a name="tema-3"></a>

Tema 3: Windows para seguridad
Objetivo: Entender Windows a nivel de administración y seguridad.

Subtemas
□ 3.1 Estructura de Windows
□ 3.2 Registro de Windows
□ 3.3 Usuarios y grupos
□ 3.4 Permisos NTFS
□ 3.5 Servicios de Windows
□ 3.6 PowerShell
□ 3.7 CMD y herramientas nativas
□ 3.8 Event Viewer y logs
□ 3.9 Active Directory (introducción)
□ 3.10 Group Policy (GPO)
□ 3.11 Firewall de Windows
□ 3.12 Windows Defender
□ 3.13 Hardening de Windows
Ejercicios
Nivel 1 — Básico:

Lista usuarios y grupos locales con net user y net localgroup.

Navega el registro con regedit y busca claves de inicio.

Lista servicios con sc query y Get-Service.

Lee el Event Viewer y encuentra intentos fallidos de login.

Nivel 2 — Intermedio:

Configura permisos NTFS en una carpeta.

Escribe un script PowerShell que liste procesos y servicios.

Configura una GPO básica en un dominio.

Audita cuentas de usuario con net accounts.

Nivel 3 — Avanzado:

Configura Active Directory en Windows Server.

Une un Windows 10 al dominio.

Crea usuarios, grupos y OUs en AD.

Aplica GPOs para restringir acciones.

Audita AD con BloodHound (introducción).

Hardening completo de Windows Server.

Recursos: Microsoft Docs, "Windows Internals", "Active Directory" (Brian Desmond).

<a name="tema-4"></a>

Tema 4: Programación para seguridad
Objetivo: Automatizar, escribir herramientas y entender código.

Subtemas
□ 4.1 Python: sintaxis y tipos
□ 4.2 Python: control de flujo
□ 4.3 Python: funciones
□ 4.4 Python: listas, tuplas, diccionarios
□ 4.5 Python: archivos y errores
□ 4.6 Python: módulos y paquetes
□ 4.7 Python: os, sys, subprocess, re
□ 4.8 Python: socket (redes)
□ 4.9 Python: requests (HTTP)
□ 4.10 Python: scapy (paquetes)
□ 4.11 Python: threads y concurrencia
□ 4.12 Bash: scripting avanzado
□ 4.13 PowerShell: scripting
□ 4.14 SQL: consultas básicas
□ 4.15 JavaScript: básico
□ 4.16 Git y GitHub
Ejercicios
Nivel 1 — Básico:

Script Python: pide nombre y edad, devuelve saludo y edad+1.

Script Bash: lista archivos .txt y los cuenta.

Script Python: lee un archivo y cuenta líneas.

Script PowerShell: lista procesos activos.

Nivel 2 — Intermedio:

Escáner de puertos en Python con socket.

Parser de logs que cuenta IPs.

Cliente/servidor TCP en Python.

Script Bash que hace backup con rsync.

Script Python que descarga una web con requests y muestra cabeceras.

Script que resuelve un dominio a IP.

Nivel 3 — Avanzado:

Escáner de red con scapy.

Herramienta que detecta hosts vivos en una red.

Cliente HTTP que envía POST con datos.

Script que combina Nmap + Python para reportar vulnerabilidades.

Banner grabber multihilo.

Script que automatiza la enumeración de SMB.

Herramienta CLI con argparse.

Recursos: docs.python.org, Real Python, "Automate the Boring Stuff", "Black Hat Python".

<a name="tema-5"></a>

Tema 5: Criptografía
Objetivo: Entender confidencialidad, integridad y autenticación.

Subtemas
□ 5.1 Tríada CIA
□ 5.2 Cifrado simétrico (AES, DES)
□ 5.3 Cifrado asimétrico (RSA, ECC)
□ 5.4 Funciones hash (SHA-256, MD5)
□ 5.5 HMAC
□ 5.6 Certificados digitales
□ 5.7 TLS/SSL
□ 5.8 PKI
□ 5.9 Firmas digitales
□ 5.10 Autenticación (contraseñas, tokens, biometría)
Ejercicios
Nivel 1 — Básico:

Diferencia entre cifrado simétrico y asimétrico.

Calcula SHA-256 de un archivo.

Explica qué es un hash y para qué sirve.

Nivel 2 — Intermedio:

Cifra/descifra con AES usando openssl.

Inspecciona certificado TLS de google.com.

Genera par de claves RSA.

Firma y verifica un mensaje.

Nivel 3 — Avanzado:

Explica MITM contra TLS y cómo prevenirlo.

Rompe un hash MD5 con hashcat (en laboratorio).

Crea tu propia CA y firma un certificado.

Analiza un handshake TLS en Wireshark.

Recursos: "Serious Cryptography", man openssl, "Cryptography Engineering".

<a name="fase-2"></a>

FASE 2: SEGURIDAD OFENSIVA BASE (3-4 meses)
<a name="tema-6"></a>

Tema 6: Metodología de Pentesting
Objetivo: Entender las fases de un pentest profesional.

Subtemas
□ 6.1 Tipos de pentest (black, white, gray box)
□ 6.2 Fases: reconocimiento, enumeración, explotación, post-explotación, reporte
□ 6.3 Alcance y reglas de engagement
□ 6.4 OSINT
□ 6.5 Documentación y reporte
□ 6.6 Frameworks: PTES, OWASP WSTG, MITRE ATT&CK
Ejercicios
Nivel 1 — Básico:

Define las 5 fases de un pentest.

Explica diferencia entre pentest, análisis de vulnerabilidades y red team.

Redacta un alcance ficticio para un pentest.

Nivel 2 — Intermedio:

Haz OSINT de un dominio propio (whois, DNS, subdominios).

Documenta un pentest simulado siguiendo PTES.

Mapea TTPs a MITRE ATT&CK.

Nivel 3 — Avanzado:

Redacta un informe de pentest completo de un laboratorio.

Diseña un plan de pentest para una empresa ficticia.

Presenta el informe como si fuera a un cliente.

Recursos: PTES, OWASP WSTG, MITRE ATT&CK.

<a name="tema-7"></a>

Tema 7: Reconocimiento y Enumeración
Objetivo: Recopilar información del objetivo.

Subtemas
□ 7.1 Reconocimiento pasivo (OSINT, whois, DNS)
□ 7.2 Reconocimiento activo (Nmap, ping sweep)
□ 7.3 Enumeración de servicios (SMB, FTP, SSH, HTTP)
□ 7.4 Enumeración de usuarios
□ 7.5 Enumeración web (gobuster, dirb, ffuf)
□ 7.6 Google dorks
□ 7.7 Shodan, Censys
□ 7.8 theHarvester, Maltego
Ejercicios
Nivel 1 — Básico:

Haz whois y DNS lookup de un dominio.

Escanea una máquina con Nmap y documenta servicios.

Encuentra subdominios con sublist3r.

Nivel 2 — Intermedio:

Enumera SMB en una máquina vulnerable con enum4linux.

Enumera directorios web con gobuster.

Usa Google dorks para encontrar información.

Nivel 3 — Avanzado:

OSINT completo de una persona ficticia.

Enumeración web completa con ffuf y wfuzz.

Combina theHarvester + Maltego para un informe.

Recursos: man nmap, man gobuster, OSINT Framework.

<a name="tema-8"></a>

Tema 8: Vulnerabilidades Web
Objetivo: Explotar las vulnerabilidades más comunes en aplicaciones web.

Subtemas
□ 8.1 HTTP a fondo
□ 8.2 OWASP Top 10
□ 8.3 SQL Injection
□ 8.4 XSS (reflected, stored, DOM)
□ 8.5 CSRF
□ 8.6 SSRF
□ 8.7 XXE
□ 8.8 Deserialización insegura
□ 8.9 Autenticación y sesiones
□ 8.10 JWT
□ 8.11 Burp Suite
□ 8.12 APIs REST y GraphQL
Ejercicios
Nivel 1 — Básico:

Haz peticiones GET y POST con curl.

Identifica cabeceras de seguridad.

Instala Burp Suite y configura el proxy.

Nivel 2 — Intermedio:

5 labs de SQLi en PortSwigger.

5 labs de XSS en PortSwigger.

Intercepta y modifica peticiones con Burp.

Nivel 3 — Avanzado:

5 labs de SSRF, XXE, deserialización.

Explota JWT mal configurado.

Bug bounty en un programa público.

Recursos: PortSwigger Academy, OWASP Top 10, "The Web Application Hacker's Handbook".

<a name="tema-9"></a>

Tema 9: Explotación de Servicios
Objetivo: Explotar servicios de red vulnerables.

Subtemas
□ 9.1 Metasploit Framework
□ 9.2 Searchsploit y Exploit-DB
□ 9.3 Explotación de SMB (EternalBlue)
□ 9.4 Explotación de FTP, SSH, Telnet
□ 9.5 Explotación de bases de datos
□ 9.6 Explotación de servidores web
□ 9.7 Password attacks (Hydra, John, Hashcat)
□ 9.8 Reverse shells y bind shells
Ejercicios
Nivel 1 — Básico:

Explota Metasploitable2 con Metasploit.

Usa searchsploit para encontrar exploits.

Crea un reverse shell básico.

Nivel 2 — Intermedio:

Ataca contraseñas con Hydra (en laboratorio).

Crackea hashes con John y Hashcat.

Explota EternalBlue en un Windows vulnerable.

Nivel 3 — Avanzado:

Máquina Easy de HTB con writeup.

Máquina Medium de HTB con writeup.

Encadena múltiples vulnerabilidades en VulnHub.

Recursos: TryHackMe, HackTheBox, VulnHub, "Metasploit Unleashed".

<a name="tema-10"></a>

Tema 10: Post-Explotación
Objetivo: Mantener acceso, escalar privilegios y moverse lateralmente.

Subtemas
□ 10.1 Escalada de privilegios Linux
□ 10.2 Escalada de privilegios Windows
□ 10.3 Persistencia
□ 10.4 Movimiento lateral
□ 10.5 Pivoting
□ 10.6 Exfiltración de datos
□ 10.7 Limpieza de huellas
□ 10.8 Password dumping (Mimikatz)
Ejercicios
Nivel 1 — Básico:

Escala privilegios en Linux con sudo -l.

Escala con SUID mal configurado.

Documenta técnicas de escalada.

Nivel 2 — Intermedio:

Escala en Windows con winPEAS.

Dump de hashes con Mimikatz (laboratorio).

Configura persistencia en Linux.

Nivel 3 — Avanzado:

Pivoting a través de una máquina comprometida.

Movimiento lateral en un dominio.

Exfiltración de datos sin ser detectado.

Recursos: "Linux Privilege Escalation" (g0tmi1k), "Windows Privilege Escalation" (FuzzySecurity), HackTricks.

<a name="fase-3"></a>

FASE 3: RED TEAM AVANZADO (6-12 meses)
<a name="tema-11"></a>

Tema 11: Active Directory
Objetivo: Comprometer entornos Windows corporativos.

Subtemas
□ 11.1 Estructura de AD
□ 11.2 Kerberos
□ 11.3 LDAP
□ 11.4 Enumeración de AD (BloodHound, PowerView)
□ 11.5 Kerberoasting
□ 11.6 AS-REP Roasting
□ 11.7 DCSync
□ 11.8 Pass-the-Hash
□ 11.9 Pass-the-Ticket
□ 11.10 Golden Ticket
□ 11.11 Silver Ticket
□ 11.12 Delegaciones
□ 11.13 ACLs y ACEs
□ 11.14 Trusts
□ 11.15 Ataques a GPO
Ejercicios
Nivel 1 — Básico:

Monta un laboratorio AD (Windows Server + 2 clientes).

Enumera AD con net y PowerShell.

Usa BloodHound para mapear el dominio.

Nivel 2 — Intermedio:

Kerberoasting contra un servicio.

AS-REP Roasting contra usuarios sin preauth.

Pass-the-Hash en laboratorio.

Nivel 3 — Avanzado:

DCSync para obtener hashes del dominio.

Golden Ticket y persistencia.

Ataque a delegaciones.

Máquinas AD de HTB (Forest, Sauna, Blackfield).

Recursos: "Active Directory Security" (adsecurity.org), CRTP, HackTricks AD.

<a name="tema-12"></a>

Tema 12: Evasión y Payloads
Objetivo: Evadir antivirus y EDR.

Subtemas
□ 12.1 Ofuscación de payloads
□ 12.2 Encoding y encryption
□ 12.3 Shellcode
□ 12.4 Inyección de procesos
□ 12.5 AMSI bypass
□ 12.6 PowerShell ofuscado
□ 12.7 Living off the Land (LOLBins)
□ 12.8 Evasión de EDR
Ejercicios
Nivel 1 — Básico:

Ofusca un script PowerShell.

Codifica un payload en base64.

Usa LOLBins para ejecutar comandos.

Nivel 2 — Intermedio:

Bypass de AMSI.

Inyección de shellcode en proceso.

Payload con msfvenom ofuscado.

Nivel 3 — Avanzado:

Evade Windows Defender con payload custom.

Ejecuta shellcode en memoria sin tocar disco.

Bypass de EDR (en laboratorio).

Recursos: "Evading EDR" (Matt Hand), "Red Team Development and Operations".

<a name="tema-13"></a>

Tema 13: C2 Frameworks
Objetivo: Gestionar múltiples agentes comprometidos.

Subtemas
□ 13.1 Cobalt Strike
□ 13.2 Sliver
□ 13.3 Mythic
□ 13.4 Havoc
□ 13.5 Beacons y listeners
□ 13.6 Pivoting con C2
Ejercicios
Nivel 1 — Básico:

Instala Sliver y crea un beacon.

Conecta un agente a tu C2.

Nivel 2 — Intermedio:

Sliver: movimiento lateral.

Cobalt Strike (versión community o trial).

Configura listeners HTTPS.

Nivel 3 — Avanzado:

C2 con dominio fronting.

Redirectores con Nginx.

Malleable C2 profiles.

Recursos: Documentación oficial de Sliver, Cobalt Strike, Mythic.

<a name="tema-14"></a>

Tema 14: Exploit Development
Objetivo: Escribir exploits propios.

Subtemas
□ 14.1 Assembly x86/x64
□ 14.2 Buffer overflow en Linux
□ 14.3 Buffer overflow en Windows
□ 14.4 Shellcode development
□ 14.5 ROP chains
□ 14.6 Heap exploitation
□ 14.7 Format string
□ 14.8 UAF
Ejercicios
Nivel 1 — Básico:

Buffer overflow básico en Linux.

Escribe shellcode que ejecute /bin/sh.

Nivel 2 — Intermedio:

Buffer overflow con ASLR y NX.

ROP chain básico.

Bypass de stack canary.

Nivel 3 — Avanzado:

Heap exploitation.

UAF con bypass de mitigaciones.

Exploit para un CVE público.

Recursos: "Hacking: The Art of Exploitation", "The Shellcoder's Handbook", pwn.college.

<a name="tema-15"></a>

Tema 15: Reversing
Objetivo: Analizar binarios y malware.

Subtemas
□ 15.1 Ghidra
□ 15.2 IDA Pro
□ 15.3 x64dbg
□ 15.4 Análisis estático
□ 15.5 Análisis dinámico
□ 15.6 Análisis de malware
□ 15.7 Anti-debugging
□ 15.8 Packing y unpacking
Ejercicios
Nivel 1 — Básico:

Analiza un binario simple con Ghidra.

Identifica funciones principales.

Nivel 2 — Intermedio:

Analiza malware simple (en VM aislada).

Bypass anti-debugging.

Unpack de un binario con UPX.

Nivel 3 — Avanzado:

Analiza ransomware de muestra pública.

Escribe un unpacker propio.

Reversea un crackme complejo.

Recursos: "Practical Malware Analysis", "Practical Reverse Engineering", MalwareUnicorn.

<a name="tema-16"></a>

Tema 16: Cloud Red Team
Objetivo: Comprometer entornos cloud.

Subtemas
□ 16.1 AWS
□ 16.2 Azure
□ 16.3 GCP
□ 16.4 IAM
□ 16.5 S3 buckets mal configurados
□ 16.6 Metadata service (SSRF)
□ 16.7 Kubernetes
□ 16.8 Docker escape
Ejercicios
Nivel 1 — Básico:

Crea cuenta AWS free tier.

Configura IAM con permisos mínimos.

Detecta un bucket S3 público.

Nivel 2 — Intermedio:

CloudGoat: labs de AWS.

Explota metadata service.

Enumera permisos IAM.

Nivel 3 — Avanzado:

Kubernetes Goat.

Escape de contenedor Docker.

Red team completo en cloud.

Recursos: CloudGoat, Flaws.cloud, Kubernetes Goat, HackTricks Cloud.

<a name="fase-4"></a>

FASE 4: MAESTRÍA (12+ meses)
Certificaciones Red Team
□ eJPT (entry)
□ PNPT (entry)
□ CRTP (AD)
□ CRTO (C2)
□ OSCP (pentest)
□ OSEP (evasión)
□ OSED (exploit dev)
□ OSEE (experto)
□ GXPN (SANS)
Actividades de maestría
□ Publicar CVEs
□ Escribir herramientas open source
□ Dar charlas en conferencias
□ Escribir blog técnico
□ Mentoría a otros
□ Bug bounty activo
□ CTFs regulares

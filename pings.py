#Autor poorboy
#Modulos a importar
from requests import get, exceptions
import socket as s
import nmap
from art import *

#Ascii art
tprint("Bienvenido", font="random")

#Decorador
def decor(func):
    def wrap():
        print("===================================")
        func()
        print("===================================")
    return wrap

#Codigo para averiguar la ip
def print_text():
    print("Ingrese la pagina para analizar")

decorated = decor(print_text)
decorated()

host = input("")

print("Esta es la direccion ip del sitio " + host)
print(f'of {host} is {s.gethostbyname(host)}')
print("=========================================")
print("")

#Codigo para encontrar el dns activo
def check_internet_connection():
    try:
        print("Ingrese la pagina completa (http o https): ")
        print("")
        get(input(''),  timeout = 30)
        print('El servidor esta conectado')
    except exceptions.ConnectionError:
        print('El servidor no conectado')
check_internet_connection()

print("")

print("Escaner de puertos")

nm=nmap.PortScanner()

ip=input("IP: ")
nm.scan(hosts=ip, arguments="--top-ports 65535 -sV --version-intensity 3")
print("")
print("comando ejecutado: {}".format(nm.command_line()))

print("Protocolos utilizados: {}".format(nm[ip].all_protocols()))

print("Estado de la maquina: {}".format(nm[ip].state()))

print("Puertos abiertos")
for puerto in nm[ip]['tcp'].keys():
	print(puerto)


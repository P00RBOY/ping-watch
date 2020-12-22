#Autor poorboy
#Modulos a importar
from requests import get, exceptions
from tabulate import tabulate
import socket as s
from pyfiglet import Figlet
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
print("=========================================")
print("")
print(f'of {host} is {s.gethostbyname(host)}')

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
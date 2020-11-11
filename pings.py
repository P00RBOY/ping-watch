#Autor julio

def decor(func):
    def wrap():
        print("===============")
        func()
        print("===============")
    return wrap

def print_text():
    print("Chequer de ping")

decorated = decor(print_text)
decorated()

from requests import get, exceptions
import socket as s

print("Ingrese la pagina: ")
host = input()

print("Esta es la direccion ip del sitio " + host)
print(f'of {host} is {s.gethostbyname(host)}')


def check_internet_connection():
    try:
        print("Ingrese la pagina o el host: ")
        get(input(''),  timeout =10)
        print('El servidor esta conectado')
    except exceptions.ConnectionError:
        print('El servidor no conectado')

check_internet_connection()
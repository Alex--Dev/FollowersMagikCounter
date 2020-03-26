#! /usr/bin/env python3.6
from platform import system
if system == 'Windows':
    from msvcrt import getch
else:
    from getch import getch #require haber instalado getch mediante pip

def leerDatos():
    print('\nUsuarios:\n')
    with open("datos", 'r') as f:
        dato = f.readline()
        while dato != '':
            print(dato, end='')
            dato = f.readline()
    print()

def escribirDato():
    print('\nEscriba el usuario a añadir: ')
    newUser = input()
    with open("datos", 'a') as f:
        f.write (newUser)
        f.write('\n')
    print('Añadido\n')

def buscarUsuario():
    print('\nBuscar usuario:')
    user = input()
    with open("datos", 'r') as f:
        encontrado = False
        dato = f.readline().split()[0]
        while dato != '':
            if dato == user:
                print("El usuario ya se encuentra en la lista\n")
                encontrado = True
                break
            else:
                dato = f.readline().split()[0]
        if not encontrado:
            print('El usuario NO se encuentra en la lista\n')

if __name__ == '__main__':
    print('FOLLOWERS TWITTER\n')
    opcion = 4
    #Display MENU
    while opcion != 0:
        print('Pulse 1 para mostrar la lista de usuarios')
        print('Pulse 2 para añadir un nuevo user a la lista')
        print('Pulse 3 para buscar un usuario en la lista')
        print('Para salir pulse 0')
        opcion = int (getch())
        switcher  = {
            0: lambda: 0, #salir
            1: leerDatos,
            2: escribirDato,
            3: buscarUsuario
        }
        switcher[opcion]()

    print('¡Hasta Luego!')

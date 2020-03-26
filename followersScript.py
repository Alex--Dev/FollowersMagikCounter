import msvcrt

def leerDatos():
    with open("datos", 'r') as f:
        dato = f.readline()
        while dato != '':
            print(dato, end='')
            dato = f.readline()

def escribirDato(newUser):
    with open("datos", 'a') as f:
        f.write (newUser)
        f.write('\n')

def buscarUsuario(user):
        with open("datos", 'r') as f:
            encontrado = False
            dato = f.readline()
            while dato != '':
                if dato == user
                    print("El usuario ya se encuentra en la lista")
                    encontrado = True
                else
                    dato = f.readline()
            if !encontrado:
                print('El usuario no se encuentra en la lista')


if __name__ == '__main__':
    print('FOLLOWERS TWITTER\n')
    opcion = 4
    #Display MENU
    while opcion != 0:
        print('Pulse 1 para mostrar la lista de usuarios')
        print('Pulse 2 para añadir un nuevo user a la lista')
        print('Pulse 3 para buscar un usuario en la lista')
        print('Para salir pulse 0')
        opcion = int (msvcrt.getche())
        switcher  = {
            0: #salir
            1: leerDatos()
            2: escribirDato()
            3: buscarUsuarios()
        }
        if opcion == 1:
            print('\n')
            leerDatos() 
        elif opcion == 2:
            print('Escriba el usuario a añadir: ')
            newUser = input()
            escribirDato(newUser)
        print('\n')
    print('¡Hasta Luego!')

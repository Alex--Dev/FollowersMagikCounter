import msvcrt

def leerDatos():
    with open("datos", 'a') as f:
        dato = f.readline()
        while dato != '':
            print(dato, end='')
            dato = f.readline()


def escribirDato(newUser):
    with open("datos", 'a') as f:
        f.write (newUser)

if __name__ == '__main__':
    print('FOLLOWERS TWITTER\n')
    opcion = 4
    #Display MENU
    while opcion != 0:
        print('pulse 1 para buscar un user en la lista')
        print('Pulse 2 para añadir un nuevo user a la lista')
        print('Para salir pulse 0')
        opcion = int (msvcrt.getche())
        if opcion == 1:
            leerDatos() #De momento MUESTRA POR PANTALLA
        elif opcion == 2:
            print('Escriba el usuario a añadir: ')
            newUser = msvcrt.getche()
            escribirDato(newUser) #TODO: implementar paso parametro
        print('\n')
    print('¡Hasta Luego!')

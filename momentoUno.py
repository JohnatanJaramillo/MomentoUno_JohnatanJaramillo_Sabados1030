usuarios = []
bicicletas = [1,2,3,4,5,6]
prestamos = []


def agregarUsuarios():   
    tarjeta = input("Ingrese su número de tarjeta: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo electrónico: ")
    nuevoUsuario = [tarjeta,nombre,apellido,correo]
    usuarios.append(nuevoUsuario)

def prestamoCicla():
    bandera = False
    bicicleta = ""
    control2 = 0
    while control2 == 0:
        tarjetaPrestamo = input("Ingrese su número de tarjeta: ")
        for i in range(0,len(usuarios)):
            usuario = usuarios[i]
            if tarjetaPrestamo in usuario:
                i = len(usuarios)
                bandera = True
            else:
                bandera = False
        if bandera :
            control3 = 0
            while control3 == 0:
                print("Seleccione una Cicla")
                print("1. Cicla 1.")
                print("2. Cicla 2.")
                print("3. Cicla 3.")
                print("4. Cicla 4.")
                print("5. Cicla 5.")
                print("6. Cicla 6.")
                bicicleta = input("Ingrese el número de su elección: ")
                bicicletaInt = int(bicicleta)
                if bicicletaInt < 7 and bicicletaInt > 0:
                    if bicicletaInt in bicicletas:                   
                        bicicletas.remove(bicicletaInt)
                        control3 = 1
                    else:
                        print("")
                        print("Cicla no disponible")
                        print("")
                        control3 = 0
                else:
                    print("Ingrese una opción valida")
            origen = input("Ingrese el origen: ")
            destino = input("Ingrese su destino: ")
            control2 = 1
        else:
            print("")
            print("El numero de la tarjeta no esta registrada")
            print("")
            control2 = 0
            menuPpal()
        nuevoPrestamo = [tarjetaPrestamo, bicicleta, origen, destino]
        prestamos.append(nuevoPrestamo)
    



def listarUsuarios():
    for i in range(0, len(usuarios)):
        usuario = usuarios[i]
        for j in range(0, len(usuario[j])):
            print("")
            print(f"Usuario No.  {j + 1}")
            print(f"No tarjeta : {usuario[0]}")
            print(f"Nombre : {usuario[1]}")
            print(f"Apellido : {usuario[2]}")
            print(f"Correo : {usuario[3]}")
            print("")

def listarPrestamos():
    for i in range(0, len(prestamos)):
        prestamo = prestamos[i]
        for j in range(0, len(prestamo[j])):
            print("")
            print(f"Prestamo No.  {i + 1}")
            print(f"No tarjeta : {prestamo[0]}")
            print(f"Bicicleta : {prestamo[1]}")
            print(f"Origen : {prestamo[2]}")
            print(f"Destino : {prestamo[3]}")
            print("")

def menuPpal():
    control = 0
    while control == 0:
        print("")
        print("----Sistema de prestamos de ciclas-----")
        print("---------------------------------------")
        print("-------------Bienvenido----------------")
        print("1. Registrar usuario.")
        print("2. Realizar prestamo.")
        print("3. Listar Usuarios.")
        print("4. Listar Prestamos.")
        print("5. Salir.")
        opcion = input("Digite el número de la opción deseada: ")
        print("")
        if opcion == "1":
            agregarUsuarios();
        elif opcion == "2":
            prestamoCicla();
        elif opcion == "3":
            listarUsuarios();
        elif opcion == "4":
            listarPrestamos();
        elif opcion == "5":
            control = 1
        else:
            print("Digite una opción valida")

menuPpal()
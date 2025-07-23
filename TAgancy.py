def Menu():
    print("Bienvenido a la agencia de viajes Bing Bong")
    print("1.Agregar clientes")
    print("2.Listado de clientes y destinos")
    print("3.Total de destinos visitados")
    print("4.Cliente con más destinos")
    print("5.Salir")
allow = False
clients = {}
cont = 0
try:
    while allow == False:
        Menu()
        opt = int(input("Ingrese la opción que desee: "))
        match opt:
            case 1:
                number = int(input("Cuantos clientes desea ingresar?"))
                if number <= 0 or number >100:
                    print("La cantidad ingresada no es valida")
                else:
                    for i in range(number):
                        C_code = f"CL+{cont}"
                        name = input("Ingrese el nombre del cliente: ")
                        traveln = int(input("Ingrese cuántos destinos desea ingresar: "))
            case 2:
                print("Ver")
            case 3:
                print("Ver")
            case 4:
                print("Ver")
            case 5:
                print("Bing Bong le agradece por utilizar el programa")
                break
            case _:
                print("La opción seleccionada no es valida")
except ValueError:
    print("Error, el tipo de dato ingresado no coincide")
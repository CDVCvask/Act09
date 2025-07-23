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
cont1 = 0
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
                        clients[C_code] = {}
                        name = input("Ingrese el nombre del cliente: ")
                        clients[C_code]["name"] = name
                        traveln = int(input("Ingrese cuántos destinos desea ingresar: "))
                        if traveln <= 0 or traveln >5:
                            print("La cantidad ingresada no es valida")
                        else:
                            for i in range(traveln):
                                D_code = f"D+{cont1}"
                                destiny = input(f"Ingrese el destino no.{i}")
                                clients[D_code]["destiny"][D_code] = {destiny}
                                cont1 = cont1 + 1
                        cont = cont + 1
            case 2:
                show_c = 0
                for code, value in clients.items():
                    print(f"Cliente {show_c}")
                    print(f"Código de cliente: {code}")
                    print(f"Nombre del cliente: {value['name']}")
                    print("Destinos del cliente")
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
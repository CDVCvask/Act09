def Menu():
    print(" ")
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
                number = int(input("Cuantos clientes desea ingresar? "))
                if number <= 0 or number >100:
                    print("La cantidad ingresada no es valida")
                else:
                    for i in range(number):
                        C_code = f"CL{cont}"
                        clients[C_code] = {}
                        name = input("Ingrese el nombre del cliente: ")
                        clients[C_code]["name"] = name
                        clients[C_code]["Destiny"] = {}
                        traveln = int(input("Ingrese cuántos destinos desea ingresar: "))
                        if traveln <= 0 or traveln >5:
                            print("La cantidad ingresada no es valida")
                        else:
                            for i in range(traveln):
                                D_code = f"DY{cont1}"
                                destiny = input(f"Ingrese el destino no.{i+1}: ")
                                clients[C_code]["Destiny"][D_code] = {"destination": destiny}
                                cont1 = cont1 + 1
                        cont = cont + 1
                    print(" ")
            case 2:
                show_c = 1
                for code, value in clients.items():
                    des_c = 1
                    print(" ")
                    print(f"Cliente {show_c}")
                    print(f"Código de cliente: {code}")
                    print(f"Nombre del cliente: {value['name']}")
                    print(f"Destinos del cliente {show_c}")
                    for code, value in value["Destiny"].items():
                        print(f"Destino {des_c}: {value['destination']}")
                        des_c = des_c + 1
                    show_c = show_c + 1
                print(" ")

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
def Menu():
    print(" ")
    print("Bienvenido a la agencia de viajes Bing Bong")
    print("1.Agregar clientes")
    print("2.Listado de clientes y destinos")
    print("3.Total de destinos visitados")
    print("4.Cliente con más destinos")
    print("5.Salir")
def Total_Des(Clients, N, Tot):
    keys = list(Clients.keys())
    if N == len(keys):
        return Tot
    else:
        current_client = Clients[keys[N]]
        for destiny in current_client["Destiny"].values():
            Tot += destiny["Quantity"]
        return Total_Des(Clients, N + 1, Tot)
def Most(Clients,N,High,client_code):
    Cont = 0
    keys = list(Clients.keys())
    if N == len(keys):
        return client_code
    else:
        current_client = Clients[keys[N]]
        for destiny in current_client["Destiny"].values():
            Cont = Cont + destiny["Quantity"]
        if Cont > High:
            High = Cont
            client_code = keys[N]
            return Most(Clients, N + 1, High, client_code)
        else:
            return Most(Clients, N + 1, High, client_code)
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
                                clients[C_code]["Destiny"][D_code] = {"destination": destiny,"Quantity": 1}
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
                print(Total_Des(clients,0,0))
            case 4:
                print(Most(clients,0,0,0))
            case 5:
                print("Bing Bong le agradece por utilizar el programa")
                break
            case _:
                print("La opción seleccionada no es valida")
except ValueError:
    print("Error, el tipo de dato ingresado no coincide")
import os
import time
clear="cls"
opc=0
capacidad=530
PesoTotal=0
precioTotal=0
camiones=0
while True:
    while True:
        try:
            name=input("ingresa tu nombre(minimo 3 caracters):")
            longitudname=len(name)
            if longitudname >=3:
                print("se ha guardao correctamente tu nombre")
                time.sleep(2)
                os.system("cls")
                break
            else:
                print("ingresa un minimo de 3 caracteres")
                time.sleep(2)
                os.system("cls")
        except ValueError:
            print("ingresa el valor correcto")
            time.sleep(2)
            os.system("cls")
    while True:
            try:
                telef=input("ingresa tu nomero telefonico (minimo 8 digitos y max 9):")
                longitudtelef=len(telef)
                if longitudtelef <=9 and longitudtelef >=8:
                    time.sleep(2)
                    os.system("cls")
                    print("se ha guardado correctamente tu telefono")
                    time.sleep(2)
                    os.system("cls")
                    break
                else:
                    print("ingresa minimo 8 digitos y maximo 9")
                    time.sleep(2)
                    os.system("cls")
            except ValueError:
                print("ingresa el valor correcto")
    while True:
        try:
            print("1.Compra camion estandar")
            print("2.Compra entrega especifica")
            print("3.Continuar(boleta)")
            opc=int(input("ingresa la opcion que deseas:"))
            time.sleep(2)
            os.system("cls")
            if opc==1:
                camiones=int(input("Ingresa la cantidad de camiones que desea:"))
                time.sleep(2)
                os.system("cls")
                PesoTotal=(capacidad*camiones)
                precioTotal=(14310000*camiones)
            elif opc==2:
                while True:
                        print("1.Catlove")
                        print("2.DogPremium")
                        print("3.CatElitePlus")
                        print("4.Continuar")
                        opc=int(input("ingresa una opcion del 1 al 4"))
                        if opc==1:
                                sacos=int(input("ingresa la cantiada de sacos que desea:"))
                                PesoTotal+=(sacos)
                                precioTotal+=(28750 + 250000)
                                time.sleep(2)
                                os.system("cls")
                        elif opc==2:
                                sacos=int(input("ingresa la cantiada de sacos que desea:"))
                                PesoTotal+=(sacos)
                                precioTotal+=(28750 + 250000)
                                time.sleep(2)
                                os.system("cls")
                        elif opc==3:
                                sacos=int(input("ingresa la cantiada de sacos que desea:"))
                                PesoTotal+=(sacos)
                                precioTotal+=(28750+250000)
                                time.sleep(2)
                                os.system("cls")
                        elif opc==4:
                                print("saliendo al menu")
                                time.sleep(2)
                                os.system("cls")
                                break
            elif opc==3:
                    print("continuando hacia la boleta...")
                    time.sleep(2)
                    os.system("cls")
                    break
        except ValueError:
            print("ingresa una opcion del 1 al 3")
    PesoTotal=(PesoTotal)
    precioTotal=(precioTotal)
    CamionesTotal=(camiones)
    print("*"*30)
    print("boleta")
    print(f"Cliente:¨{name}")
    print(f"telefono:{telef}")
    print(f"Cantidad de kilos:{PesoTotal}")
    print(f"camiones:{CamionesTotal}")
    print(f"Valor Total:{precioTotal}")
    continuar=int(input("Si quieres realizar otra compra inhresa la opcion1. Si no ingresa la opcion 2:"))
    time.sleep(2)
    os.system("cls")
    if continuar==1:
         import os
         import time
         clear="cls"
         opc=0
         capacidad=530
         PesoTotal=0
         precioTotal=0
    elif continuar==2:
         print("Vuelva pronto :)")
         break
         
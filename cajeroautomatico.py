                                            ##CAJERO AUTOMATICO



saldo=1000

def consultar_saldo():
    global saldo
    print(f'Tu saldo es: {float(saldo)} $. \n')
    

def retirar_dinero(r):
    global saldo
    if r <= saldo:
        saldo -= r
        print(f'Retiraste {r} $.\n')
        print(f'Te queda: {saldo} $. \n')
    else:
        print('No cuentas con el dinero suficiente \n')

def depositar_dinero(d):
    global saldo
    saldo += d
    print('Deposito Realizado con exito.')
    print(f'Su saldo es: {saldo} $.\n')


while True:
    try:
        print('***************************************')
        print('* Bienvenido a cajero automarico EMIL *')
        print('***************************************')
        print('1. Consultar Saldo')
        print('2. Retirar dinero')
        print('3. Depositar dinero')
        print('4. Salir')
        opcion = int(input('Que desea realizar: '))
        if opcion==1:
            consultar_saldo()
        elif opcion==2:
            r=float(input('Cuanto dinero desea retirar: '))
            retirar_dinero(r)
        elif opcion==3:
            d= float(input('Cuanto dinero desea depositar: '))
            depositar_dinero(d)
        elif opcion==4:
            print('Gracias por usar mi banco, vuelve pronto.')
            break  
        else:
            print('Opción invalida, ingresa una opcion disponible.')
        
    except ValueError:
        print('Error, ingresa un valor numérico \n')
    
    





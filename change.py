def change():
        expense = 23.75
        money = 100
        print("Ingresar gasto:")
        print(expense)
        print("Dinero recibido")
        print(money)
        print("")       
        print("Vuelto")
        print("")       

        vuelto = money - expense
        pesos = int(vuelto)
        centavos = round((vuelto - pesos) * 100)

        print("Pesos:")
        print(str(pesos))
        print("Centavos:")
        print(str(centavos))


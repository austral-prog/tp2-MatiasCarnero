def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)  
    centavos = round((vuelto - pesos) * 100)
    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)


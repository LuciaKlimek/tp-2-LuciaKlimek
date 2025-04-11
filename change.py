def change():
    expense = 23.75
    money = 100
    message = "Gasto"
    message_2 = "Dinero recibido"
    message_3 = "Vuelto"
    vuelto = money - expense
    vuelto_pesos = int(vuelto)
    vuelto_centavos = int((vuelto - vuelto_pesos)*100)
    print(message)
    print(expense)
    print(message_2)
    print(money)
    print("")
    print(message_3)
    print(vuelto)
    print("")
    print("Pesos:")
    print(vuelto_pesos)
    print("Centavos:")
    print(vuelto_centavos)

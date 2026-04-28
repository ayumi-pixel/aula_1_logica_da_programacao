while True:
    num = int(input("Digite qual tabuada você quer: "))
    if num == 0:
        print("Programa encerrado.")
        break
    minimo = int(input("Digite qual o valor mínimo a ser calculado: "))
    maximo = int(input("Digite qual o valor maximo a ser calculado: "))
    print("Tabuada de", num, "de", minimo, "a", maximo)
    i = minimo
    for i in range(minimo, maximo + 1):
        restante = i%2
        if restante == 0:
             print(i, "é par")
        else:
            print(i, "é impar")
        res = num * i
        print(num, "x", i, "=", res)
        i += 1
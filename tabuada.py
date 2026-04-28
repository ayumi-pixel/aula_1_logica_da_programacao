while True:
    try:
        numero = int(input("Digite a tabuada (0 para sair): "))
    except ValueError:
        print("Por favor, digite um número inteiro.")
        continue

    if numero == 0:
        print("Programa encerrado.")
        break

    try:
        minimo = int(input("Digite o valor mínimo: "))
        maximo = int(input("Digite o valor máximo: "))
    except ValueError:
        print("Por favor, digite valores inteiros para o mínimo e o máximo.")
        continue

    if minimo > maximo:
        print("O valor mínimo deve ser menor ou igual ao valor máximo.")
        continue

    print(f"Tabuada de {numero} de {minimo} até {maximo}:")
    i = minimo
    while i <= maximo:
        print(f"{numero} x {i} = {numero * i}")
        i += 1
    print()
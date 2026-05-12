L = []
print(L)
print("================================================")
L1 = [0] * 5
print(L1)
print("================================================")
L2 = [0, 0, 0, 0, 0]
print(L2)
print("================================================")
L3 = [0 * 5]
print(L3)
print("================================================")
L4 = [1, 2, 3, 4, 5]
print(L4)
print("================================================")
L5 = [1, 2, 3, 4, 5]
print(L5[3]) #É PARA MOSTRAR O ELEMENTO DE ÍNDICE 3, QUE É O NÚMERO 4
print("================================================")
L5[3] = 10 #ALTERA O ELEMENTO DE ÍNDICE 3 PARA O NÚMERO 10
print(L5)
print("================================================")
L6 = list(range(1, 11)) #CRIA UMA LISTA COM OS NÚMEROS DE 1 A 10
print(L6)
print("================================================")
L7 = list(range(0, 21, 2)) #CRIA UMA LISTA COM OS NÚMEROS PARES DE 0 A 20
print(L7)
print("================================================")
L8 = list(range(1, 21, 2)) #CRIA UMA LISTA COM OS NÚMEROS ÍMPARES DE 1 A 20
print(L8)
print("================================================")
L9 = list(range(10, 0, -1)) #CRIA UMA LISTA COM OS NÚMEROS DE 10 A 1
print(L9)
print("================================================")
L10 = list(range(0, -11, -1)) #CRIA UMA LISTA COM OS NÚMEROS DE 0 A -10
print(L10)
print("================================================")
L11 = list("TSI")
print(L11)
print("================================================")
L12 = list("TSI" + "TERMO")
print(L12)
print("================================================")
L13 = []
L13.append(int(input('Digite um número inteiro para adicionar à lista: '))) #ADICIONA UM NÚMERO INTEIRO À LISTA L13
print(L13)
print("================================================")
L13.insert(0,80) #INSERE O NÚMERO 80 NA POSIÇÃO DE ÍNDICE 0 DA LISTA L13
print(L13)
print("================================================")
from random import randint
L14 = []
for i in range(2):
    L14.append(randint(1, 40)) #ADICIONA 2 NÚMEROS INTEIROS ALEATÓRIOS ENTRE 1 E 40 À LISTA L14
print(L14)
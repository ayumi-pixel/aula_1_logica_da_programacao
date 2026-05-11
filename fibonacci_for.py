n = int(input('Digite um número inteiro para a posição da sequência Fibonacci: '))

if n <= 0:
    print('Digite um número inteiro maior que zero.')
else:
    fib = [0, 1]
    if n == 1:
        print('Sequência Fibonacci até a posição 1:')
        print(fib[0])
    else:
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])

        print(f'Sequência Fibonacci até a posição {n}:')
        for i in range(n):
            print(fib[i], end=' ')
        print()
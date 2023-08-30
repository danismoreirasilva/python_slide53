continuar = 's'
soma = 0
cont = 0
while continuar == 's':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1

    if cont == 1:
        maior = menor = num
    else:
        if num > maior: maior = num
        if num < menor: menor = num

    while True:
        continuar = str(input('Deseja continuar: s ou n: ')).lower()
        if continuar != 's' and continuar != 'n':
            print('Resposta incorreta. Digite s ou n!')
        else:
            break

else:
    if cont == 1:
        print(f'Foi digitado apenas um número: {num}')
    else:
        print(f'A média dos valores é: {soma / cont:.2f}!')
        print(f'O menor é: ({menor}) \nO maior é: ({maior})')
        print('Você saiu do programa!')

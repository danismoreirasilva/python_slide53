#validando dados de entrada (ainda sem verificar se de fato é um número)
valorInvalido = True
while valorInvalido:
    preco = float(input('Digite o preço do produto: '))
    if preco > 0:
        valorInvalido = False
    else:
        print(f'O preço do produto deve ser um valor positivo e maior do que zero!')
else:
    print(f'O produto terá um desconto de R$ {preco * (5/100):.2f}\nO valor a pagar é R$ {preco * 0.95:.2f}')

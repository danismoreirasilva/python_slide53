#validando dados de entrada (ainda sem verificar se de fato é um número)
valorInvalido = True
valorVazio = True

while valorVazio:
    nome = str(input('Digite o nome do funcionário: '))
    if len(nome) == 0 or nome.isspace():
        print(f'O nome do funcionário não pode ser vazio!')
    else:
        valorVazio = False

while True:
    salario = float(input('Digite o salario R$: '))
    if salario > 0:
        print(f'O funcionário {nome.title()} terá 15% de aumento!\nSeu novo salário é de R$ {salario * 1.15:.2f}')
        break
    else:
        print(f'O salário deve ser um valor positivo e maior do que zero!')



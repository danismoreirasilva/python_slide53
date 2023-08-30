#com validação de dados

'''notasInvalidas = True
while notasInvalidas:
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
        notasInvalidas = False
    else:
        print(f'Os valores válidos de notas são entre 0 e 10!')'''

nota1 = nota2 = -1
while not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
        print(f'Os valores válidos de notas são entre 0 e 10!')

media = (nota1 + nota2) / 2

if media >= 6:
    print(f'Aluno aprovado com média {media:.2f}!')
else:
    print(f'Aluno reprovado com média {media:.2f}!')
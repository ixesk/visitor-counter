# Informações; Numero de visitantes/Cidades
# import collections
from collections import Counter

cmd = input("Digite 'entrar' ou 'sair': ")
cidades = []

if cmd == 'entrar':
    while cmd != 'sair':

        cmd1 = input("Digite 'info', 'contar' ou 'sair': ")

        if cmd1 == 'contar':
            cmd2 = input('Pressione enter: ')

            while cmd2 != 'sair':
                cmd2 = input('Digite o nome da sua cidade: ')

                if cmd2 != 'sair':
                    cidades.append(cmd2)
                    print('Registrado com sucesso.')

                if cmd2 == 'sair':
                    print('Saiu com sucesso.')
                    break

        if cmd1 == 'info':
            c = Counter(cidades)
            for chave, valor in c.items():
                print(f'{chave}: {valor}')
            print(f'Numero de visitantes totais: {len(cidades)}')
            print(f'Numero de cidades distintas: {len(set(cidades))}')

        if cmd1 == 'sair':
            print(f'Numero de visitantes totais: {len(cidades)}')
            print('Saiu com sucesso.')
            break

if cmd == 'sair':
    print('Saiu com sucesso.')

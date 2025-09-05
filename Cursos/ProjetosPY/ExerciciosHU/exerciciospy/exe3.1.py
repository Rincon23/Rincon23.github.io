"""
Escreva um programa que leia os nomes de três pessoas de uma família: mãe, pai e criança. O
programa deve exibir na tela a mensagem.

"Os adultos {mãe} e {pai} são os responsáveis por {criança}"

Faça de dois modos: com o método .format() e com f-string
"""

mae = input('Nome da Mãe: ')
pai = input('Nome da pai: ')
crianca = input('Nome da criança: ')

print(f'Os adultos {mae} e {pai} são os responsáveis por {crianca}')
print('Os adultos {} e {} são os responsáveis por {}'.format(mae, pai, crianca))
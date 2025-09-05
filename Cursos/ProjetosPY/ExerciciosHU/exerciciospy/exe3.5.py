"""
Enunciado: Escreva um programa que leia um número inteiro que representa uma quantidade de tempo em
segundos. Calcule e mostre na tela a quantidade de horas, minutos e segundos.

Exemplos:   Entrada (segundos)              Saída
            1                               0 hora(s), 0 minuto(s), 1 segundo(s)
            38                              0 hora(s), 0 minuto(s), 38 segundo(s)
            746                             0 hora(s), 12 minuto(s), 26 segundo(s)
            4578                            1 hora(s), 16 minuto(s), 18 segundo(s)
            73551                           20 hora(s), 25 minuto(s), 51 segundo(s)

Dicas: Leve em consideração que 1 hora tem 3600 segundos e 1 minuto tem 60 segundos.
Use os operadores de divisão de inteiros (//) e resto (%).
"""

t = int(input('Digite uma quantidade de tempo em segundos: '))

h = t // 3600
m = t % 3600 // 60
s = t % 3600 % 60 

print(f'{h} hora(s), {m} minuto(s), {s} segundo(s)')



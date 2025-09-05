"""
Enunciado: Quando uma pessoa ou uma empresa realiza um investimento espera-se um retorno positivo (lucro),
embora também possa ocorrer um retorno negativo (prejuízo). Uma forma inicial de avaliar o retorno
é conhecida com Retorno sobre Investimento (ou ROI, uma sigla em inglês). Cálculo do ROI:

ROI =  Receita-(Custos+𝐼𝑛𝑣𝑒𝑠𝑡𝑖𝑚𝑒𝑛𝑡𝑜)
        ----------------------------       . 100%
            Custos+𝐼𝑛𝑣𝑒𝑠𝑡𝑖𝑚𝑒𝑛𝑡𝑜            

Escreva um programa que leia 3 dados de entrada reais: Investimento, Custos e Receita, calcule o
ROI usando a fórmula acima e exiba o resultado com uma casa decimal no formato mostrado abaixo.

Exemplo: Investimento = 2300.00 - Custos = 345.73 - Receita = 2712,17

Saída: ROI = 2.5%
"""

I = float(input('Digite o valor do investimento: '))
C = float(input('Digite o valor do custo: '))
R = float(input('Digite o valor da receita: '))

ROI = ((R-(C+I))/(C+I))*100

print(f'O ROI foi de: {ROI:.1f}%')

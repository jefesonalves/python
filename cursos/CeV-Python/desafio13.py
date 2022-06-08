# Desafio 13 do Curso em Vídeo

salario = float(input('Digite o preço de venda do produto: '))
margem_aumento = float(input('Digite a mergem de aumento em %: '))
valor_aumento = salario * margem_aumento / 100
valor_com_aumento = salario + valor_aumento

print('Salário inicial de R$ {:.2f} com o aumento de {:.2f}% ficou por R$ {:.2f}'.format(salario, margem_aumento, valor_com_aumento))
# Desafio 12 do Curso em Vídeo

preco = float(input('Digite o preço de venda do produto: '))
desconto = float(input('Digite o desconto em %: '))
preco_desconto = preco * desconto / 100
preco_com_desconto = preco - preco_desconto

print('Preço do produto R$ {:.2f} com o desconto de {:.2f}% ficou por R$ {:.2f}'.format(preco, desconto, preco_com_desconto))
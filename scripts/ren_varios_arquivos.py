import os

def mudar_nome_arquivos():
    os.system("clear")
    dir_atual = os.getcwd()
    print("Diretório atual: ", dir_atual)
    dir_informado = os.chdir(input("Informe o nome do diretório: "))
    quant_arquivos = int(len(os.listdir()))
    arquivos = (os.listdir())
    prefixo = input("Informe o prefixo: ")
    ext = "."+input("Informe a extensão do arquivo (ex: avi): ")

    for i in range(0, quant_arquivos, 1):           
        arquivo_antigo = arquivos[i]
        novo_arquivo = prefixo+f'{i:04d}'+ext
        os.rename(arquivo_antigo, novo_arquivo)

mudar_nome_arquivos()
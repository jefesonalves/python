import os

def mudar_nome_arquivos():
    os.system("clear")
    dir_atual = os.getcwd()
    print("Diretório atual: ", dir_atual, "\n")
    dir_atual = os.chdir(input("Informe o nome do diretório: "))
    dir_atual = os.getcwd() 
    print("\nDiretório alterado para: ", dir_atual, "\n")
    quant_arquivos = int(len(os.listdir()))
    arquivos = (os.listdir())
    prefixo = input("Informe o prefixo: ")
    ext = "."+input("Informe a extensão do arquivo (ex: avi): ")

    for i in range(0, quant_arquivos, 1):           
        processo = i + 1
        print("Processo:", processo)
        arquivo_antigo = arquivos[i]
        print("Nome atual:", arquivo_antigo)
        novo_arquivo = prefixo+f'{i:04d}'+ext
        print("Nome alterado para:", novo_arquivo)
        os.rename(arquivo_antigo, novo_arquivo)

mudar_nome_arquivos()
import os

def verificar_dir():
    dir_atual = os.getcwd()
    return dir_atual

def mudar_dir():
    dir_informado = os.chdir(input("Informe:"))
    return dir_informado

def contar_arquivos():
    quant_arquivos = int(len(os.listdir()))
    return quant_arquivos

def listar_arquivos():
    arquivos = (os.listdir())
    return arquivos

def definir_name(prefixo):
    for i in range(0, 10, 1):
        prefixo = prefixo+f'{i:04d}'
        return prefixo

mudar_dir()


# def prefixo_ext():
#     for i in range(0, 1001, 1):
#         prefix = input("Informe o prefixo: "+ f'MOVI{i:04d}')
#         ext = input("Informe a extensão: ")
#         print(prefix+ext)
        
#         print("# Processo:",file + 1)   
#         old_file = files[file]
#         print("Nome do arquivo original: "+old_file)
#         new_file = prefix+str(file)+ext
#         os.rename(old_file, new_file)
#         print("Arquivo renomeado para: "+new_file)
#         print("\n")
#         print("Arquivos renomeados!")


# diretorio()
# prefixo_ext()

 
# 
# 
# os.system("clear")

# for file in range(limit):
#     print("# Processo:",file + 1)   
#     old_file = files[file]
#     print("Nome do arquivo original: "+old_file)
#     new_file = prefix+str(file)+ext
#     os.rename(old_file, new_file)
#     print("Arquivo renomeado para: "+new_file)
#     print("\n")
# print("Arquivos renomeados!")
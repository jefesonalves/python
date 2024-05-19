import os

dir = input("Digite o diretório completo:")
os.chdir(dir)
files = (os.listdir(dir))
limit = int(len(files))
prefix = input("Digite o prefixo:")
ext = "."+input("Digite a extensão do arquivo:")
os.system("clear")

for file in range(limit):
    print("# Processo:",file + 1)   
    old_file = files[file]
    print("Nome do arquivo original: "+old_file)
    new_file = prefix+str(file)+ext
    os.rename(old_file, new_file)
    print("Arquivo renomeado para: "+new_file)
    print("\n")
print("Arquivos renomeados!")
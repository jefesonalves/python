import os
import platform

so = platform.system()
caminho = "\\arquivos.ufca.edu.br\Arquivos"
stxe1 = "net use * /delete /yes"
stxe2 = "net use Z: " + caminho

if so == "Windows":
		os.system(stxe1)
		os.system(stxe2)
elif so == "Linux":
	print ("Em desenvolvimento...")
else:
	print ("Sistema operacional deseconhecido...")


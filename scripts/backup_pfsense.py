# This Python file uses the following encoding: utf-8
'''
Script para realização de backup do Firewall pfsense
Desenvolvido por Jefeson Alves
e-mail: jefesonbezerra@gmail.com
Requisitos:
- Sistema operacional Linux;
- Cliente SCP;
- Usuário READ-ONLY no pfsense;
- SCP Habilitado no pfense;
'''

# Importando os módulo
import os 
import time
from datetime import datetime
from pathlib import Path

dir_backup = "~/backup_pfsense/"
 
if (os.path.exists(dir_backup) == True):
    print("O diretório existe!")
else:
    os.system("mkdir ~/backup_fgt/")
    print("Diretório criado!")

# Declaração de variáveis
porta = "22"
usuario = "" #definir
ip_pfsense = "192.168.1.18"
arquivo_firewall = "/cf/conf/config.xml"

scp -P + " " usuario+"@"+ip_pfsense+":"+arquivo_firewall+" "+dir_backup
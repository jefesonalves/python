# This Python file uses the following encoding: utf-8
# Script para reaalização de backup do Firewall Fortigate da Fortinet
# Desenvolvido por Jefeson Ales
# e-mail: jefesonbezerra@gmail.com
#
# Requisitos:
# - Cliente SCP
# - Usuário READ-ONLY no Fortigate
# - SCP Habilitado no Fortigate com o seguinte comando
# Fonte: http://kb.fortinet.com/kb/documentLink.do?externalID=12002

import os 
import time
from datetime import datetime

os.system("clear")
os.system("mkdir ~/backup_fgt/")
print ("------------------------------------")
print ("Script para backup do Fortigate.")
print ("Aguarde tres segundos...")
print ("------------------------------------")
time.sleep(3)

print ("----------------------------------------------")
print ("Preencha as informações relativas ao firewall:")
print ("----------------------------------------------")
siglalocal = input ("1. Digite a sigla da localidade: ").upper()
ipfwl = input ("2. Digite o endereço IP: ")
porta = input ("3. Digite a porta scp ")
usuario = input ("4. Digite o usuário: ")
caminho = ("~/backup_fgt/")

data = datetime.now().strftime('%d%m%Y_%H%M')

os.system("scp -P " + porta + " " + usuario + "@" + ipfwl + ":sys_config " + caminho + "FGT-" + siglalocal + data + ".conf")

# This Python file uses the following encoding: utf-8
'''
Script para realização de backup do Firewall Fortigate da Fortinet
Desenvolvido por Jefeson Alves
e-mail: jefesonbezerra@gmail.com
Requisitos:
- Sistema operacional Linux;
- Cliente SCP;
- Usuário READ-ONLY no Fortigate;
- SCP Habilitado no Fortigate;

Fonte: http://kb.fortinet.com/kb/documentLink.do?externalID=12002
'''

# Importando os módulo
import os 
import time
from datetime import datetime

os.system("clear") # Limpar a tela 
os.system("mkdir ~/backup_fgt/") # Criação do diretório backup_fgt
print ("----------------------------------------------")
print ("Preencha as informações relativas ao firewall:")
print ("----------------------------------------------")

# Declaração de variáveis
siglalocal = input ("1. Digite a sigla da localidade: ").upper() #Variável que armazena a localidade
ipfwl = input ("2. Digite o endereço IP: ") # Variável que armazena o endereço IP
porta = input ("3. Digite a porta scp: ") # Variável que armazena a porta do ssh
usuario = input ("4. Digite o usuário: ") # Variável que armazena a conta do usuário do fortigate
caminho = ("~/backup_fgt/") # Variável que armazena o caminho onde será salvo o backup
data = datetime.now().strftime('%d%m%Y_%H%M') # Variável que armazena o dia, mês, ano e horário atual

# Comando do linux para executar o backup utilizando as varíáveis declaradas
os.system("scp -P " + porta + " " + usuario + "@" + ipfwl + ":sys_config " + caminho + "FGT-" + siglalocal + data + ".conf")
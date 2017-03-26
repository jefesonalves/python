# This Python file uses the following encoding: utf-8
# Script para reaalização de backup do Firewall Fortigate da Fortinet
# Desenvolvido por Jefeson Ales
# e-mail: jefesonbezerra@gmail.com
#
# ----Em desenvolvimento----
# 
# Requisitos:
# - Cliente SCP
# - Usuário READ-ONLY no Fortigate
# - SCP Habilitado no Fortigate com o seguinte comando

import os

nomefwl = input ("Digite o nome ou localidade do Firewall: ")
ipfwl = input ("Digite o ip do Firewall: ")
porta = input ("Digite a porta ssh do Firewall: ")
usuario = input ("Digite o usuário do Firewall: ")
caminho = input ("Digite o local para armazenar o backup: ")
datahora = input ("Digite a data do backup (formato: ddmmaaaahhmm ")
os.system("scp " + "-p " + porta + " " + usuario + "@" + ipfwl + ":fgt-config:" + caminho + nomefwl + datahora + ".conf")

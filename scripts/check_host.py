# This Python file uses the following encoding: utf-8
# Script para checagem de host com ping
# Desenvolvido por Jefeson Alves
# e-mail: jefesonbezerra@gmail.com

import os, re

print ("-----------------------")
ipdestino = input ("Digite o endereço IP: ")
pacotes = input ("Digite a quantidade de pacote(s): ")
print ("Pingando " + pacotes + " pacote(s) no endereço IP: " + ipdestino)
stxe = "ping -w" + pacotes + " " + ipdestino
result = "".join(os.popen(stxe).readlines())

if bool(re.search ("100% packet loss", result)):
  print ("--------------------------")
  print ("#IP " + ipdestino + " Indisponível.")
  print ("--------------------------")
  print (" ")
else:
  if bool(re.search ("0% packet loss", result)):
    print ("----------------------------")
    print ("#IP " + ipdestino + " Disponível.")
    print ("----------------------------")
    print (" ")
  else:
    print ("----------------------------")
    print ("#IP " + ipdestino + " com perda de pacotes ou ip digitado errado.")
    print ("----------------------------")
    print (" ")
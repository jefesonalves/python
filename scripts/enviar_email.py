# This Python file uses the following encoding: utf-8
# Enviar e-mail com o servidor gmail
import smtplib

#Parâmetros
servidor = 'smtp.gmail.com'
porta = '587'
remetente = 'e-mail do remetente'
senha = 'senha do e-mail'
destinatario = 'e-mail do destinatário'
msg = 'Texto da mensagem a ser enviada'

server = smtplib.SMTP(servidor, porta)
server.starttls()
server.login(remetente, senha)
server.sendmail(remetente, destinatario, msg)
server.quit()

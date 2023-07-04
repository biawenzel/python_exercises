# import dos pacotes necessários
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando esse email com Python"

# parâmetros
senha = "xxxxxxxxx"
msg['From'] = "biahwenzel@gmail.com"
msg['To'] = "bia7_bia7@hotmail.com"
msg['Subject'] = "Assunto: Python"

# criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

# criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

# login na conta para envio
server.login(msg['From'], senha)

# envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

# encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso!')
# importar bibliotecas necessárias
from pywhatkit import sendwhatmsg
from keyboard import press_and_release
from time import sleep
from datetime import datetime

# definir para quais contatos enviar msgs
contatos = ['+5527988330280']
# definir intervalo de envio
while len(contatos) >= 1:
    # enviar mensagens
    sendwhatmsg(contatos[0], 'Testando automatização de mensagens com Python!!',
                datetime.now().hour, datetime.now().minute + 1)
    del contatos[0]
    sleep(15)
    press_and_release('ctrl + w')

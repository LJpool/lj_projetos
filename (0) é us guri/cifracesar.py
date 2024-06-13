def cifraMensagem(msg):
    msgCifrada = ''
    for i in range (len(msg)):
        code = ord(msg[i]) - 1
        msgCifrada = msgCifrada + chr(code)
    return msgCifrada

########################

msg = input('digete uma mensagem: ')

msgCifrada = cifraMensagem(msg)

print(msgCifrada)
senhacadastrada= '123'
senhadigitada = ''
tentativas= 0
acertouasenha= False

while (tentativas < 3 and acertouasenha == False):
    senhadigitada = input('digite a senha para entrar: ')
    tentativas = tentativas = + 1
    if (senhadigitada == senhacadastrada):
        acertouasenha = True
        print('senha correta. ')
    else:
        print('senha errada mané!!! vc posui mai', 3-tentativas,'tentativas!')
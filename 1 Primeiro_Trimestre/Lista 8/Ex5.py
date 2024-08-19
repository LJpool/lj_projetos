import re

def verificar_senha(senha):
    if not any(letra.isupper() for letra in senha):
        return False

    if not re.search(r'\d', senha) or not re.search(r'[*!$#]', senha):
        return False
    return True

senhas = ["Senha123*", "senha@123", "Senh@123", "SENHA123", "Senha123", "senha@#$%"]
for senha in senhas:
    if verificar_senha(senha):
        print(f"A senha '{senha}' é válida para cadastro.")
    else:
        print(f"A senha '{senha}' não é válida para cadastro.")
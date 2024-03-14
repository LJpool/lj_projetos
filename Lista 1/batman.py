def apresentar_questao(questao, alternativas):
    print(questao)
    for i, alternativa in enumerate(alternativas):
        print(f"{chr(97 + i)}) {alternativa}")

def verificar_resposta(resposta_correta, resposta_usuario):
    return chr(97 + resposta_correta) == resposta_usuario.lower()

def main():
    questao = "Qual é o verdadeiro nome do super-herói Batman?"
    alternativas = ["Bruce Wayne", "Clark Kent", "Peter Parker", "Tony Stark", "Steve Rogers"]
    resposta_correta = 0  # Resposta correta é a alternativa 'a'
    
    apresentar_questao(questao, alternativas)
    
    resposta_usuario = input("Digite a letra correspondente à sua resposta: ")
    
    if verificar_resposta(resposta_correta, resposta_usuario):
        print(f"Você respondeu alternativa {resposta_usuario}. A resposta correta é a alternativa a.")
    else:
        print(f"Você respondeu alternativa {resposta_usuario}. A resposta correta é a alternativa a.")

if __name__ == "__main__":
    main()

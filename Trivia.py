print("=== TRIVIA – DESENHOS E FILMES ===\n")

print("Escolha a dificuldade:")
print("1 - Fácil")
print("2 - Médio")
print("3 - Difícil")

dificuldade = input("Digite o número da dificuldade: ")

if dificuldade not in ["1", "2", "3"]:
    print("Dificuldade inválida. Vamos jogar no nível Fácil!\n")
    dificuldade = "1"

# -----------------------
# PERGUNTAS DO JOGO
# -----------------------

perguntas = [
    {
        "pergunta": "Quem é o dono do cachorro Pluto?",
        "opcoes": ["A) Pateta", "B) Pato Donald", "C) Mickey", "D) Minnie"],
        "correta": "C"
    },
     {
        "pergunta": "Qual princesa comeu uma maçã envenenada?",
        "opcoes": ["A) Cinderela", "B) Aurora", "C) Rapunzel", "D) Branca de Neve"],
        "correta": "D"
    },
     {
        "pergunta": "Qual desses personagens é o rei leão?",
        "opcoes": ["A) Timão", "B) Simba", "C) Scar", "D) Zazú"],
        "correta": "B"
    },
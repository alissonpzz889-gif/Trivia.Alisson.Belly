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
     {
        "pergunta": "Qual é o peixe-palhaço em Procurando Nemo?",
        "opcoes": ["A) Bruce", "B) Marlin", "C) Crush", "D) Dory"],
        "correta": "B"
    },
     {
        "pergunta": "Em Toy Story, qual é o melhor amigo do Woody?",
        "opcoes": ["A) Buzz Lightyear", "B) Sr. Cabeça de Batata", "C) Jessie", "D) Rex"],
        "correta": "A"
    },
    {
        "pergunta": "Quem é a princesa que tem uma torre e cabelos longos e mágicos?",
        "opcoes": ["A) Mulan", "B) Rapunzel", "C) Moana", "D) Ariel"],
        "correta": "B"
    },
    {
        "pergunta": "Qual personagem vive em um abacaxi no fundo do mar?",
        "opcoes": ["A) Bob Esponja", "B) Patrick", "C) Lula Molusco", "D) Sandy"],
        "correta": "A"
    }
]

# -----------------------
# LÓGICA DO JOGO
# -----------------------

pontos = 0
erros = 0

for p in perguntas:
    print("\n" + p["pergunta"])
    for opcao in p["opcoes"]:
        print(opcao)

    resposta = input("Digite a letra da resposta: ").upper()

 if resposta == p["correta"]:
        print("✔️ Correto!")
        pontos += 1
    else:
        print("❌ Errado! A resposta certa era:", p["correta"])
        erros += 1

# -----------------------
# PLACAR FINAL
# -----------------------

print("\n=== FIM DO JOGO ===")
print(f"✔️ Acertos: {pontos}")
print(f"❌ Erros: {erros}")

# Mensagens finais personalizadas
if pontos == 7:
    print("🎉 PERFEITO! Você domina tudo sobre Disney e desenhos!")

# Trivia.Alisson.Belly

print("=== JOGO DE TRIVIA ===")
print("Escolha a dificuldade:")
print("1 - Fácil")
print("2 - Médio")
print("3 - Difícil")

dificuldade = input("Digite o número da dificuldade: ")

if dificuldade not in ["1", "2", "3"]:
    print("Dificuldade inválida! Definindo dificuldade Fácil.")
    dificuldade = "1"


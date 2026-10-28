
import random

numero_secreto = random.randint(0, 500)
tentativas = 0
limite = 10

print("=== JOGO DE ADIVINHAR NÚMEROS ===")
print("Adivinhe o número entre 0 e 500!")
print(f"Você tem {limite} tentativas.")

while tentativas < limite:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < 0 or palpite > 500:
        print("Digite um número entre 0 e 500!")
    elif palpite < numero_secreto:
        print("O número secreto é MAIOR!")
    elif palpite > numero_secreto:
        print("O número secreto é MENOR!")
    else:
        print("Parabéns! Você acertou!")
        print(f"Você acertou em {tentativas} tentativa(s)!")
        break

    print(f"Tentativas restantes: {limite - tentativas}")

if tentativas == limite and palpite != numero_secreto:
    print("Fim de jogo! Você esgotou suas tentativas.")
    print(f"O número secreto era {numero_secreto}.")

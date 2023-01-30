print("**************************************")
print("Olá, bem vindo ao jogo de adivinhação")
print("Digite um número de 0 a 100 e veja se você tem sorte!")
print("**************************************")

numero_secreto = 37

chute_str = input("Digite o seu número:")

print("Você digitou", chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
    print("Você acertou!:^)")
else:
    print("Você errou! '_'")

print("Fim de jogo!")




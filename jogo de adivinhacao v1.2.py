t random

print("**************************************")
print("Olá, bem vindo ao jogo de adivinhação")
print("Digite um número de 1 a 100 e veja se você tem sorte!")
print("**************************************")
print("O número de tentativas será baseado de acordo com nível de dificuldade escolhido")
print("**************************************")


numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000


print("qual nivel de dificuldade?")
print("(1) Fácil, (2) Médio, (3) Difícil")

nível = int(input("Defina o nível:"))

if(nível == 1):
    total_de_tentativas = 20
elif(nível == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5


for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número:")
    print("Você digitou", chute_str)
    chute = int(chute_str)


    if(chute <= 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue


    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acerto e fez {} pontos!".format(pontos))
        break
else:
    if(maior):
        print("Você errou! O seu chute foi maior que o número secreto '_'", numero_secreto)
    elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto U.U:", numero_secreto)
        pontos_perdidos = numero_secreto - chute
        pontos = pontos - pontos_perdidos

print("Fim de jogo!")





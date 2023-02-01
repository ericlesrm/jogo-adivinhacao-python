print("**************************************")
print("Olá, bem vindo ao jogo de adivinhação")
print("Digite um número de 0 a 100 e veja se você tem sorte!")
print("**************************************")
print("Você terá rodadas de 5 tentativas cada")
print("**************************************")


numero_secreto = 37
total_de_tentativas = 5
rodada = 1


while(rodada <= total_de_tentativas)
    print("Tentativa {} de {}",format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número:")
    print("Você digitou")
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


if(acertou):
    print("Você acertou!:^)")
else:
    if(maior):
        print("Você errou! O seu chute foi maior que o número secreto '_'")
    elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto U.U")


rodada = rodada + 1

print("Fim de jogo!")




#Criado por Tatiane.
#Link para o meu Linkedin: https://www.linkedin.com/in/tatianetmasutti/.
# Desenvolvi o código para fins de estudo, por isso podem haver formas melhorá-lo.

from random import randint

numero_sorteado = randint(1,100) #Sorteia um número aleatório entre 1 e 100
contador = 0

print("_______________________________________\n")
print("Bem vindo a Adivinhação!\n")
print('Será sorteado um número entre 1 e 100!\n')
print("Você tem 5 tentativas válidas, ou seja,\n\
se chutar um número fora do intervalo\n\
ou letras e símbolos não contam.")

while contador < 5: #Se a quantidade de chutes chegar a 5 encerra o while.
    try: #Utilizado para testar se é um número válido
        print("_______________________________________")
        chute = int(input("\nDigite um número entre 1 e 100: "))
        if (0 < chute <= 100): #Se o chute for um valor válido.
            contador = contador + 1 #Define o quantidade de tentativas.
            restante = 5 - contador #Define quantas tentativas restam.
            maior = chute < numero_sorteado #Compara se o numero sorteado é maior do que o chute.
            proximo = (numero_sorteado - 10) <= chute <= (numero_sorteado + 10) #Identifica se o chute está próximo.
            acertou = (chute == numero_sorteado) #Identifica se é o chute está correto.
            if (chute != numero_sorteado and restante > 0): #Se o chute for errado e ainda há tentativas válidas.
                print("Tente novamente. \nVocê ainda tem {} tentativas.".format(restante))
                if (proximo):
                    print("O número está próximo.")
                if (maior):
                    print("O número sorteado é maior.")
                else: 
                    print("O número sorteado é menor.")
            if (contador == 5 and not acertou ): #Se o total de chute for igual a 5 e o os chutes não foram corretos.
                print("Tentativas encerradas.")
                print("O número sorteado era: {}".format(numero_sorteado))
            if (acertou): #Se o número for o correto encerra o while.
                print("Você acertou!")
                break
        if (0 < chute > 100): #Se o número for menor ou igual a 0 ou maior do que 100.
            print("O número deve ser maior do que 0 e menor ou igual a 100.")
    except ValueError: #Não foi digitado um número inteiro.
        print("Digite um número válido.")

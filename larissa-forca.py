#Artigo que esclarece o funcionamento do comando imports da linguagem Python.
import random 

palavras = []
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def funcao_adiciona():
    global palavras
    while True:
        p = input('Escolha uma palavra: ')
        if p == "":
            break
        palavras.append(p)

#O def é cria uma função 
def principal():
    """
    Função Princial do programa
    """
#Imprimir a palavra Forca 
    print('F O R C A')
    funcao_adiciona()

    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)
#é quando as questões for verdadeira 
    while True:
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
#if e else  são comandos de fluxo, ou seja podem muar a sequencia de execução de um programa 
        if perdeuJogo():
            print('Voce Perdeu!!!')
#break é quebra, quebra (ou interrompe)o fluxo natural do programa 
            break
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
        
def perdeuJogo():
#global  serve para informa que a função não está mais dsponivel somente para um comando e sim para o programa inteiro    
    global FORCAIMG
    if len(letrasErradas) == len(FORCAIMG):
        return True
#return encerra a execução da função corrente, voltado extamente para o ponto onde ela foi chamada 
    else:
#o else é utilizado quando existem 2 opções , ex:existe tal coisa e outra coisa , dando a possibilidade de ser uma verdadeira e outra falsa
        return False
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
#for significa para , ou seja, para tal função existe tal coisa
    for letra in palavraSecreta:
        if letra not in letrasCertas:
#in significa em, ou seja, para letra em palavraSecreta existem mais alternativas.(está entro de tal coisa)
#not in é a mesma coisa, porem existe o not, que significa não, fazendo com que se caso tal coisa não estiver em tal coisa  era tal coisa 
            ganhou = False 
    return ganhou        
        



def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
    else:
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
#range retorna uma serie numerica no intervalo enviado como argumento
#len retorna retorna o numero de caracteres de uma string 
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()

    
principal()

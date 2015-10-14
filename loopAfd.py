#!/usr/bin/env python
sigma = [0,1] #lista de simbolos do AFD
estados = [1,2,3,4,5,6]
programa =[[1,0,2], #[Estado atual, simbolo, estado alcançado]
           [1,1,3],
           [2,1,4],
           [2,0,2],
           [3,1,4],
           [3,0,1],
           [4,1,5],
           [4,0,1],
           [5,0,0],
           [5,1,6],
           [6,0,0],
           [6,1,0]]
Ei = 1 #estado inicial
Ef = [6] #Lista de Estados finais do automato
lEa = []  #lista de estados alcançados a partir de Ei
count = [0,0,0,0,0,0] #lista que conta o numero de vezes que o estado é alcancado
lEa.append(Ei)

def main():
    lAs = [] #lista de estados alcançaveis a partir do estado atual(Ea)
    while(len(lEa)!=0): #verifica se a lista de estados alcançados esta vazia
        #print(lEa)
        Ea = lEa.pop() #coloca o ultimo elemento da lista na variavel de estado atual(Ea)
        for i in sigma: #verifica os estados alcançaveis a partir do estado atual com cada simbolo do alfabeto
            Esa = transicao(Ea,sigma[i]) #estado alcancado a partir de Ea
            if(Esa != 0):
                if(Esa not in lAs): #se o estado ainda não foi alcançado partindo de Ea
                    count[Esa -1] = count[Esa -1] + 1 #numero de vezes em que um estado foi alcançado
                    lEa.append(Esa) #adiciona Esa a lista de estados alcançados a partir de Ei
                    lAs.append(Esa) #adiciona Esa a lista de estados alcançados a partir de Ea
                if(count[Esa-1]>2): #se o estado atual estiver em loop
                    while(Esa in lEa):lEa.remove(Esa) #remove todos os Esa que entram em loop
            if(Esa in Ef and count[Ea-1]>1): #se o estado Alcançado por Ea for Estado final e se o estado atual possuir loop
                print("Automato possui loop")
                return 1
        lAs = [] #zera a lista de Estados alcançados a partir de Ea para iniciar a computação
    print("Automato não possui loop")


def transicao(Eatual,sig): #retorna o estado que é alcançado a partir do Eatual com o simbolo sig
    for i in programa:
        if(i[0] == Eatual and i[1] == sig):
            return i[2]

main()

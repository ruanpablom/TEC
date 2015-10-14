sigma = [0,1] #lista de simbolos do AFD
estados = [1,2,3,4,5,6]
programa =[[1,0,6],
           [1,1,2],
           [2,1,5],
           [2,0,3],
           [3,1,4],
           [3,0,4],
           [4,1,3],
           [4,0,3],
           [5,0,3],
           [5,1,3],
           [6,0,5],
           [6,1,3]]
Ei = 1 #estado inicial
Ef = [5] #Lista de Estados finais do automato
lEa = []  #lista de estados alcançados a partir de Ei
count = [0,0,0,0,0,0] #lista que conta o numero de vezes que o estado é alcancado
lEa.append(Ei)

def main():
    loop = False #identifica a existencia de loop no automato
    lAs = [] #lista de estados alcançaveis a partir do estado atual
    while(len(lEa)!=0):
        print(lEa)
        inc = False
        Ea = lEa.pop() #estado atual
        lAs.append(Ea)
        for i in sigma:
            Esa = transicao(Ea,sigma[i]) #estado alcancado a partir de Ea
            if(Esa != 0): 
                if(Esa not in lAs):
                    count[Esa -1] = count[Esa -1] + 1
                    lEa.append(Esa)
                    lAs.append(Esa)
                    inc = True
                if(count[Esa -1]>1 and inc == True):
                    if(count[Esa-1]>2): 
                        while(Esa in lEa):lEa.remove(Esa)
                    loop = True 
            if(Esa in Ef and loop):
                print("Automato possui loop")
                return 1
        lAs = []    
    print("Automato não possui loop")


def transicao(Eatual,sig):
    transicoes = [] #possiveis transicoes
    for i in programa:
        if(i[0] == Eatual and i[1] == sig):
            return i[2]

main()

import numpy as np
import random

plik = open("australian.dat")
lista = []
for line in plik:
    lista.append(list(map(lambda e:float(e) , line.replace('\n','').split(' '))))


x=[1,1,1,1,1,8,5,6,3,2,1,1,1,1]


def od(x,lista):
    tmp = 0
    wyn = []
    for j in range(len(lista)):
        tmp = 0
        for e in range(len(lista[j])-1):
           tmp += (lista[j][e] - x[e])**2
        tmp = tmp**(1/2)
        wyn.append((lista[j][-1], tmp))
    return wyn


listaod = od(x,lista)
#print(listaod)


def grupowanie(lista):
    tmp = {}
    for i in range(len(lista)):
        c = lista[i][0]
        if c not in tmp:
            tmp[c]=[]
        tmp[c].append(lista[i][1])
    return tmp


grup = grupowanie(listaod)
#print(grup)


def sumowanie(grupa, k):
    count = 0
    wyn = {}
    for j in range(len(grupa)):
        tmp=sorted(grupa[j])
        sumka = 0
        for i in range(k):
            sumka += tmp[i]
        c = list(grupa)[j]
        if c not in wyn:
            wyn[c] = 0
        if sumka in wyn.values():
            return "Brak odpowiedzi"
        wyn[c]+=sumka

    res = min(wyn,key=wyn.get)
    return (res, wyn[res])


sumeczka = sumowanie(grup,5)
#print(sumeczka)


d = {0: [3, 3, 3], 1: [3, 3, 3]}
test = sumowanie(d, 3)
#print(test)


def euk(a,b):
    tmp=0
    for e in range(len(lista[a])):
        tmp+=(lista[a][e] - lista[b][e])**2
    tmp=tmp**(1/2)
    return tmp


def euk2(lista1, lista2):
    lista1 = lista1[:-1]
    lista2 = lista2[:-1]
    v1 = np.array(lista1)
    v2 = np.array(lista2)
    c=0
    for i in range(len(v1)):
        c += (v1[i]-v2[i])**2

    return c**(1/2)


print(euk2(lista[0], lista[1]))

print(euk(0,1))

#pd całkowanie numeryczne
#montecarlo
#lub sumy górne lub dolne//prostokątów/trapezów metoda
#i dokonczyc ze srodkiem ciezkosci
#na wykladzie: 28.02 1:10:00

nowa=lista

for i in range(len(nowa)):
    nowa[i] = nowa[i][:-1]


def kolorowanie(lista):

    for i in range(len(lista)):
        wyb=random.randint()
        if wyb%2==0:
            
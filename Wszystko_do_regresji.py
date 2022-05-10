import numpy as np
import random
import re

def tworz():
    plik = open("australian.dat")
    lista = []
    for line in plik:
        lista.append(list(map(lambda e: float(e), line.replace('\n', '').split(' '))))
    return lista
lista = tworz()
x = [1, 1, 1, 1, 1, 8, 5, 6, 3, 2, 1, 1, 1, 1]


def od(x, lista):
    tmp = 0
    wyn = []
    for j in range(len(lista)):
        tmp = 0
        for e in range(len(lista[j]) - 1):
            tmp += (lista[j][e] - x[e]) ** 2
        tmp = tmp ** (1 / 2)
        wyn.append((lista[j][-1], tmp))
    return wyn


listaod = od(x, lista)


# print(listaod)


def grupowanie(lista):
    tmp = {}
    for i in range(len(lista)):
        c = lista[i][0]
        if c not in tmp:
            tmp[c] = []
        tmp[c].append(lista[i][1])
    return tmp


grup = grupowanie(listaod)


# print(grup)


def sumowanie(grupa, k):
    count = 0
    wyn = {}
    for j in range(len(grupa)):
        tmp = sorted(grupa[j])
        sumka = 0
        for i in range(k):
            sumka += tmp[i]
        c = list(grupa)[j]
        if c not in wyn:
            wyn[c] = 0
        if sumka in wyn.values():
            return "Brak odpowiedzi"
        wyn[c] += sumka

    res = min(wyn, key=wyn.get)
    return (res, wyn[res])


sumeczka = sumowanie(grup, 5)
# print(sumeczka)


d = {0: [3, 3, 3], 1: [3, 3, 3]}
test = sumowanie(d, 3)


# print(test)


def euk(a, b):
    tmp = 0
    for e in range(len(lista[a])):
        tmp += (lista[a][e] - lista[b][e]) ** 2
    tmp = tmp ** (1 / 2)
    return tmp


def euk2(lista1, lista2):
    lista1 = lista1[:-1]
    lista2 = lista2[:-1]
    v1 = np.array(lista1)
    v2 = np.array(lista2)
    c = 0
    for i in range(len(v1)):
        c += (v1[i] - v2[i]) ** 2

    return c ** (1 / 2)


# print(euk2(lista[0], lista[1]))

# print(euk(0, 1))

# pd ca³kowanie numeryczne
# montecarlo
# lub sumy górne lub dolne//prostokıtów/trapezów metoda
# i dokonczyc ze srodkiem ciezkosci
# na wykladzie: 28.02 1:10:00

nowa = lista

for i in range(len(nowa)):
    nowa[i] = nowa[i][:-1]


# print(nowa)

def kolorowanie(lista):
    for i in range(len(lista)):
        wyb = random.randint(0, 100)
        if wyb % 2 == 0:
            lista[i].append(1.0)
        else:
            lista[i].append(0.0)


kolorowanie(nowa)


def toDict(lista, tmp):
    res = {0: [], 1: []}
    for i in range(len(lista)):
        if lista[i][-1] == 0:
            res[0].append(tmp[i])
        else:
            res[1].append(tmp[i])
    return res


def srodki(lista):
    suma = 0
    count = 1
    tmp = []
    while count != 0:
        for i in range(len(lista)):
            for j in range(len(lista)):
                if lista[i][-1] == lista[j][-1]:
                    suma += euk2(lista[i], lista[j])
            tmp.append(suma)
            suma = 0
        d = toDict(lista, tmp)
        srz = min(d[0])
        srj = min(d[1])
        iz = tmp.index(srz)
        ij = tmp.index(srj)

        count = 0
        for k in range(len(lista)):
            if euk2(lista[k], lista[iz]) <= euk2(lista[k], lista[ij]):
                if lista[k][-1] != 0:
                    count += 1
                    lista[k][-1] = 0.0
            else:
                if lista[k][-1] != 1:
                    count += 1
                    lista[k][-1] = 1.0

        print(count)
    return lista



def porownaj(lista1, lista2):
    wynik0 = [0, 0]
    wynik1 = [0, 0]
    for i in range(len(lista1)):
        if lista1[i][-1]==lista2[i][-1] and lista1[i][-1]==0:
            wynik0[0]=wynik0[0]+1

        if lista1[i][-1]==lista2[i][-1] and lista1[i][-1]==1:
            wynik1[0]=wynik1[0]+1

        if lista1[i][-1]==1:
            wynik1[1]=wynik1[1]+1

        if lista1[i][-1]==0:
            wynik0[1]=wynik0[1]+1
    return [wynik0,wynik1]


lista = tworz()
#wysrodkowana=srodki(nowa)
#print(wysrodkowana)
#porownanie = porownaj(lista,wysrodkowana)
#print("0:",porownanie[0][0]/porownanie[0][1])
#print("1:",porownanie[1][0]/porownanie[1][1])


def funkcja(x):
    # return -(x**2)+4
    return x


def monteCarlo(xp,xk):
    yp = funkcja(xp)
    yk = funkcja(xk)
    n = 10000
    p = abs(xk-xp)*abs(yk-yp)
    c = 0
    for i in range(n):
        x = random.uniform(xp, xk)
        y = random.uniform(yp, yk)
        if 0 < y and y <= funkcja(x):
            c=c+1
        if 0 > y and y >= funkcja(x):
            c=c-1
    return p * (c/n)


def punkty(xk,xp,n):
    x=[]
    for i in range(1,n+1):
        x.append(xp+(i/n)*(xk-xp))
    return x

def prostokaty(xp,xk):
    n = 10000
    x=punkty(xp,xk,n)
    s=0
    d=(xk-xp)/n
    for i in range(n):
        s+=funkcja(x[i])
    s=s*d
    return s

#print(monteCarlo(0,1))
#print(prostokaty(0,1))

def srednia(lista):
    for i in range(len(lista)):
        sr = np.dot(lista, np.ones(len(lista)))
        sr = sr / len(lista)
    return sr

def wariancja(lista):
    for i in range(len(lista)):
        wr = lista - np.dot(srednia(lista), np.ones(len(lista)))
        wr = np.dot(wr, wr)
        wr = wr / len(lista)
    return wr


def odchylenie(lista):
    war = wariancja(lista)
    return war ** (1/2)

stata=[1,1,5,6,3,2,6,8,2,4]
#print(srednia(stata))
#print(wariancja(stata))
#print(odchylenie(stata))

# W DOMU!
#zrobic prostokıty DONE
#zrobic porownanie ile procent australiana kolorowania pokrywa sie z nowym kolorowaniem DONE
#wszystkie funkcje dla pojedynczego wektoera
#srednia - pomnozyc wektor przez wektor jednostkowy (skalarnie) i podzielic przez ilosc DONE
#wariancja - (wektor - srednia*wektor jednostkowy) potem iloczyn skalarny tego co wyjdzie z nim samym
#wariancja powinna wyjsc 0


# REGRESJA =============================================

# XB=y
# Macierz X to pierwsza kolumna samych jedynek a druga to obserwacje x1...xn
# beta to wektor beta0 i beta1
# y to wektor y1...yn
# z mnozenia XB jest b0+b1x1 = y1 i tak dla wszystkich
# podobne do y = ax + b
# beta1 to nachylenie prostej
# beta0 to o ile jest podniesiona  prosta (przeciecie oY)
# Trzeba to XB=y pomnozyc lewostronnie przez X^t
# X^TXB=X^Ty
# 2,1 5,2 7,3 8,3 to sı punkty i dla nich powinno wyjsc b0 =2/7, b1=5/14

punkty = [(2, 1), (5, 2), (7, 3), (8, 3)]


def regresja(punkty):
    # tworzenie i ustawianie x w macierzy X
    mx = np.ones((len(punkty), 2))
    for i in range(len(punkty)):
        mx[i, 1] = punkty[i][0]

    # tworzenie i ustawianie y w macierzy y
    my = np.ones((len(punkty),1))
    for i in range(len(punkty)):
        my[i]=punkty[i][1]
    mxt = np.transpose(mx)
    mxti = np.linalg.inv(np.dot(mxt,mx))
    b = np.dot(np.dot(mxti,mxt),my)
    return b



regresja(punkty)
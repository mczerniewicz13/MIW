import numpy as np
# =======================QR=======================

def proj(u, v):
    a = np.dot(v, u)
    b = np.dot(u, u)
    return (a / b) * u


def vectorLen(v):
    wyn = 0
    for i in range(len(v)):
        wyn += v[i] ** 2

    return wyn ** (1 / 2)


def e(u):
    return u / vectorLen(u)


def qr(macierz):
    q = []
    ulist = []
    for i in range(len(macierz)):
        u = np.array(macierz[i])
        sumProj = 0
        if i > 0:
            for j in range(i):
                sumProj += proj(ulist[j], u)
            u = u - sumProj

        ulist.append(u)
        q.append(e(u))

    q = np.array(q)
    qt = q.transpose()
    r = macierz.dot(qt)
    r = r.transpose()
    return (qt, r)


# =======================QR=======================


def Ak(a):
    a0 = a
    q, r = qr(a)
    ak1 = np.matmul(r, q)
    return ak1

#A = [[1,2,2],[0,5,4],[1,6,0]] # 8 -3 1
A = [[3, 2], [4, 1]]  # 5 -1
def wartosciWlasne(A):
    a = np.array(A)
    aCopy = a
    for i in range(10):
        a = Ak(a)

    wynik=[]
    for i in range(len(a)):
        wynik.append(round(a[i][i]))
    return wynik

def wektorWlasny(macierz):
    # Wektor własny
    w, v = np.linalg.eig(macierz)
    return v
'''
    s = len(macierz)
    for i in range(s):
        macierz[i][i] = macierz[i][i]-wartosc
        

 Gauss-Jordan nie działa dla układów nieoznaczonych
    #print("Macierz po odjęciu wartości własnych: \n",macierz)
    # Tworzenie macierzy do metody Gaussa-Jordana
    w = np.zeros((s, s+1))
    for i in range(s):
        for j in range(s):
            w[i][j] = int(macierz[i][j])

    #print("Macierz w: \n",w)

    for i in range(s):
        for j in range(s):
            if i != j:
                ratio = w[j][i] / w[i][i]
                #print("Ratio: ",ratio,i,j)
                #print("w[j][i]: ", w[j][i])
                #print("w[i][i]: ", w[i][i])

                for k in range(s + 1):
                    w[j][k] = w[j][k] - ratio * w[i][k]
                    #print(w[j][k] - ratio * w[i][k])
    #print(w)
    wyn=np.zeros(s)
    for i in range(s):
        wyn[i]=w[i][s]/a[i][i]
    return wyn
'''

def maxWartosc(arr):
    wyn=arr[0]
    for i in range(len(arr)):
        if wyn<arr[i]:
            wyn=arr[i]
    return wyn
#====================SVD==========================
np.set_printoptions(suppress=True)
a=[[1,2,0],[2,0,2]]
a=np.array(a)
u = a.dot(a.transpose())

print("Macierz AAt:\n",u)
ww=wartosciWlasne(u)
print("Wartości własne U:\n",ww)
wu,wektoryu = np.linalg.eig(u)
print("Wektory własne U:\n",wektoryu)

v = a.transpose().dot(a)
print("Macierz AtA:\n",v)
print("Wartości własne V:\n",ww)
wv,wektoryv = np.linalg.eig(v)
print("Wektory własne V:\n",wektoryv.transpose())

sigma = np.zeros_like(a)
for i in range(len(ww)):
    sigma[i][i]=maxWartosc(ww)**(1/2)
    ww.pop(ww.index(maxWartosc(ww)))

print(sigma)

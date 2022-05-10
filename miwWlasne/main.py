import numpy as np


# =======================QR=======================
def column(mat, n):
    return [row[n] for row in mat]


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


def mnozenieMacierzy(a, b):
    aRows = len(a)
    aCols = len(a[0])
    bRows = len(b)
    bCols = len(b[0])
    wyn = np.zeros((aRows, bCols))
    if aRows == bCols and aCols == bRows:
        for i in range(aRows):
            for j in range(bCols):
                for k in range(len(a[0])):
                    print(i, j)
                    wyn[i][j] += a[i][k] * b[k][i]

    else:
        print("Nieprawidłowe rozmiary macierzy")
        return -1

    return np.array(wyn)


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


# def wekWlasny():


A = [[1,2,2],[0,5,4],[1,6,0]] # 8 -3 1
#A = [[3, 2], [4, 1]]  # 5 -1
a = np.array(A)
aCopy = a
for i in range(10):
    a = Ak(a)
np.set_printoptions(precision=0, suppress=True)
print(a)

# Zbieranie wartości własnej do array
wlasne = []
for i in range(len(a)):
    wlasne.append(a[i][i])
dl = len(wlasne)
wlasne = np.array(wlasne)
np.rint(wlasne)

# Macierz wartosci wlasnej do odejmowania
wlasneMat = np.zeros((dl, dl))
for i in range(len(wlasne)):
    wlasneMat[i][i] = wlasne[i]

# Odejmowanie macierzy poczatkowej i macierzy wartosci wlasnych
aWyn = aCopy - wlasneMat
print(aWyn)

# Tworzenie macierzy do metody Gaussa-Jordana
w = np.zeros((dl, dl + 1))
for i in range(dl):
    for j in range(dl):
        w[i][j] = aWyn[i][j]

print(w)

for i in range(dl):
    for j in range(dl):
        if i != j:
            ratio = w[j][i] / w[i][i]

            for k in range(dl + 1):
                w[j][k] = w[j][k] - ratio * w[i][k]
print(w)

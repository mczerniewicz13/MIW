import numpy as np


def column(mat,n):
    return [row[n] for row in mat]


def proj(u,v):
    a = np.dot(v,u)
    b = np.dot(u,u)
    return (a/b)*u


def vectorLen(v):
    wyn = 0
    for i in range(len(v)):
        wyn += v[i]**2

    return wyn**(1/2)





def e(u):
    return u/vectorLen(u)


def mnozenieMacierzy(a,b):
    aRows = len(a)
    aCols = len(a[0])
    bRows = len(b)
    bCols = len(b[0])
    wyn=np.zeros((aRows,bCols))
    if aRows == bCols and aCols == bRows:
        for i in range(aRows):
            for j in range(bCols):
                for k in range(len(a[0])):
                    print(i,j)
                    wyn[i][j]+=a[i][k]*b[k][i]

    else:
        print("Nieprawidłowe rozmiary macierzy")
        return -1

    return np.array(wyn)


def qr(macierz):
    q=[]
    ulist=[]
    for i in range(len(macierz)):
        u=np.array(macierz[i])
        sumProj=0
        if i>0:
            for j in range(i):
                sumProj+=proj(ulist[j],u)
            u=u-sumProj

        ulist.append(u)
        q.append(e(u))

    q=np.array(q)
    qt=q.transpose()
    r = macierz.dot(qt)
    r = r.transpose()
    return (qt,r)

list = [[1,1,0],[0,1,1],[1,0,1]]
macierz = np.array(list)

t = qr(macierz)
print(t[0],"\n",t[1])




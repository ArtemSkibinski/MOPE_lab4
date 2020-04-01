import numpy as np

X1max = 30
X1min = -20
X2max = 15
X2min = -35
X3max = 5
X3min = -20
Ymax = 200 + (X1max + X2max + X3max)/3
Ymin = 200 + (X1min + X2min + X3min)/3
X = [[X1min, X2min, X3min],
     [X1min, X2min, X3max],
     [X1min, X2max, X3min],
     [X1min, X2max, X3max],
     [X1max, X2min, X3min],
     [X1max, X2min, X3max],
     [X1max, X2max, X3min],
     [X1max, X2max, X3max]]

nX1min = nX2min = nX3min = -1
nX1max = nX2max = nX3max = 1
x = [[1, nX1min, nX2min, nX3min, nX1min * nX2min, nX1min * nX3min, nX2min * nX3min, nX1min * nX2min * nX3min],
     [1, nX1min, nX2min, nX3max, nX1min * nX2min, nX1min * nX3max, nX2min * nX3max, nX1min * nX2min * nX3max],
     [1, nX1min, nX2max, nX3min, nX1min * nX2max, nX1min * nX3min, nX2max * nX3min, nX1min * nX2max * nX3min],
     [1, nX1min, nX2max, nX3max, nX1min * nX2max, nX1min * nX3max, nX2max * nX3max, nX1min * nX2max * nX3max],
     [1, nX1max, nX2min, nX3min, nX1max * nX2min, nX1max * nX3min, nX2min * nX3min, nX1max * nX2min * nX3min],
     [1, nX1max, nX2min, nX3max, nX1max * nX2min, nX1max * nX3max, nX2min * nX3max, nX1max * nX2min * nX3max],
     [1, nX1max, nX2max, nX3min, nX1max * nX2max, nX1max * nX3min, nX2max * nX3min, nX1max * nX2max * nX3min],
     [1, nX1max, nX2max, nX3max, nX1max * nX2max, nX1max * nX3max, nX2max * nX3max, nX1max * nX2max * nX3max]]

m = 3
N = 8
print("Кодовані значення факторів: ")
for row in x:
      for i in row:
          print("{:4d}".format(int(i)), end = " |")
      print()
print("Натуральні значення факторів: ")
for row in X:
      for i in row:
          print("{:4d}".format(int(i)), end = " |")
      print()

def lab4(m, N):
    A = np.random.randint(Ymin, Ymax, (N, m))
    print("Згенерована матриця значень Y: ")
    for row in A:
        for i in row:
            print("{:4d}".format(int(i)), end=" |")
        print()

    print("Середні значення натуральних значеннь факторів по стовпчикам:")
    mx_all = np.sum(X, axis=0) / N
    mx1, mx2, mx3 = mx_all
    print("mx1 = ", mx1)
    print("mx2 = ", mx2)
    print("mx3 = ", mx3)

    s = np.sum(X, axis=0)
    s1, s2, s3 = s
    m0 = [N, s1, s2, s3, s1*s2, s1*s2, s2*s3, s1*s2*s3]
    m1 = [i * s1 for i in m0]
    m2 = [i * s2 for i in m0]
    m3 = [i * s3 for i in m0]
    m4 = [i * (s1*s2) for i in m0]
    m5 = [i * (s1*s3) for i in m0]
    m6 = [i * (s2*s3) for i in m0]
    m7 = [i * (s1*s2*s3) for i in m0]
    Yall = np.sum(A , axis=1) / m
    Y0, Y1, Y2, Y3, Y4, Y5, Y6, Y7 = Yall
    k0 = Y0
    k1 = Y1 * s1
    k2 = Y2 * s2
    k3 = Y3 * s3
    k4 = Y4 * s1 * s2
    k5 = Y5 * s1 * s3
    k6 = Y6 * s2 * s3
    k7 = Y7 * s1 * s2 * s3
    det = np.linalg.det([
        m0,
        m1,
        m2,
        m3,
        m4,
        m5,
        m6,
        m7
    ])
    print(det)
lab4(m, N)

c = 3
r = 3
matrix=[]
Z12 = 0.1+0.3j
Z13 = 0.2+0.6j
Z23 = 0.15+0.5j
Y12 = 0.01j
Y23 = 0.00625j
Y13 = 0.014j
Y12 = (1/Z12)
Y21 = (1/Z12)
Y31 = (1/Z13)
Y32 = (1/Z23)
Y13 = (1/Z13)
Y23 = (1/Z23)
Y10 = 0.024j
Y20 = 0.01625j
Y30 = 0.02025j
Y11 = Y10+ Y12 + Y13
Y22 = Y20+ Y21 + Y23
Y33 = Y30+ Y31 + Y32
K = 0
while(K<9):
    for i in range(r):
        a = []
        for j in range(c):
            s = [[Y11, -(Y12), -(Y13)],[-(Y12), Y22, -(Y23)],[-(Y13), -(Y23), Y33]]
            a.append(s)
        matrix.append(a)
        K=K+1
print(matrix[i][j],end =" ")
print("\n")

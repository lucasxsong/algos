defstrassen(Y,Z):
    if len(Y) <= 2:
        return mult(Y,Z)
    else:
        A,B,C,D = partition(Y)
        E,F,G,H = partition(Z)
        M1 = strassen(add(A,C),add(E,F))
        M2 = strassen(add(B,D),add(G,H))
        M3 = strassen(sub(A,D),add(E,H))
        M4 = strassen(A,sub(F,H))
        M5 = strassen(add(C,D),E)
        M6 = strassen(add(A,B),H)
        M7 = strassen(D,sub(G,E))
        I = sub(sub(add(M2,M3),M6),M7)
        J = add(M4,M6)K = add(M5,M7)
        L = sub(sub(sub(M1,M3),M4),M5)
        return recompose(I,J,K,L)
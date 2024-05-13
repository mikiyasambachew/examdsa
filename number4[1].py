def  bubblessort(alphabets):
    for i in range(len(alphabets)- 1, 0 -1):
        for j in range (0,i):
            if alphabeta[j] > alphabets[j+1]:
                alphabets[j], alphabets[j+1] = alphabets[j+1], alphabets[j]
    return alphabets
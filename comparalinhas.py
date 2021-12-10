def comparaLinhas(mat):
    
    numLinhas = len(mat)
    for i in range(numLinhas):
        for j in range(numLinhas):
            if i!=j and mat[i]==mat[j]:
                return True
            
    return False

mat = [[1, 2, 3],
       [4, 5, 6],
       [1, 2, 3],
       [7, 8, 9]]

print(comparaLinhas(mat))
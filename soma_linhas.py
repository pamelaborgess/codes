def somaLinhas(mat):
    # Armazena número de linhas e colunas da matriz
    numLinhas = len(mat)
    numColunas = len(mat[0])

    # Define uma lista para armazenar as somas
    somas = []
    for i in range(0,numLinhas):
        # Soma a linha i
        soma = 0
        for j in range(0,numColunas):
            soma = soma + mat[i][j]
        somas.append(soma)
        
    return somas

mat = [[1, 2, 1], [1, 2, 3], [2, 2, 1]]
print(somaLinhas(mat))
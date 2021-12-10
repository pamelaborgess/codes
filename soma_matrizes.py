mat1 = [[1, 2, 1],
        [2, 3, 1],
        [2, 1, 1]]

mat2 = [[4, 3, 5],
        [4, 2, 3],
        [3, 4, 1]]

# Define uma lista vazia
matRes = []
for i in range(0,3):
    # Lista que irá armazenar as somas na linha i
    soma_linha = []
    for j in range(0,3):
        # Soma os elementos das matrizes
        soma = mat1[i][j] + mat2[i][j]
        # Adiciona o resultado na lista soma_linha
        soma_linha.append(soma)
    # Adiciona a linha na matriz    
    matRes.append(soma_linha)
        
print(matRes)

        
        
        
matriz = [[74,65,87],
          [7,3,1],
          [0,4,2]]

while True:
    x = input("Digite um valor para substituir na matriz ou 's' para sair:")
    if x == "s":
        print("Matriz inalterada.")
        break

    i = int(input("Digite a linha da matriz:"))
    j = int(input("Digite a coluna da matriz:"))
    if i > 3 or j > 3:
        print("Erro.")
        print("Matriz inalterada.")
        break
    i = i - 1
    j = j - 1
    matriz[i][j] = x
    
print(matriz[0])
print(matriz[1])
print(matriz[2])
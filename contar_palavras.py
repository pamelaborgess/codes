m = 0
nome = input("Digite uma frase:")
lista = nome.split(" ")

for i in range (len(lista)):
    a = len(lista[i])
    if a > m:
        m = a
        b = i
print("O número de palavras da frase é: ", len(lista))
print("A maior palavra é:",lista[b])
print("O número de letras da maior palavra é:",m)
    
#conta a ocorrência da letra escolhida e o número de vogais

def my_count(frase, n):
    cont = 0
    frase = frase.lower()
    n = n.lower()
    for i in frase:
        if i == n:
            cont = cont + 1
    return cont

fr = str(input("Digite uma frase: "))
carac = str(input("Digite a letra: "))
num = my_count(fr, carac)
num1 = my_count(fr, "a")
num2 = my_count(fr, "e")
num3 = my_count(fr, "i")
num4 = my_count(fr, "o")
num5 = my_count(fr, "u")
soma = num1 + num2 + num3 + num4 + num5
print ("O número de ocorrências da letra é: ",num)
print ("O número de vogais na frase é: ",soma)
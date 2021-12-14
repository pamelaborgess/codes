par = []
impar = []

while True:
    n = input("Digite um número inteiro ou 's' para sair: ")
    if n != 's':
        n = int(n)
        if n%2 == 0:
            par.append(n)
        else:
            impar.append(n)
    else:
        break
    
par = sorted(par)
maior_par = par[-1]
impar = sorted(impar)
maior_impar = impar[-1]

print("O maior número ímpar é: ", maior_impar)
print("O maior número par é: ", maior_par)

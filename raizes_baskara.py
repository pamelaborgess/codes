import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c
raiz_um = (-b + math.sqrt(delta)) / (2 * a)
raiz_dois = (-b - math.sqrt(delta)) / (2 * a)

print(f'Delta: {delta}')

if delta < 0:
    print("Não há raízes reais")
elif delta > 0:
    print("Há duas raízes")
    print("Raíz 1: ", round(raiz_um, 2))
    print("Raíz 2: ", round(raiz_dois, 2) )
else:
    print("Há apenas uma raiz. Valor: ", (-b + math.sqrt(delta)) / (2 * a))


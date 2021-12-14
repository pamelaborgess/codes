a=float(input("Digite o valor do lado a: "))
b=float(input("Digite o valor do lado b: "))
c=float(input("Digite o valor do lado c: "))
if(a<0 or b<0 or c<0):
    print("Você não pode fornecer valores negativos")
elif((b-c)<a and a<(b+c) and (a-c)<b and b<(a+c) and (a-b)<c and c<(a+b)):
    if(a!=b and b!=c and a!=c):
        print("Triângulo escaleno.")
    if(a==b and b==c):
        print("Triângulo equilátero.")
    if(a!=b and b==c or a==b and b!=c or a==c and c!=b):
        print("Triângulo isósceles.")
else:
    print("Lados não formam um triângulo")


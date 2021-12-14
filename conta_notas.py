valor=int(input("Digite uma quantia inteira em reais: R$"))
nota_100=int(valor/100)
resto_100=valor%100
nota_50=int(resto_100/50)
resto_50=resto_100%50
nota_20=int(resto_50/20)
resto_20=resto_50%20
nota_10=int(resto_20/10)
resto_10=resto_20%10
nota_5=int(resto_10/5)
resto_5=resto_10%5
moeda_1=int(resto_5/1)
resto_1=resto_5%1
if(valor<0):
    print("Valor incorreto.")
else:
    print("Número de notas de 100 reais: ", nota_100)
    print("Número de notas de 50 reais: ", nota_50)
    print("Número de notas de 20 reais: ", nota_20)
    print("Número de notas de 10 reais: ", nota_10)
    print("Número de notas de 5 reais: ", nota_5)
    print("Número de moedas de 1 real: ", moeda_1)
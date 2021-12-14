P1 = float(input("Digite a nota da primeira prova: "))
P2 = float(input("Digite a nota da segunda prova: "))
sub = float(input("Digite a nota da prova sub: "))
media1 = (P1+2*P2)/3
media2 = (sub+2*P2)/3
media3 = (P1+2*sub)/3
if P2 > P1 and sub > P1:
    print("Sub deve substituir a P1.")
    print("Média final antes: ", round(media1,2))
    print("Média final depois: ", round(media2,2))
    if media2 >= 6:
        print("APROVADO!")
    elif media2 >=5 and media2 < 6:
        print("EM RECUPERAÇÃO.")
    else:
        print("REPROVADO.")
elif P1 > P2 and sub > P2:
    print("Sub deve substituir a P2.")
    print("Média final antes: ", round(media1,2))
    print("Média final depois: ", round(media3,2))
    if media3 >= 6:
        print("APROVADO!")
    elif media3 >=5 and media3 < 6:
        print("EM RECUPERAÇÃO.")
    else:
        print("REPROVADO.")
else:
    print("Nota da sub deve ser ignorada.")
    print("Média final: ", round(media1,2))
    
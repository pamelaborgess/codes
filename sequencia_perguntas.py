suco = input(" Você gostaria de um suco? (sim/não): ")
if suco == "sim":
    preco_do_suco = 4.5
elif suco == "não":
    preco_do_suco = 0

refrigerante = input("Você gostaria de um refrigerante? (sim/não): ")
if refrigerante == "sim":
    preco_do_refri = 4.0
elif refrigerante == "não":
    preco_do_refri = 0

entrada = input("Você gostaria de uma entrada? (sim/não): ")
if entrada == "sim":
    preco_da_entrada = 7.0
elif entrada == "não":
    preco_da_entrada = 0

prato_principal = input("Você gostaria de um prato principal? (sim/não): ")
if prato_principal == "sim":
    preco_prato_principal = 25.0
elif prato_principal == "não":
    preco_prato_principal = 0

sobremesa = input("Você quer uma sobremesa?: ")
if sobremesa == "sim":
    preco_sobremesa = 10.0
elif sobremesa == "não":
    preco_sobremesa = 0

conta = preco_do_suco + preco_do_refri + preco_da_entrada + preco_prato_principal + preco_sobremesa
print("O valor final da sua conta a pagar é de R$", round(conta, 2),"reais.")
nome = input("Nome da pessoa: ")

def print_nome():
    global nome
    nome = input("Nome da segunda pessoa: ")
    print("O nome dentro da função é ",nome)

print_nome()
print("O nome fora da função é ",nome)
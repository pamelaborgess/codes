inventario = {}
total = 0

while True:
    acesso = input("Digite "c" para cadastrar um novo usuário. Digite "b" para buscar um usuario ja cadastrado. Digite "s" para encerrar o programa:")
    
    if acesso == "c" :
        nome = input("Digite o nome:")
        cpf = int(input("Digite o CPF:"))
        idade = int(input("Digite a idade:"))
        adress = input("Digite o endereço:")
    
        inventario[cpf] = nome, idade , adress
        print(inventario)
    
    elif acesso == "b" :
        busca = int(input("Digite o CPF para acessar as informações:"))
        if busca in inventario :
            print(inventario[busca])
        else :
            print("Usuário não se encontra no banco de dados.")
        
    else :
        break
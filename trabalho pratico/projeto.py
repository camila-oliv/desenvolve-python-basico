import csv

# Estrutura de Dados para Usuários
usuarios = {}

# Estrutura de Dados para Produtos
produtos = []

# Função para carregar dados dos arquivos
def carregar_dados():
    global usuarios, produtos
    with open('usuarios.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            usuarios[row[0]] = [row[1], row[2]]
    
    with open('produtos.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produtos.append(row)

# Função para salvar dados nos arquivos
def salvar_dados():
    with open('usuarios.csv', 'w') as file:
        writer = csv.writer(file)
        for usuario, info in usuarios.items():
            writer.writerow([usuario] + info)
    
    with open('produtos.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['titulo', 'autor', 'preco', 'quantidade'])
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)

# Função para adicionar um novo usuário (Create)
def adicionar_usuario(nome, senha, permissao):
    usuarios[nome] = [senha, permissao]
    salvar_dados()

# Função para listar todos os usuários (Read)
def listar_usuarios():
    for usuario, info in usuarios.items():
        print(f"Nome: {usuario}, Permissão: {info[1]}")

# Função para atualizar um usuário (Update)
def atualizar_usuario(nome, nova_senha=None, nova_permissao=None):
    if nome in usuarios:
        if nova_senha:
            usuarios[nome][0] = nova_senha
        if nova_permissao:
            usuarios[nome][1] = nova_permissao
        salvar_dados()

# Função para remover um usuário (Delete)
def remover_usuario(nome):
    if nome in usuarios:
        del usuarios[nome]
        salvar_dados()

# Função para adicionar um novo produto (Create)
def adicionar_produto(titulo, autor, preco, quantidade):
    produtos.append({'titulo': titulo, 'autor': autor, 'preco': preco, 'quantidade': quantidade})
    salvar_dados()

# Função para listar todos os produtos (Read)
def listar_produtos():
    for produto in produtos:
        print(produto)

# Função para atualizar um produto (Update)
def atualizar_produto(titulo, novo_autor=None, novo_preco=None, nova_quantidade=None):
    for produto in produtos:
        if produto['titulo'] == titulo:
            if novo_autor:
                produto['autor'] = novo_autor
            if novo_preco:
                produto['preco'] = novo_preco
            if nova_quantidade:
                produto['quantidade'] = nova_quantidade
            salvar_dados()

# Função para remover um produto (Delete)
def remover_produto(titulo):
    global produtos
    produtos = [produto for produto in produtos if produto['titulo'] != titulo]
    salvar_dados()

# Função para buscar um produto específico (Buscar)
def buscar_produto(titulo):
    for produto in produtos:
        if produto['titulo'] == titulo:
            print(produto)
            return produto
    print("Produto não encontrado.")

# Função para ordenar produtos por nome
def ordenar_produtos_por_nome():
    produtos_ordenados = sorted(produtos, key=lambda x: x['titulo'])
    for produto in produtos_ordenados:
        print(produto)

# Função para ordenar produtos por preço
def ordenar_produtos_por_preco():
    produtos_ordenados = sorted(produtos, key=lambda x: float(x['preco']))
    for produto in produtos_ordenados:
        print(produto)

# Função para login
def login(nome, senha):
    if nome in usuarios and usuarios[nome][0] == senha:
        print("Login bem-sucedido!")
        return usuarios[nome][1]  # Retorna a permissão do usuário
    print("Nome de usuário ou senha incorretos.")
    return None

# Função para exibir o menu de acordo com o nível de permissão
def exibir_menu(permissao):
    while True:
        if permissao == 'gerente':
            print("1. Adicionar Usuário")
            print("2. Listar Usuários")
            print("3. Atualizar Usuário")
            print("4. Remover Usuário")
            print("5. Adicionar Produto")
            print("6. Listar Produtos")
            print("7. Atualizar Produto")
            print("8. Remover Produto")
            print("9. Buscar Produto")
            print("10. Ordenar Produtos por Nome")
            print("11. Ordenar Produtos por Preço")
            print("12. Sair")
        elif permissao == 'funcionario':
            print("5. Adicionar Produto")
            print("6. Listar Produtos")
            print("7. Atualizar Produto")
            print("8. Remover Produto")
            print("9. Buscar Produto")
            print("10. Ordenar Produtos por Nome")
            print("11. Ordenar Produtos por Preço")
            print("12. Sair")
        elif permissao == 'cliente':
            print("6. Listar Produtos")
            print("9. Buscar Produto")
            print("10. Ordenar Produtos por Nome")
            print("11. Ordenar Produtos por Preço")
            print("12. Sair")
        
        escolha = input("Escolha uma opção: ")

        if permissao == 'gerente':
            if escolha == '1':
                nome = input("Nome: ")
                senha = input("Senha: ")
                permissao_usuario = input("Permissão: ")
                adicionar_usuario(nome, senha, permissao_usuario)
            elif escolha == '2':
                listar_usuarios()
            elif escolha == '3':
                nome = input("Nome: ")
                nova_senha = input("Nova Senha (ou deixe em branco): ")
                nova_permissao = input("Nova Permissão (ou deixe em branco): ")
                atualizar_usuario(nome, nova_senha, nova_permissao)
            elif escolha == '4':
                nome = input("Nome: ")
                remover_usuario(nome)
            elif escolha == '5':
                titulo = input("Título: ")
                autor = input("Autor: ")
                preco = input("Preço: ")
                quantidade = input("Quantidade: ")
                adicionar_produto(titulo, autor, preco, quantidade)
            elif escolha == '6':
                listar_produtos()
            elif escolha == '7':
                titulo = input("Título: ")
                novo_autor = input("Novo Autor (ou deixe em branco): ")
                novo_preco = input("Novo Preço (ou deixe em branco): ")
                nova_quantidade = input("Nova Quantidade (ou deixe em branco): ")
                atualizar_produto(titulo, novo_autor, novo_preco, nova_quantidade)
            elif escolha == '8':
                titulo = input("Título: ")
                remover_produto(titulo)
            elif escolha == '9':
                titulo = input("Título: ")
                buscar_produto(titulo)
            elif escolha == '10':
                ordenar_produtos_por_nome()
            elif escolha == '11':
                ordenar_produtos_por_preco()
            elif escolha == '12':
                break
            else:
                print("Opção inválida!")
        
        elif permissao == 'funcionario':
            if escolha == '5':
                titulo = input("Título: ")
                autor = input("Autor: ")
                preco = input("Preço: ")
                quantidade = input("Quantidade: ")
                adicionar_produto(titulo, autor, preco, quantidade)
            elif escolha == '6':
                listar_produtos()
            elif escolha == '7':
                titulo = input("Título: ")
                novo_autor = input("Novo Autor (ou deixe em branco): ")
                novo_preco = input("Novo Preço (ou deixe em branco): ")
                nova_quantidade = input("Nova Quantidade (ou deixe em branco): ")
                atualizar_produto(titulo, novo_autor, novo_preco, nova_quantidade)
            elif escolha == '8':
                titulo = input("Título: ")
                remover_produto(titulo)
            elif escolha == '9':
                titulo = input("Título: ")
                buscar_produto(titulo)
            elif escolha == '10':
                ordenar_produtos_por_nome()
            elif escolha == '11':
                ordenar_produtos_por_preco()
            elif escolha == '12':
                break
            else:
                print("Opção inválida!")
        
        elif permissao == 'cliente':
            if escolha == '6':
                listar_produtos()
            elif escolha == '9':
                titulo = input("Título: ")
                buscar_produto(titulo)
            elif escolha == '10':
                ordenar_produtos_por_nome()
            elif escolha == '11':
                ordenar_produtos_por_preco()
            elif escolha == '12':
                break
            else:
                print("Opção inválida!")

# Função principal
def main():
    carregar_dados()
    while True:
        print("Bem-vindo ao sistema da Livraria Online!")
        nome = input("Nome de usuário: ")
        senha = input("Senha: ")
        permissao = login(nome, senha)
        if permissao:
            exibir_menu(permissao)
            break

if _name_ == "_main_":
    main()
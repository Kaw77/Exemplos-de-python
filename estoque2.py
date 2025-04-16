# Sistema de Gerenciamento de Peças e Produtos Montados

# Dicionário para armazenar as peças (estoque)
estoque_pecas = {
    # 'código': {'descricao': '', 'preco': 0.0, 'quantidade': 0}
}

# Dicionário para armazenar os produtos (receitas)
produtos = {
    # 'código': {'descricao': '', 'pecas': {}, 'custo_producao': 0.0}
}

def cadastrar_peca():
    print("\n" + "="*40)
    print("CADASTRO DE PEÇA".center(40))
    print("="*40)
    
    codigo = input("Código da peça: ").upper()
    if codigo in estoque_pecas:
        print("Peça já cadastrada! Atualizando dados...")
    
    descricao = input("Descrição: ")
    preco = float(input("Preço unitário R$: "))
    quantidade = int(input("Quantidade em estoque: "))
    
    estoque_pecas[codigo] = {
        'descricao': descricao,
        'preco': preco,
        'quantidade': quantidade
    }
    print(f"Peça {codigo} cadastrada/atualizada com sucesso!")

def cadastrar_produto():
    print("\n" + "="*40)
    print("CADASTRO DE PRODUTO".center(40))
    print("="*40)
    
    codigo = input("Código do produto: ").upper()
    if codigo in produtos:
        print("Produto já cadastrado! Atualizando dados...")
    
    descricao = input("Descrição do produto: ")
    
    # Cadastro das peças necessárias
    pecas_produto = {}
    while True:
        print("\nPeças disponíveis:")
        for cod, peca in estoque_pecas.items():
            print(f"{cod} - {peca['descricao']} (R${peca['preco']:.2f})")
        
        cod_peca = input("\nDigite o código da peça (ou 'sair' para finalizar): ").upper()
        if cod_peca == 'SAIR':
            break
        if cod_peca not in estoque_pecas:
            print("Peça não encontrada!")
            continue
        
        quantidade = int(input(f"Quantidade de {estoque_pecas[cod_peca]['descricao']} necessária: "))
        pecas_produto[cod_peca] = quantidade
    
    # Calcula o custo de produção
    custo = 0.0
    for cod_peca, qtd in pecas_produto.items():
        custo += estoque_pecas[cod_peca]['preco'] * qtd
    
    produtos[codigo] = {
        'descricao': descricao,
        'pecas': pecas_produto,
        'custo_producao': custo
    }
    print(f"\nProduto {codigo} cadastrado com sucesso!")
    print(f"Custo de produção: R${custo:.2f}")

def listar_pecas():
    print("\n" + "="*40)
    print("ESTOQUE DE PEÇAS".center(40))
    print("="*40)
    print("{:<10} {:<20} {:>10} {:>10}".format(
        "Código", "Descrição", "Preço", "Estoque"))
    
    for codigo, peca in estoque_pecas.items():
        print("{:<10} {:<20} {:>9.2f} {:>10}".format(
            codigo, peca['descricao'], peca['preco'], peca['quantidade']))

def listar_produtos():
    print("\n" + "="*40)
    print("PRODUTOS CADASTRADOS".center(40))
    print("="*40)
    
    for codigo, produto in produtos.items():
        print(f"\nCódigo: {codigo}")
        print(f"Descrição: {produto['descricao']}")
        print("Peças necessárias:")
        
        for cod_peca, qtd in produto['pecas'].items():
            peca = estoque_pecas[cod_peca]
            print(f"- {peca['descricao']}: {qtd} x R${peca['preco']:.2f} = R${peca['preco'] * qtd:.2f}")
        
        print(f"Custo total de produção: R${produto['custo_producao']:.2f}")

def menu_principal():
    while True:
        print("\n" + "="*40)
        print("SISTEMA DE PRODUÇÃO".center(40))
        print("="*40)
        print("1. Cadastrar peça")
        print("2. Cadastrar produto")
        print("3. Listar peças em estoque")
        print("4. Listar produtos cadastrados")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            cadastrar_peca()
        elif opcao == '2':
            if not estoque_pecas:
                print("Cadastre peças antes de criar produtos!")
            else:
                cadastrar_produto()
        elif opcao == '3':
            if estoque_pecas:
                listar_pecas()
            else:
                print("Nenhuma peça cadastrada ainda!")
        elif opcao == '4':
            if produtos:
                listar_produtos()
            else:
                print("Nenhum produto cadastrado ainda!")
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

# Iniciar o sistema
if __name__ == "__main__":
    menu_principal()

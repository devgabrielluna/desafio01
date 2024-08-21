def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    pessoa = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favoritado": False}
    contatos.append(pessoa)
    print(f"\nContato [{nome_contato}] adicionado com sucesso!")
    return

def ver_lista_contatos(contatos):
    print("\nLista de contatos:\n ")
    for indice, pessoa in enumerate(contatos, start=1):
        status = "✓" if pessoa["favoritado"] else " "
        nome_contato = pessoa["nome"]
        print(f"{indice}. {nome_contato} - Favorito: [{status}]")
    return

def editar_nome(contatos, indice, novo_nome_contato):
    indice_ajustado = int(indice)-1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        contatos[indice_ajustado]["nome"] = novo_nome_contato
        print(f"Contato editado com sucesso!")
    else:
        print("Índice de contato INVÁLIDO!")

def editar_email(contatos, indice, novo_email_contato):
    indice_ajustado = int(indice)-1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        nome_contato = contatos[indice_ajustado]["nome"]
        print(f"O contato {indice}.[{nome_contato}, será modificado!]")
        contatos[indice_ajustado]["email"] = novo_email_contato
    else:
        print("Índice de contato INVÁLIDO!")

def editar_telefone(contatos, indice,novo_telefone_contato):
    indice_ajustado = int(indice)-1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        nome_contato = contatos[indice_ajustado]["nome"]
        print(f"O contato {indice}.[{nome_contato}, será modificado!]")
        contatos[indice_ajustado]["telefone"] = novo_telefone_contato
    else:
        print("Índice de contato INVÁLIDO!")

def marcar_favorito(contatos, indice):
    indice_ajustado = int(indice)-1
    if contatos[indice_ajustado]["favoritado"] == False:
        print(f"\nContato [{indice}] Marcado com Favorito")
        contatos[indice_ajustado]["favoritado"] = True
    else:
        contatos[indice_ajustado]["favoritado"] = False
        print(f"\nContato [{indice}] Desmarcado com Favorito")
    return

def ver_favoritos(contatos):
    print("\n Lista de Favoritos: ")
    for indice, pessoa in enumerate(contatos, start=1):
        if pessoa["favoritado"]:
            status = "✓"
            nome_contato = pessoa["nome"]
            print(f"{indice}. {nome_contato} - Favorito: [{status}]")
    return

def apagar_contato(contatos, indice):
    indice_ajustado = int(indice) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        contatos.pop(indice_ajustado)
        print(f"\nContato [{indice}] removido com sucesso!")
    else:
        print("Índice de contato INVÁLIDO!")
    return  

contatos = []

while True:
    
    print("\nAgenda Telefônica:")
    print("1. Adicionar Contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar Contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Ver Lista de Favoritos")
    print("6. Deletar Contato")
    print("7. Sair")

    escolha = input("\nDigite a sua escolha: ")
    
    if escolha == "1":
        nome_contato = input("\n1. Digite o nome do contato: ")
        email_contato = input("2. Digite o email do contato: ")
        telefone_contato = input("3. Digite o telefone do contato: ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    elif escolha == "2":
        ver_lista_contatos(contatos)
    elif escolha == "3":
        ver_lista_contatos(contatos)
        indice = input("\nDigite o índice do contato que quer modificar: ")
        print("1. Alterar Nome")
        print("2. Alterar Email")
        print("3. Altarar Telefone")
        chave = input("Digite o que quer alterar no contato: ")
        if chave == "1":
            novo_nome_contato = input("Digite o novo Nome do contato: ")
            editar_nome(contatos, indice, novo_nome_contato)
        elif chave == "2":
            novo_email_contato = input("Digite o novo Email do contato: ")
            editar_email(contatos, indice, novo_email_contato)
        elif chave == "3":
            novo_telefone_contato = input("Digite o novo Telefone do contato: ")
            editar_telefone(contatos, indice, novo_telefone_contato)        
    elif escolha == "4":
         ver_lista_contatos(contatos)
         indice = input("Digite o numero do contato que deseja marcar/desmarcar como favorito: ")
         marcar_favorito(contatos, indice)
    elif escolha == "5":
        ver_favoritos(contatos)
    elif escolha == "6":
        ver_lista_contatos(contatos)
        indice = input("Digite o indice do contato que quer deletar: ")
        apagar_contato(contatos, indice)
    elif escolha == "7":
        break

print("Programa Finalizado!")    





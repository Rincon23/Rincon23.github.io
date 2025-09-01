nome = input('Digite o nome: ')
ultimo = len(nome.split()) -1
print("""O primeiro nome é: {}
O ultimo nome é: {}""".format(nome.split()[0],nome.rsplit()[ultimo]))
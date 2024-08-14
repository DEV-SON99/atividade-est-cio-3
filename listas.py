# Criação da lista
lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]

# Imprimir o conteúdo da lista
print("Conteúdo da lista_mesclada:", lista_mesclada)

# Adicionar um elemento à lista usando o método append
lista_mesclada.append(["Lista aninhada"])
print("Conteúdo da lista_mesclada após append:", lista_mesclada)

# Inserir um elemento na posição 4 usando o método insert
lista_mesclada.insert(4, 5)
print("Conteúdo da lista_mesclada após insert:", lista_mesclada)

# Imprimir o tamanho atual da lista
print("Tamanho atual da lista_mesclada:", len(lista_mesclada))

# Remover o item na posição 1
del lista_mesclada[1]
print("Conteúdo da lista_mesclada após remoção do item na posição 1:", lista_mesclada)

# Criar uma nova lista com os itens até a posição 4 da lista anterior
nova_lista_mesclada = lista_mesclada[:4]
print("Conteúdo da nova_lista_mesclada:", nova_lista_mesclada)

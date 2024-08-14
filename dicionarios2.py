# Criação do dicionário inicial
dicionario = {1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}}

# Adiciona novos elementos ao dicionário usando o método update
dicionario.update({
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'portuguesa'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'espanhola'}
})

# Imprime o dicionário recém atualizado
print("Dicionário atualizado:", dicionario)

# Criação de uma cópia do dicionário
dicionario_copia = dicionario.copy()

# Remove um elemento do dicionário original e imprime o elemento removido
elemento_removido = dicionario.pop(1)
print("Elemento removido:", elemento_removido)
print("Dicionário após remoção do elemento com chave 1:", dicionario)

# Remove o último elemento do dicionário original e imprime o elemento removido
ultimo_elemento_removido = dicionario.popitem()
print("Último elemento removido:", ultimo_elemento_removido)
print("Dicionário após remoção do último elemento:", dicionario)

# Remove todos os elementos dos dicionários
dicionario.clear()
dicionario_copia.clear()

# Criação de um novo dicionário usando fromkeys
novos_dicionarios = dict.fromkeys(['a', 'b', 'c'], 'valor_padrao')

# Imprime o conteúdo do novo dicionário usando o método items
print("Conteúdo do novo dicionário (items):", novos_dicionarios.items())

# Imprime apenas as chaves do novo dicionário usando o método keys
print("Chaves do novo dicionário (keys):", novos_dicionarios.keys())

# Imprime apenas os valores do novo dicionário usando o método values
print("Valores do novo dicionário (values):", novos_dicionarios.values())

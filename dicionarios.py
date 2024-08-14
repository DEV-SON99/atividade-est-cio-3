# Criação e inicialização do dicionário
meu_dicionario = {
    1: 'Python',
    2: 'Java',
    3: 'PHP'
}

# Imprimir o conteúdo do dicionário
print("Conteúdo do meu_dicionario:", meu_dicionario)

# Imprimir o tipo de dados do dicionário
print("Tipo de dados de meu_dicionario:", type(meu_dicionario))

print("Valores de linguagem:", [value for key, value in meu_dicionario.items()])

# Imprimir o tamanho do dicionário
print("Tamanho do meu_dicionario:", len(meu_dicionario))

# Criação e inicialização do dicionário aninhado
dicionario_frutas = dict({
    1: {'nome': 'limão', 'tipo': 'ácida'},
    2: {'nome': 'laranja', 'tipo': 'ácida'},
    3: {'nome': 'manga', 'tipo': 'semiácida'},
    4: {'nome': 'maçã', 'tipo': 'semiácida'},
    5: {'nome': 'banana', 'tipo': 'doce'},
    6: {'nome': 'mamão', 'tipo': 'doce'}
})

# Imprimir o valor das chaves "nome" e "tipo" da chave 1
print("Chave 1 - Nome:", dicionario_frutas[1]['nome'])
print("Chave 1 - Tipo:", dicionario_frutas[1]['tipo'])

# Imprimir o valor das chaves "nome" e "tipo" da chave 2
print("Chave 2 - Nome:", dicionario_frutas[2]['nome'])
print("Chave 2 - Tipo:", dicionario_frutas[2]['tipo'])

# Iterar e imprimir os valores de todas as chaves "nome" e "tipo"
for chave, fruta in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {fruta['nome']}, Tipo: {fruta['tipo']}")

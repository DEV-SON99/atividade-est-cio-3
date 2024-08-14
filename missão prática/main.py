# main.py

from operacoes import calcular_media, verificar_reprovacao, formatar_dados_reprovados

# Dados dos alunos e notas
dados_alunos = {
    '001': {'nome': 'Ana', 'notas': [7, 6, 5, 4]},
    '002': {'nome': 'Carlos', 'notas': [5, 5, 5, 5]},
    '003': {'nome': 'Maria', 'notas': [8, 7, 9, 10]},
}

# Calcular média de cada aluno e verificar reprovação
matriculas_reprovados = []
for matricula, info in dados_alunos.items():
    media = calcular_media(info['notas'])
    if verificar_reprovacao(media):
        dados_alunos[matricula]['media'] = media
        matriculas_reprovados.append(matricula)

# Formatar e imprimir os dados dos alunos reprovados
dados_reprovados = formatar_dados_reprovados(dados_alunos, matriculas_reprovados)
for dado in dados_reprovados:
    print(dado)

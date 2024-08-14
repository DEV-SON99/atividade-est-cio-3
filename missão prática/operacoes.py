# operacoes.py

def calcular_media(notas):

    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    
    return media < 6

def formatar_dados_reprovados(dados_alunos, matriculas_reprovados):
    
    resultado = []
    for matricula in matriculas_reprovados:
        aluno = dados_alunos.get(matricula, {})
        nome = aluno.get('nome', 'Desconhecido')
        media = aluno.get('media', 0)
        resultado.append(f'Aluno Reprovado: {nome} – Matrícula: {matricula} – Média Final: {media:.2f}')
    return resultado

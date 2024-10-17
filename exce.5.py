def gerar_boletim(nome, disciplinas, notas, frequencia):
    """Gera um boletim escolar simples em formato de texto.

    Args:
        nome (str): Nome do aluno.
        disciplinas (list): Lista com os nomes das disciplinas.
        notas (list): Lista com as notas do aluno em cada disciplina.
        frequencia (int): Número de dias presentes.

    Returns:
        str: Boletim em formato de texto.
    """

    # Cálculo da média
    media = sum(notas) / len(notas)

    # Verificação da aprovação (simplificada)
    aprovado = True if media >= 7 else False

    # Formatação do boletim
    boletim = f"Boletim do aluno: {nome}\n"
    for disciplina, nota in zip(disciplinas, notas):
        boletim += f"{disciplina}: {nota}\n"
    boletim += f"Frequência: {frequencia} dias\n"
    boletim += f"Média final: {media:.2f}\n"
    boletim += f"Aprovado: {'Sim' if aprovado else 'Não'}"

    return boletim

# Exemplo de uso
nome_aluno = "João da Silva"
disciplinas = ["Português", "Matemática", "História", "Geografia"]
notas = [8.5, 7.0, 9.0, 6.5]
frequencia = 180

print(gerar_boletim(nome_aluno, disciplinas, notas, frequencia))

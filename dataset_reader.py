from collections import defaultdict
import os

def listar_arquivos_diretorio(diretorio):
    grafos = {}

    if not os.path.isdir(diretorio):
        raise ValueError(f"Caminho inválido: {diretorio}")

    for nome in sorted(os.listdir(diretorio)):
        caminho = os.path.join(diretorio, nome)
        if os.path.isfile(caminho):
            grafos[nome] = leitura_matriz_adjacencia(caminho)

    return grafos

def leitura_matriz_adjacencia(arquivo):
    adjacencias = defaultdict(list)
    with open(arquivo, "r") as file:
        for linha in file:
            linha = linha.strip()

            # Ignora cabeçalhos e linhas em branco
            if linha.startswith("%") or linha == '':
                continue

            parte = linha.split()

            if len(parte) < 2:
                continue

            # conversão para índices de base zero
            # i, j = int(parte[0]) - 1, int(parte[1]) - 1
            i, j = int(parte[0]), int(parte[1])

            # ignora o auto loop
            if i != j:
                adjacencias[i].append(j)
                adjacencias[j].append(i)

    # Cria uma lista de adjacências para todos os vétices presentes
    n = max(adjacencias) + 1

    grafo = [adjacencias[i] for i in range(n)]

    print(f"Leitura concluída [{arquivo}]")

    return grafo
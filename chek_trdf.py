# check_trdf.py
import itertools
import networkx as nx

from brkga_trd import BRKGA_TRD

def exact_trdf(G):
    """
    Função exata para encontrar a γtR mínima.
    Retorna:
        best_sol: dict {vértice: valor f(v)}
        best_weight: soma mínima
    """
    n = G.number_of_nodes()
    nodes = list(G.nodes)
    node_to_idx = {v: i for i, v in enumerate(nodes)}

    best_weight = float('inf')
    best_sol = None

    # Gera todas as funções f: V -> {0,1,2}
    for f_tuple in itertools.product([0,1,2], repeat=n):
        f_list = list(f_tuple)
        # Verifica se é TRDF válido
        valid = True
        for i, val in enumerate(f_list):
            if val == 0:
                neighbors = list(G.neighbors(nodes[i]))
                if not any(f_list[node_to_idx[u]] == 2 for u in neighbors):
                    valid = False
                    break
        if valid:
            weight = sum(f_list)
            if weight < best_weight:
                best_weight = weight
                best_sol = {nodes[i]: f_list[i] for i in range(n)}

    return best_sol, best_weight

if __name__ == "__main__":
    graphs = {
        "C5": nx.cycle_graph(5),
        "P5": nx.path_graph(5),
        "K4": nx.complete_graph(4),
        "Star": nx.star_graph(4)
    }

    for name, G in graphs.items():
        sol, w = exact_trdf(G)
        print(f"{name}: γtR = {w}, solução = {sol}")

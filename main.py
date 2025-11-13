from dataset_reader import *
from brkga import BRKGA
# from ga import GA
import guloso_brkga
import artigo_brkga
# import artigo_ga

import time

def run_brkga(grafo, metodo):
    print()
    print(f"Database: {name}")

    n = len(grafo)

    print(f"Metodo utilizado: {metodo}")

    if metodo == "artigo_brkga":
        ag = BRKGA(
            n = n,
            pop_size=int(n/4.4056), 
            elite_frac=0.2, 
            mutant_frac=0.5, 
            generations=1000,
            max_gens_without_improvement=100,
            max_optimal_solution=3,
            print_generations=False
        )
        ag.fitness = artigo_brkga.fitness
        ag.generate_population = artigo_brkga.generate_population_graph(grafo)
        ag.repair = artigo_brkga.repair_graph(grafo)
    elif metodo == "guloso_brkga":
        ag = BRKGA(
            n = n,
            pop_size=int(n/4.4056), 
            elite_frac=0.2, 
            mutant_frac=0.5, 
            generations=1000,
            max_gens_without_improvement=100,
            max_optimal_solution=3,
            print_generations=False
        )
        ag.fitness = guloso_brkga.fitness_guloso(grafo)
    # elif metodo == "artigo_ga":
    #     ag = GA(
    #         n = n,
    #         pop_size=int(n/4.4056), 
    #         elite_frac=0.2262, 
    #         taxa_mutacao=0.057,
    #         tam_torneio=6, 
    #         generations=586,
    #         max_gens_without_improvement=363,
    #         max_optimal_solution=3,
    #         print_generations=True
    #     )
    #     ag.generate_population = artigo_ga.generate_population_graph(grafo)
    #     ag.repair = artigo_ga.repair_graph(grafo)
    else:
        print(f'Método não reconhecido: {metodo}')
        exit(1)

    t0 = time.time()
    w, sol = ag.run()
    t1 = time.time()

    print(f"γtR = {w}")
    print(f'Tempo de processamento: {t1-t0} segundos')

    return {
        'fit': int(w),
        'solucao': sol, 
        'time': t1-t0
    }

if __name__ == "__main__":

    graphs = listar_arquivos_diretorio("datasets/random")

    texto_export = ""

    linha_export = "grafo"

    # metodos = ("artigo_ga", "artigo_brkga", "guloso")
    metodos = ("artigo_brkga", "guloso_brkga")

    for metodo in metodos:
        linha_export += f",{metodo}_fit"
    for metodo in metodos:
        linha_export += f",{metodo}_tempo"

    texto_export += linha_export + '\n'

    for name, graph in graphs.items():

        resultado_artigo_brkga = run_brkga(graph, "artigo_brkga")
        # resultado_artigo_ga = run_brkga(graph, "artigo_ga")
        resultado_guloso = run_brkga(graph, "guloso_brkga")

        # resultados_metodos = (resultado_artigo_ga, resultado_artigo_brkga, resultado_guloso)
        resultados_metodos = (resultado_artigo_brkga, resultado_guloso)

        linha_export = f"{name}"
        for resultados in resultados_metodos:
            linha_export += f",{resultados['fit']}"
        for resultados in resultados_metodos:
            linha_export += f",{resultados['time']}"

        texto_export += linha_export + '\n'

        # break
    
    with open('output.csv', 'w') as output_file:
        output_file.write(texto_export)
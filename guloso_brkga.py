def fitness_guloso(adjacencias):
    """
    Usa cromossomo como chave → ordena vértices → aplica guloso.
    """
    def guloso(chrom):
        n = len(adjacencias)
        rotulos = [None] * n
        
        # 1. Ordena vértices por chave (menor primeiro)
        ordem = sorted(range(n), key=lambda x: chrom[x])
        
        for v in ordem:
            if rotulos[v] is not None:
                continue
                
            # Etapa 1: f(v) = 2
            rotulos[v] = 2
            
            # Etapa 2: vizinho com menor chave → f=1 (apoio)
            vizinhos = adjacencias[v]
            if not vizinhos:
                continue
                
            vj = min(vizinhos, key=lambda x: chrom[x])  # menor chave
            rotulos[vj] = 1
            
            # Etapa 3: todos os outros vizinhos → f=0
            for u in vizinhos:
                if rotulos[u] is None:
                    rotulos[u] = 0
        
        # Preenche vértices não alcançados
        for i in range(n):
            if rotulos[i] is None:
                rotulos[i] = 0
                
        return rotulos, sum(rotulos)
    
    return guloso

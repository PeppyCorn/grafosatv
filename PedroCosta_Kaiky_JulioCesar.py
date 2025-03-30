class Grafo:
    
    def __init__(self):
        self.grafo = {} 
        self.operacoes()
        
    def adiciona_vertice(self, nome):
        if nome not in self.grafo:
            self.grafo[nome] = [] 
        else:
            print(f"Vértice '{nome}' já existe.")

    def remover_vertice(self, nome):
        if nome in self.grafo:
            self.grafo.pop(nome)  
            
            for conexoes in self.grafo.values():
                if nome in conexoes:
                    conexoes.remove(nome)
        else:
            print(f"Vértice '{nome}' não encontrado.")

    def adiciona_aresta(self, origem, destino):
        if origem in self.grafo and destino in self.grafo:
            self.grafo[origem].append(destino)
        else:
            print(f"Erro: Um ou ambos os vértices '{origem}' ou '{destino}' não existem.")

    def remover_aresta(self, origem, destino):
        if origem in self.grafo and destino in self.grafo[origem]:
            self.grafo[origem].remove(destino)
        else:
            print(f"Erro: Aresta '{origem} → {destino}' não encontrada.")

    def mostra_lista(self):
        for vertice, conexoes in self.grafo.items():
            print(f'{vertice}:', ' -> '.join(conexoes) if conexoes else 'Sem conexões')

    def mostra_matriz(self):
        vertices = list(self.grafo.keys())
        print('   ', '  '.join(vertices))
        for v1 in vertices:
            linha = []
            for v2 in vertices:
                linha.append('1' if v2 in self.grafo[v1] else '0')
            print(f'{v1}:', '  '.join(linha))

    def operacoes(self):
        while True:
            print("""
                --- Menu de Operações ---
                [1] - Adicionar Vértice
                [2] - Adicionar Aresta
                [3] - Remover Vértice
                [4] - Remover Aresta
                [5] - Mostrar Lista de Adjacência
                [6] - Mostrar Matriz de Adjacência
                [0] - Sair
                """)
            
            op = int(input('Digite a opção desejada: '))
            if op == 1:
                nome = input('Digite o nome do vértice: ')
                self.adiciona_vertice(nome)
            elif op == 2:
                origem = input('Digite o nome do vértice de origem: ')
                destino = input('Digite o nome do vértice de destino: ')
                self.adiciona_aresta(origem, destino)
            elif op == 3:
                nome = input('Digite o nome do vértice a ser removido: ')
                self.remover_vertice(nome)
            elif op == 4:
                origem = input('Digite o nome do vértice de origem: ')
                destino = input('Digite o nome do vértice de destino: ')
                self.remover_aresta(origem, destino)
            elif op == 5:
                self.mostra_lista()
            elif op == 6:
                self.mostra_matriz()
            elif op == 0:
                break


Grafo()
import networkx as nx

class Vertice:
     ### Constructor
    def __init__(self,i):
        self.id = i
        self.scan = False
        self.label = 0
        self.vecinos = []
        self.padre = None
    
    def agregar_vecino(self,v,p):
        if v not in self.vecinos:
            self.vecinos.append([v,p])
    
    def quitar_vecino(self,v):
        if v in self.vecinos:
            self.vecinos.remove(v)


class Grafica:
    
    ### Constructor
    def __init__(self):
        self.vertices={} ###diccionario
        
    def aristas(self):
        edge_lst = [] 
        for u in self.vertices:
            for v in self.vertices[u].vecinos:
                    edge_lst.append([u,v[0]])

        edges = {tuple(sorted(e)) for e in edge_lst}
        return list(edges)

    def info(self):
        n = len(self.vertices)
        edges = self.aristas()
        m = (len(edges))//2
        print("La gráfica tiene "+str(n)+" vértices y "+str(m)+" aristas.")

    def reiniciar_grafica(self):
        self.vertices.clear()

        for u in self.vertices:
          self.vertices[u].vecinos.clear()
    
    def agregar_vertice(self,v):
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)
    
    def agregar_arista(self,a,b,p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregar_vecino(b,p)
            self.vertices[b].agregar_vecino(a,p)
            #e = self.Arista(a, b, x)
    
    def aristas_incidentes(self,v):
        if v in self.vertices:
            edges=[]
            for vecino in self.vertices[v].vecinos:
                edges.append([v,vecino])
        return edges
 
    def quitar_arista(self,a,b,p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].quitar_vecino([b,p])
            self.vertices[b].quitar_vecino([a,p])
    
    ### Nos ayuda a quitar las aristas del árbol generadas por sfs_tree
    def quitar_arbol(self,lista):
        for i in range(0, len(lista)-1,3):
            self.quitar_arista(lista[i],lista[i+1],lista[i+2])
            
    #### Solo ayuda para saber quien es el papá de los vértices en sfs        
    def imprimir_grafica(self,r):
        for v in self.vertices:
            print("El papá del vértice "+str(v)+ " es " + str(self.vertices[v].padre))
            
            
    def maximo(self, lista):
        if len(lista)>0:
            m = self.vertices[lista[0]].label ### label del primer elemento de la lista
            
            v = lista[0]
            
            for e in lista:
                if m < self.vertices[e].label:
                    m = self.vertices[e].label
                    v = e
            
            return v
    ### Puede ser reutilizada para k-sfs
    def sfs(self,r):
        
        if r in self.vertices and len(self.vertices[r].vecinos) > 0:
            
            no_scan = []
            actual = r
            
            for v in self.vertices:
                self.vertices[v].padre = None
                no_scan.append(v)
            
            while len(no_scan) > 0:
                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].label == 0:
                        self.vertices[vecino[0]].padre = actual
                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[actual].label == self.vertices[vecino[0]].label:
                        self.vertices[actual].label += 1
                    
                    self.vertices[vecino[0]].label += 1
                
                self.vertices[actual].scan = True
                no_scan.remove(actual)
                
                actual = self.maximo(no_scan)
        else: 
            
            return False
        
    def sfs_tree(self,g):
        t = Grafica()
        edge_list=[]
        edge_plain=[]
    
        for v in g.vertices:
            t.agregar_vertice(v)
        for v in t.vertices:
            t.agregar_arista(v,g.vertices[v].padre,1)
    
        for u in t.vertices:
            for v in t.vertices[u].vecinos:
                edge_list.append((u,v[0]))
                edge_list.append(1)
        for u in t.vertices:
            for v in t.vertices[u].vecinos:
                edge_plain.append(u)
                edge_plain.append(v[0])
                edge_plain.append(v[1])
        
        return t, edge_list,edge_plain
        
    def ni_search(self,r):
        
        if r in self.vertices and len(self.vertices[r].vecinos) > 0:
            
            no_scan_vertices = []
            actual = r
        
        for v in self.vertices:
                no_scan_vertices.append(v)
        
        
        while len(no_scan_vertices) > 0:
            for vecino in self.vertices[actual].vecinos:
                if self.vertices[vecino[0]].scan == False:
                    vecino[1] = (self.vertices[vecino[0]].label) + 1
                
                if self.vertices[actual].label == self.vertices[vecino[0]].label:
                    self.vertices[actual].label += 1
                    
                self.vertices[vecino[0]].label += 1
                
            self.vertices[actual].scan = True
            no_scan_vertices.remove(actual)
                
            actual = self.maximo(no_scan_vertices) 
            
        else:
            
            False

    def ni_edges(self):
      edge_list=[]
      
      for u in self.vertices:
        for v in self.vertices[u].vecinos:
            if v[1]>0:
                edge_list.append([u,v[0]])
                edge_list.append(v[1]) ### v[1] se guarda el rank de la arista [u,v]
    
      return edge_list

def sfs_tree(g):
    t = Grafica()
    edge_list=[]
    edge_plain=[]
    
    for v in g.vertices:
        t.agregar_vertice(v)
    for v in t.vertices:
        t.agregar_arista(v,g.vertices[v].padre,0)
        
    for u in t.vertices:
        print(u,t.vertices[u].vecinos)
    
    for u in t.vertices:
        for v in t.vertices[u].vecinos:
            edge_list.append((u,v))
    
    for u in t.vertices:
        for v in t.vertices[u].vecinos:
            edge_plain.append(u)
            edge_plain.append(v)
    
    return t, edge_list,edge_plain

def nueva_grafica(G):
    H = Grafica()

    for v in G.vertices:
        H.agregar_vertice(v)

    for u in G.vertices:
        for v in G.vertices[u].vecinos:
            H.agregar_arista(u,v[0],v[1])
    return H


### Esta función permite convertir una gráfica de Networkx a una Grafica() para correr ni_search
### en el vértice v_0 y nos regresa una gráfica de Networkx H cuyos pesos representan las etiquetas
def nx_ni_search(Gnx, v_0):
    G_1 = Grafica()
    
    for i,j in Gnx.edges:
        G_1.agregar_vertice(i)
        G_1.agregar_vertice(j)
        G_1.agregar_arista(i,j, 0)
    
    G_1.ni_search(v_0)
    busqueda_ni = G_1.ni_edges()
    
    H = nx.Graph()
    
    for i in range(0, len(busqueda_ni), 2):
        H.add_edge(busqueda_ni[i][0], busqueda_ni[i][1], weight=busqueda_ni[i+1])
    
    return H

### Esta función permite convertir una gráfica de Networkx a una Grafica() para correr sfs
### en el vértice v_0 y nos regresa una gráfica de Networkx H que representa al árbol sfs.
def nx_sfs(Gnx, v_0):
    
    G_1 = Grafica()
    
    for i,j in Gnx.edges:
        G_1.agregar_vertice(i)
        G_1.agregar_vertice(j)
        G_1.agregar_arista(i,j, 0)
    
    G_1.sfs(v_0)

    sfs1,lista_aristas1,c= sfs_tree(G_1)
    edges1 = sfs1.aristas()
    
    H = nx.Graph()
    
    for i in range(0, len(edges1)):
      H.add_edge(edges1[i][0], edges1[i][1])
    
    return H
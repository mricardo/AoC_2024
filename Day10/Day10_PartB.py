def find(num, elements):
    try:
        return elements.index(num)
    except ValueError:
        return -1

def build_search_radius(i, j, graph):
    nodes = []    

    if i + 1 < len(graph):
        nodes.append((i+1, j))
    if i - 1 >= 0:
        nodes.append((i-1, j))
    if j + 1 < len(graph[0]):
        nodes.append((i, j + 1))
    if j - 1 >= 0:
        nodes.append((i, j - 1))
    
    return nodes

def graph_transversal(roots, graph):
    total_roots = 0
    paths = {}     

    transversed_graph = [['.'] * len(graph[0]) for _ in range(len(graph))]
    nines = {}

    while total_roots < len(roots):
        root = roots[total_roots]        
        paths[root] = []

        nodes_to_walk = []
        nodes_to_walk.append((0, root[0], root[1]))
        transversed_graph[root[0]][root[1]] = 0    

        while len(nodes_to_walk) > 0:
            (current_node_value, i, j) = nodes_to_walk.pop(0)
                                              
            search_radius = build_search_radius(i, j, graph)     

            for next_node in search_radius:
                if graph[next_node[0]][next_node[1]] == '.':
                    continue

                next_node_value = int(graph[next_node[0]][next_node[1]])                
                                 
                if next_node_value - int(current_node_value) == 1:                    
                    node_to_walk = (next_node_value, next_node[0], next_node[1])
                   
                    nodes_to_walk.append(node_to_walk)
                    
                    key = (next_node[0], next_node[1])
                        
                    if next_node_value == 9:
                        if (transversed_graph[next_node[0]][next_node[1]] == 9):
                            nines[key] += 1
                        else:
                            nines[key] = 1
                                                                
                    transversed_graph[next_node[0]][next_node[1]] = next_node_value
        
        total_roots += 1

    return nines, transversed_graph
    
if __name__ == "__main__":
    filename = "Day10_input.txt"

    map = {}

    with open(filename, 'r') as f:
        lines = f.readlines()

        roots = []
        graph = []
        for i, line in enumerate(lines):
            elements = list(line.strip())
            graph.append(elements)

            for j, item in enumerate(elements):
                if item == '0':
                    roots.append((i, j))
                
        nines, transversed_graph = graph_transversal(roots, graph)        
        
        individual_paths = 0
        for key, value in nines.items():            
            individual_paths += value
        
        print ("Total individual paths: ", individual_paths)
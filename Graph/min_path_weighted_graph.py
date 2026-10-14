
def weighted_graph_min_path(graph, src, dst):
    return min_path(graph,src,dst, set())


def min_path(graph, src, dst, visited):
    if src == dst:
        return 0
    # to avoid visiting a path, we can setup an extrenmely long value    
    if src in visited:
        return float('inf')
    visited.add(src)
    min_weight = float('inf')
    for neighbour in graph[src]:
        weight = graph[src][neighbour]
        total_weight = weight + min_path(graph, neighbour, dst, visited)
        if total_weight < min_weight:
            min_weight = total_weight
    visited.remove(src)
    return min_weight
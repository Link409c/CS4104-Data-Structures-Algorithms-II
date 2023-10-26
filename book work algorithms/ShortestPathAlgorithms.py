"""Dijkstra's Algorithm for computing the shortest paths
in a weighted graph with no negative cycles."""

# def dijkstra():

def dagShortestPaths(G, w, s):
    """
    computes the shortest paths in a directed acyclic graph represented
    by an adjacency list, using the Relax function to ease the paths between
    each vertex.
    """
# topologically sort the vertices of G
# initialize the single-source Graph (G, s)
# for each vertex u in G.V, taken in topologically sorted order,
    # for each vertex v in G.adj[u]
        # Relax(u, v, w)
    return None
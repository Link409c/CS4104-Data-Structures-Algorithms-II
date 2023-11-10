from graphshw import WeightedGraph
import random
from timeit import timeit

# Student Name: Christian Simpson
#
# Programming Assignment 3
#
# Do not remove this comment that contains the detailed assignment instructions.
#
# What to Submit: Submit the following files once you complete
# the assignment:
# (a) Your modified graphshw.py which has your implementation of Dijkstra's algorithm.
# (b) Your completed shortestpathscomparison.py (don't rename either of these files).
# (c) A text file containing the table of timing results generated by the function
#     you implemented in step 2 of the assignment (see below).
# (d) Your answers to the questions from step 5 should either be in comments in this
#     file or a separate text file.
# (e) If you do the extra credit part, then make sure you include the additional .py
#     file with your extra credit solution, as well as your parser from assignment 2
#     (so I don't have to track it down again--actually I won't track it down, if you don't
#     include it with your submission I simply won't look at your extra credit).
# (f) You do NOT need to submit the other .py files that graphshw.py imports.  I gave
#     them to you. You are not modifying them. So I already have them.
#
# Do the following:
# (1) Implement Dijkstra's algorithm inside the _dijkstra method within the WeightedGraph
#    class of graphshw.py. Do not change the method name, its parameters, etc. See
#    comments inside that method for details.
#
# (2) Implement the time_shortest_path_algs function later in this file to do the following:
#     -- Call random_weighted_graph that I provided below to generate a random 
#        weighted graph with 64 vertices and 2016 edges (i.e., completely connected--all
#        possible undirected edges, other than loops) and weights random in interval
#        1 to 100 inclusive.
#     -- Read documentation of timeit (https://docs.python.org/3/library/timeit.html)
#        And also watch the videos I posted explaining its usage.
#     -- Use timeit to time two versions of Dijkstra's algorithm, specifically
#        the method, _dijkstra, that you implemented is called by dijkstra_binheap and
#        dijkstra_array. The dijkstra_binheap method passes a binary heap implementation
#        of a priority queue to your _dijkstra method. And dijkstra_array passes a simple
#        array implementation of a priority queue. Time both of these on this random graph.
#        I already imported the graphshw module at the top.
#     -- The number parameter to timeit controls how many times the thing you're
#        timing is called. To get meaningful times, you will need to experiment with this
#        a bit. E.g., increase it if the times are too small.  Use the same
#        value of number for timing both versions of Dijkstra's Algorithm.
#        IMPORTANT: Definitely don't use the default value of number, which is
#        something like 1000000 (e.g., the sun might explode before your program
#        finishes on the larger graphs below if you leave it at 10000000).
#     -- Make sure you don't include the time to generate the weighted graph in your
#        times.
#     -- Now repeat this for a graph with 128 vertices and 8128 edges.
#     -- Now repeat this for a graph with 256 vertices and 32640 edges.
#     -- Now repeat this for a graph with 512 vertices and 130816 edges.
#     -- Now repeat this for a graph with 1024 vertices and 523776 edges.
#     -- Repeat this again for 64 vertices and 128 edges.
#     -- Repeat yet again with 128 vertices and 256 edges.
#     -- Repeat yet again with 256 vertices and 512 edges.
#     -- Repeat yet again with 512 vertices and 1024 edges.
#     -- Repeat yet again with 1024 vertices and 2048 edges.
#    
#     -- Have the time_shortest_path_algs function output the timing data in a
#        table, with columns for number of vertexes, number of edges, time for the
#        binary heap version of Dijkstra, and time for the array version of Dijkstra.
#     -- If you want, you can include larger graphs.
#        The pattern I used when indicating what size to use:
#        Dense graphs: v, e=v*(v-1)/2.
#        Sparse: v, e=2*v.
#        For example, if you want to continue the experimentation with
#        larger graphs, you might
#        try 2048 vertices with 2096128 edges (dense graph),
#        2048 vertices with 4096 edges (sparse).
#     -- When you are timing the algorithms you can pass whatever vertex id you
#        want as the source vertex.  It shouldn't affect the runtime by much,
#        if at all. The random weighted graphs are such that there exists paths
#        to any destination from any source, even the sparse graphs, so timing
#        data shouldn't be affected much by source vertex.
#
# (3) Write some code in the if main block at the bottom of this file
#     to test that your Dijkstra implementation works correctly. You will actually
#     need to call dijkstra_binheap and dijkstra_array, and not your _dijkstra directly.
#     I suggest constructing a WeightedGraph from one of the textbook examples since you
#     know the correct solution to those. If g is a WeightedGraph, you can call
#     dijkstra_binheap with a source vertex of 0, with something like:
#     result = g.dijkstra_binheap(0), and similarly for dijkstra_array.
#
# (4) After that code, but in your if main block, call your function that
#     generates the timing data. Make sure you save that output to a text file.
#     If you run in IDLE, then just copy and paste from the shell into a text file.
#     If you run from the command line, you can just redirect the output to a text file.
#
# (5) Once you have the timing data, answer these questions, either right here in comments
#     or as a separate text file:
#     (a) Given the asymptotic runtimes (i.e., the big-O analysis) for the two versions
#         of Dijkstra's Algorithm, when should you expect Dijkstra with a binary heap
#         to be faster (e.g., in terms of graph density)? When should Dijkstra with a simple
#         array to be faster (e.g., in terms of graph density)? This question concerns the
#         Big-O runtimes of the algorithms, and not your timing data.
#     (b) Does graph density affect performance? In other words, using your timing data,
#         was one algorithm faster for dense graphs, but the other for sparse graphs? Or
#         was the same algorithm faster in both cases?
#     (c) Does size, in number of vertexes of the graph, affect performance? In other words,
#         using your timing data, was one algorithm always faster than the other? Or was one
#         faster for a low number of vertexes and the other faster when the number of vertexes
#         was higher?
#     (d) Are your timing results consistent with your answer to question (a)?
#         If not, what do you think caused the discrepancy?
#
#  Answers for (5):
#       (a)
#       (b)
#       (c)
#       (d)
#
# (6) OPTIONAL STEP (up to 15 points extra credit): In programming assignment 2, you
#     implemented a parser for some highway graph data files. Implement another python
#     module (i.e., another .py file) with an if main block where you: (a) get a highway
#     graph filename from the command line, (b) use your parser from assignment 2 to get a
#     WeightedGraph (you'll need an import statement for your parser), and (c) use either
#     version of Dijkstra to compute the Single Source Shortest Paths for the source
#     vertex of your choice.

def random_weighted_graph(v,e,min_w,max_w) :
    """Generates and returns a random weighted
    graph with v vertices and e different edges.

    Keyword arguments:
    v - number of vertices
    e - number of edges
    min_w - minimum weight
    max_w - maximum weight
    """

    edges = [ (random.randrange(0,i),i) for i in range(1,v) ]

    # if desired number of edges greater than length of current edge list, then add more edges
    if e > len(edges) :
        edgeSet = { x for x in edges }
        notYetUsedEdges = [ (y,x) for x in range(1,v) for y in range(x) if (y,x) not in edgeSet ]
        random.shuffle(notYetUsedEdges)
        count = e - len(edges)
        count = min(count, len(notYetUsedEdges))
        for i in range(count) :
            edges.append(notYetUsedEdges.pop())

    # generate random edge weights
    weights = [ random.uniform(min_w, max_w) for x in range(len(edges)) ]

    # construct a Digraph with the lists of edges and weights generated
    G = WeightedGraph(v, edges, weights)
    return G


def time_shortest_path_algs() :
    """Generates a table of timing results comparing two versions of Dijkstra"""
    # create a list of the edge / vertex numbers in tuples to generate each graph
    graph_params = [(128, 8128), (256, 32640), (512, 130816), (1024, 523776), (64, 128),
                    (128, 256), (256, 512), (512, 1024), (1024, 2048)]
    # create a list of random upper bounds for edge weights
    edge_weights = [10, 20, 30, 40, 50, 60]
    # create a list to hold tuples of graph elements and runtimes to return
    results = []
    # number of runs of each algorithm
    num_runs = 1
    # initialize globals for timeit
    def graphParams():
        # use for setup parameter of timeit
        nonlocal vertices
        nonlocal edges
        nonlocal G
    def arrayTimeParams():
        # use for first parameter when timing array based
        nonlocal G
        nonlocal dijkstraArrayPaths
        dijkstraArrayPaths = G.dijkstra_array(0)
    def binHeapTimeParams():
        # use for first parameter when timing binary heap based
        nonlocal G
        nonlocal dijkstraBinHeapPaths
        dijkstraBinHeapPaths = G.dijkstra_binheap(0)

# for each tuple in the list of graph parameters,
    for i in range(len(graph_params)):
        # get the vertex and edge counts
        vertices, edges = graph_params[i].__iter__()
        # call the random weighted graph function to generate a graph of those parameters
        G = random_weighted_graph(vertices, edges, 1, edge_weights[random in range(len(edge_weights))])
        # initialize timeit parameters
        # calculate runtimes using the array and binheap functions
        arrayTime = timeit(arrayTimeParams, setup=graphParams, number=num_runs)
        binHeapTime = timeit(binHeapTimeParams, setup=graphParams, number=num_runs)
        # add the vertices, edges, array time, binheap time to a tuple in that order
        # add the tuple to the list to return
        results.append((vertices, edges, arrayTime, binHeapTime))
    # return the list of runtime results in a loop to be printed
    return results

if __name__ == "__main__" :
    # Here is where you write some code to test that your algorithms
    # are correct.
    #
    # It is also where you will call your time_shortest_path_algs function.
    # Don't forget to save output to a text file.
    #
    # create a file to hold output
    # create a string for table header (vertices, edges, array time, binheap time)
    # add table header to the file
    # print table header
    # call time_shortest_path_algs to populate the runtimes list
    # for each tuple in the runtime list,
        # add tuple values to the file
        # print the values in order of the header
    #
    pass

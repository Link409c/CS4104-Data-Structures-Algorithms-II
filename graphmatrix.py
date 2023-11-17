# Student Name: Christian Simpson
#
# Programming Assignment 4
#
# Do not delete this comment containing the assignment instructions.
#
# What to Submit: Submit the following files once you complete
# the assignment:
# (a) This file: graphmatrix.py
# (b) If you do the extra credit part, then please include a
#     a specific highway graph that you used when you tested your
#     implementation (the actual highway graph file). They sometimes
#     update the data in those files, so I want to make sure I
#     have exactly what you tested with.
#
# A few notes before you begin:
#
# - As in previous assignments, you are not allowed to change the
#   names of files, classes, methods, parameters, etc. If you are wondering
#   why I have this requirement, it is because you will often find
#   yourself (such as in future jobs) tasked with implementing an
#   interface designed by someone else.  For example, in a large project,
#   smaller groups may be tasked with developing smaller parts of a
#   much larger system after the interface has been defined.  If you
#   change part of the interface without consulting the team as a
#   whole, you will break the entire system.  It is also common in
#   test-driven development for a different team to implement the
#   test cases in code from the interface alone.
#   In homework assignments, if you change the interface that I provided
#   (i.e., names of classes, methods, parameters, etc), then the
#   larger system you are breaking is the system comprised of your
#   algorithm implementations along with my test cases that I use when
#   grading.  If I have to either modify your code or my test cases
#   when grading your assignment, then you lose significant points.
#
# - You are also not allowed to change the names of any attributes
#   that I provided, which in this case is simply _W, although in your
#   code you will need to remember to use the self reference to
#   access it, such as with self._W
#
# - Also, as in the previous assignments, don't delete the docstrings
#   (the multiline strings at the start of functions and methods).
#
# Do the following:
#
# 1) Implement the initializer in the WeightedAdjacencyMatrix class,
#    which should create a matrix (i.e., Python list of Python lists) with
#    number of rows and columns both equal to size (i.e., number of vertexes).
#    Carefully read the docstring that I have for the __init__ which explains
#    the parameters.  If edges and weights are empty lists, then the
#    graph should initially have no edges.  Otherwise, initialize it
#    with the edges and weights indicated by those lists.
#    Once the __init__ is complete, the diagonal of the matrix should have
#    all 0s.  For each edge in the edge list, with corresponding weight
#    from the weights list, you should have the weight in 2 positions in
#    the matrix (remember for an undirected graph, the matrix is
#    symmetric).  For all non-edges (other than the diagonal) you must
#    have infinity, which is math.inf in Python (make sure you add the
#    import you need for that at the top).
#
#    Use the attribute I provided in __slots__ for your matrix _W (see
#    comment above). Remember to use self when referencing an object
#    attribute (i.e., self._W). Although in Java, you can often omit
#    Java's "this", in Python you cannot omit self.
#
#    You can delete the pass statement I have in there.  It is just a
#    placeholder until you have implemented this.
#
#    Read the instructions for step 2 before doing step 1.  You will find
#    it useful to have your __init__ call your add_edge implemented in
#    step 2, which will make step 3 of the assignment much easier.
#
#    Hint 1: Have your __init__ start by initializing a 2D list
#            of the appropriate size, with 0s on the diagonal and
#            infinity everywhere else.  And then have it iterate
#            over the edges calling add_edge for each edge, weight pair.
#            This will make doing step 3, with the inheritance as easy
#            as overriding add_edge, without need to override __init__
#
# 2) Implement the add_edge method of the WeightedAdjacencyMatrix class,
#    as specified in its docstring.
#    It is an undirected edge, so you'll need to set two different cells
#    of the matrix (for an undirected graph, the matrix is symmetric
#    as mentioned above).
#
#    You can delete the pass statement I have in there.  It is just a
#    placeholder until you have implemented this.
#
# 3) Override add_edge in the WeightedDirectedAdjacencyMatrix class
#    according to the docstring I've inserted in that method below.
#    Also either ensure that the __init__ from step 1 will work as is
#    in the case of a directed graph, or override it in the
#    WeightedDirectedAdjacencyMatrix so that it correctly handles the
#    directed edge case.  If you followed Hint 1 above, then you will NOT
#    need to override __init__.  And following Hint 1 is the easiest way
#    to get this to work correctly.
#
#    You can delete the pass statement I have in there.  It is just a
#    placeholder until you have implemented this.
#
#    Hint 3: Although defined in the parent class, you are able to directly
#            access _W with self._W in the WeightedDirectedAdjacencyMatrix
#            class since nothing is truly private in Python.
#
# 4) Implement the floyd_warshall method in the WeightedAdjacencyMatrix class.
#    Since it is in the parent class, you'll be able to use it with either
#    undirected or directed graphs.  Read the docstring for details of what to
#    implement.
#
#    Your method MUST NOT change self._W. So make sure when you initialize
#    D, that you make a copy of self._W.  Do NOT do: D = self._W.  That
#    doesn't copy the list, it just assigns an additional reference to it.
#    So, changing D would change self._W.  Also, do NOT do: D = self._W[:].
#    That only does a shallow copy.  Since _W is a 2D list, that will only
#    copy the first dimension.  The first dimension contains references
#    to 1D list objects, so although D will be a different list than _W,
#    D[i] will be a reference to the same list object as self._W[i],
#    so changing D[i][j] will change self._W[i][j].  You need to do a
#    deep copy. To get this correct, you will either need to write a loop
#    that does a slice on each row to copy the rows one at a time. Or
#    try importing Python's copy module, and take a look at the documentation
#    of the functions in the copy module. One of them will do the deep copy
#    that you need.
#
# 5) Implement the function test_floyd_warshall to test your implementation.
#    Your test should construct a WeightedAdjacencyMatrix object, call the
#    floyd_warshall method to compute all pairs shortest paths, and then
#    output the result with print statements.  Make sure you use a case
#    that you know the correct solution, such as a small graph where you
#    compute the solution by hand (perhaps the problem from the problem set)
#    or an example from the textbook might be good since you know the correct
#    solution to that from the book. You can just call the function from the
#    shell. You don't need to call it from an if main block. The if main
#    block is for something else for extra credit. See #6 below.
#
# 6) EXTRA CREDIT: Implement the parse_highway_graph_matrix function, and the
#    pair_shortest_path function, and the if main block at the bottom according
#    to the docstrings and comments I have there indicating what these should
#    do. The extra credit portion is worth up to 25 points.
import math
import copy
class WeightedAdjacencyMatrix :
    """A weighted graph represented as a matrix."""

    __slots__ = ['_W']

    def __init__(self, size, edges=[], weights=[]) :
        """Initializes a weighted adjacency matrix for a graph with size nodes.

        Graph is initialized with size nodes and a specified set of
        edges and edge weights.
        
        Keyword arguments:
        size -- Number of nodes of the graph.
        edges -- a list of ordered pairs (2-tuples) indicating the
                 edges of the graph.  The default value is an empty list
                 which means no edges by default.
        weights -- a list of weights for the edges, which should be the same
                   length as the edges list.  The position of a value in
                   the weights list corresponds to the edge in the same
                   position of the edges list.
        """
        # initialize _W as a 2D Array of size passed to function
        self._W = [[math.inf for _ in range(size)] for _ in range(size)]
        # populate the matrix
        for _ in range(len(edges)):
            i, j = edges[_].__iter__()
            self.add_edge(i, j, weights[_])

    def add_edge(self, u, v, weight) :
        """Adds an undirected edge between u to v with the specified weight.

        Keyword arguments:
        u -- vertex id (0-based index)
        v -- vertex id (0-based index)
        weight -- edge weight
        """
        # for indexes of same vertex,
        # set diagonal to zero
        if u == v:
            self._W[u][v] = 0
        # else get the appropriate connecting edge weight
        else:
            self._W[u][v] = weight

    def floyd_warshall(self) :
        """Floyd Warshall algorithm for all pairs shortest paths.

        Returns a matrix D consisting of the weights of the shortest
        paths between all pairs of vertices, and a matrix P for
        the predecessors matrix (what the textbook called PI).
        This method MUST NOT change the weight matrix of the graph
        itself.  
        """

        #    Your method MUST NOT change self._W. So make sure when you initialize
        #    D, that you make a copy of self._W.  Do NOT do: D = self._W.  That
        #    doesn't copy the list, it just assigns an additional reference to it.
        #    So, changing D would change self._W.  Also, do NOT do: D = self._W[:].
        #    That only does a shallow copy.  Since _W is a 2D list, that will only
        #    copy the first dimension.  The first dimension contains references
        #    to 1D list objects, so although D will be a different list than _W,
        #    D[i] will be a reference to the same list object as self._W[i],
        #    so changing D[i][j] will change self._W[i][j].  You need to do a
        #    deep copy. To get this correct, you will either need to write a loop
        #    that does a slice on each row to copy the rows one at a time. Or
        #    try importing Python's copy module, and take a look at the documentation
        #    of the functions in the copy module. One of them will do the deep copy
        #    that you need.

        # P 657 Floyd-Warshall Pseudocode
        # P 661 In-Place Floyd Warshall Implementation (23.2-4)

        # get reference for _W size
        listSize = len(self._W)
        # initialize a copy of the _W matrix D(k-1) using deep copy
        D_kMinusOne = copy.deepcopy(self._W)
        # create a new matrix Dk to set new values to
        D_k = [[math.inf for _ in range(listSize)] for _ in range(listSize)]
        # create a new 2D array P
        P = [[math.inf for _ in range(listSize)] for _ in range(listSize)]
        # for range in matrix size
        for k in range(listSize):
            # for i in range size
            for i in range(listSize):
                # for j in range size
                for j in range(listSize):
                    # find the best path between i and j through k
                    oldRef = D_k[i][j]
                    # set Dk[i][j] = min(D(k-1)[i][j], D(k-1)[i][k] + D(k-1)[k][j])
                    D_k[i][j] = min(D_kMinusOne[i][j], D_kMinusOne[i][k] + D_kMinusOne[k][j])
                    # if Dk[i][j] changed,
                    if(D_k[i][j] != oldRef):
                        # new shortest path is found between i and j through k
                        # set new parent of vertex [i][j]
                        # set P[i][j] to k
                        P[i][j] = k
            # set D(k-1) to Dk after iterating over entire matrix
            D_kMinusOne = D_k
        # return Dk and P

        # Your return statement will look something like this one
        # in the comment on the following line.  That returns
        # the two matrices, with the D matrix first.  The return None
        # is just a placeholder so that this is valid Python syntax before
        # you've completed the assignment.  This comment line is
        # more like what it should look like:
        # return D, P

        return D_k, P


class WeightedDirectedAdjacencyMatrix(WeightedAdjacencyMatrix) :
    """A weighted digraph represented as a matrix."""

    def add_edge(self, u, v, weight) :
        """Adds a directed edge from u to v with the specified weight.

        Keyword arguments:
        u -- source vertex id (0-based index)
        v -- target vertex id (0-based index)
        weight -- edge weight
        """
        # for indexes of same vertex,
        # set diagonal to zero
        if u == v:
            self._W[u][v] = 0
        # else get the appropriate connecting edge weight
        else:
            self._W[u][v] = weight

def test_floyd_warshall() :
    """See assignment instructions at top."""
    # create 2 arrays of connected vertex pairs and edge weights
    size = 5
    edges = [[1,2], [1,3], [2,4], [3,4], [4,3], [5, None]]
    weights = [1, 7, 4, 3, 8]
    # initialize a weighted matrix using the arrays
    W = WeightedAdjacencyMatrix(size, edges, weights)
    # create a tuple of D and P list using the floyd warshall function passing the matrix
    D_P = W.floyd_warshall()
    # print the contents of each object in the tuple
    # index 0 is D Matrix, index 1 is P Matrix
    for i in range(len(D_P)):
        for line in D_P[i]:
            for _ in line:
                print(_, end='\t')
            print()
        print()

def parse_highway_graph_matrix(filename) :
    """EXTRA CREDIT: Rewrite your highway graph parser from
    assignment 2 here in this function but return a WeightedAdjacencyMatrix
    object from this function. If you had that assignment working,
    then this part of the extra credit should be very easy (i.e.,
    copying and pasting code and then making very minor adjustments
    to use construct and return a WeightedAdjacencyMatrix object
    instead of the other graph type you already have.

    Keyword arguments:
    filename - the name of a highhway graph file.
    """
    return None # temporary return statement until you implement this.

def pair_shortest_path(D, P, s, t) :
    """EXTRA CREDIT: This function takes D and P matrices (i.e., what is generated
    by floyd_warshall), and a source vertex (where you want to start) and
    destination or target vertex t (where you want to end up) and
    returns a pair: w, path, such that w is the weight of the shortest
    path from s to t (just a simple lookup in the D matrix) and
    path is a Python list of vertex ids starting at s and ending at t
    derived from the P matrix. If no path exists from s to t, then returns
    math.inf for w (which is what D[s][t] should be in that case), and an
    empty list for the path.

    Keyword arguments:
    D - the D matrix
    P - the Pi matrix
    s - the source vertex
    t - the destination vertex
    """
    # Your actual return will look something like this:
    # return w, path
    return None # temporary until you implement this

if __name__ == "__main__" :
    # EXTRA CREDIT: Write code here that:
    #   (a) Gets the name of a highway graph file from the command line
    #       arguments.
    #   (b) Uses parse_highway_graph_matrix from above to parse that file
    #       into a WeightedAdjacencyMatrix object.
    #   (c) Runs the floyd_warshall method on that graph.
    #   (d) Then, prompts the user (use the Python docs to figure out
    #       how to do this) for a source and target vertex, s and t.
    #   (e) Uses pair_shortest_path to get the weight of the shortest
    #       path between their chosen s and t, and the path itself.
    #   (f) Outputs the weight and path.
    #   (g) Repeats d, e, and f in a loop until the user indicates they
    #       want to quit.  You can decide how to get that decision from them.
    test_floyd_warshall()
    




    

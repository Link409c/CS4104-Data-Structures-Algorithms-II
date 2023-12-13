from timeit import timeit
import math
from random import random
from multiprocessing import Pool

# You will need some import statements up here.

# Programming Assignment 5
#
# Student Name: Christian Simpson
#
# Do not delete this comment containing the assignment instructions.
#
# What to submit:
# (a) This montecarlo.py file
#     As always, you are not allowed to change the names of
#     py files I've given you, functions, parameters, etc.
# (b) A text file with the output from when you run your
#     generate_table and time functions.  One text file with
#     both output tables is fine.
#
# 1) Implement the function pi_monte_carlo to estimate
#    the value of pi using Monte Carlo simulation.
#    See the details of how to do this are in Blackboard,
#    which shows pseudocode of the algorithm you are to implement.
#    You will need to import the random module.  Take a
#    look at the documentation of the random module to find
#    the function that generates random floating-point
#    values in the interval [0.0, 1.0).
#
#    IMPORTANT NOTE: Several different Monte Carlo algorithms
#    exist for estimating pi. One of which is described by the
#    pseudocode I have in Blackboard. It happens to be one of
#    the better ones that exist that I have modified slightly
#    to further improve numerical stability, but it is also not
#    the one you would likely find if you attempted to Google
#    for this (even without my modifications). If you implement
#    a different Monte Carlo algorithm for estimating pi other
#    than the one specified in the assignment, then you will
#    lose all points related to this part of the assignment.
#
# 2) Implement a parallel version of this in the function
#    pi_parallel_monte_carlo. The second parameter, processes,
#    indicates how many processes to use. You should use
#    a Pool (see the parallel examples for the import that you
#    will need). The easiest ways to do this is to either use
#    the apply_async method of the Pool class or the map method
#    of the Pool class.
#
#    Hint 1: If you use apply_async, you'll start by determining
#           how many samples per process, which you can compute
#           from n and p.  You would then call apply_async p times
#           to have p processes call pi_monte_carlo (the sequential
#           version) using the number of samples necessary to spread
#           the n samples across p processes. Once you call apply_async
#           p times (make sure you store the Future objects that those
#           calls return in a list), you'll call get() on each of those
#           Future objects, and average the p results.
#
#    Hint 2: If you want to use Pool.map, then start the same
#           way by determining how many samples to use for each
#           process. Create your Pool with p processes.  Generate
#           a list of length p where the elements are the numbers of
#           samples for each process, which should sum to n.
#           Call pool.map (assuming your Pool is named pool) to map
#           your sequential pi_monte_carlo to that list.
#           When pool.map returns, compute the average of the p
#           results and return it.
#
#    Hint 3: Make sure you use a with block for your Pool (see examples
#           in video and corresponding sourcecode) to ensure the Pool
#           is closed properly.
#
# 3) Implement the generate_table function as specified below.
#
# 4) Implement the time function as specified below.
#
# 5) Run your generate_table and time functions from the shell
#    and save the output to a textfile.
#
# 6) Are the results what you expected to see? If so, why?
#    If not, why do you think your results are different
#    then you expected? You can just answer in a comment.
#
# 7) Submit the .py file and the textfile with the output.
def calculateM():
    """Helper method to calculate m, used in
    estimating the value of pi.
    """
    # generate a random float between [0 and 1)
    r = random()
    # square this value
    r = math.pow(r, 2)
    # subtract this value from 1
    r = 1 - r
    # square root the result - this is m
    return math.sqrt(r)
def pi_monte_carlo(n) :
    """Computes and returns an estimation of pi
    using Monte Carlo simulation.

    Keyword arguments:
    n - The number of samples.
    """
    # call calculateM to get an initial value for m
    m = calculateM()
    # loop for k from 2 to n
    for k in range(2, n):
        # add another value of calculateM minus m divided by k to m
        m = m + ((calculateM() - m) / k)
    # return 4m
    return 4 * m

def pi_parallel_monte_carlo(n, p=4) :
    """Computes and returns an estimation of pi
    using a parallel Monte Carlo simulation.

    Keyword arguments:
    n - The total number of samples.
    p - The number of processes to use.
    """
    # get number of samples to dedicate to each process
    samples = n // p
    # make pool object using that number of processes
    with Pool(p) as pool:
        # use pool.map calls to add each result to L
        # pass pi_monte_carlo and the number of samples repeated p times
        L = pool.map(pi_monte_carlo, [samples] * p)
    # after all processes have finished working close the pool
    pool.close()
    # average the list of results
    return sum(L) / p

def generate_table() :
    """This function should generate and print a table
    of results to demonstrate that both versions
    compute increasingly accurate estimations of pi
    as n is increased.  It should use the following
    values of n = {12, 24, 48, ..., 50331648}. That is,
    the first value of n is 12, and then each subsequent
    n is 2 times the previous.  The reason for starting at 12
    is so that n is always divisible by 1, 2, 3, and 4.
    The first column should be n, the second column should
    be the result of calling pi_monte_carlo(n), and you
    should then have 4 more columns for the parallel
    version, but with 1, 2, 3, and 4 processes in the Pool."""
    # create a list to hold values
    L = []
    # start estimation at n = 12
    n = 12
    # for each value of n up to 50331648,
    # (this is 12 * 2^22)
    for i in range(1, 23):
        # call pi_monte_carlo for that n
        estimate_pi = pi_monte_carlo(n)
        # for p in range 1 to 4,
        # call pi_parallel_monte_carlo for that n and p
        par_list = [pi_parallel_monte_carlo(n, p) for p in range(1, 5)]
        # add the list of parallel results to the list
        L.append([[n, estimate_pi, par_list]])
        # double n for the following iteration
        n *= 2
    return L

def time() :
    """This function should generate a table of runtimes
    using timeit.  Use the same columns and values of
    n as in the generate_table() function.  When you use timeit
    for this, pass number=1 (because the high n values will be slow)."""
    # create a list to hold values
    L = []
    # start estimation at n = 12
    n = 12
    # for each value of n up to 50331648,
    # (this is 12 * 2^22)
    for i in range(1, 23):
        # time the normal algorithm
        serial_pi = timeit(lambda: pi_monte_carlo(n), number=1)
        # time the parallel algorithm for 1 - 4 processes as a list
        parallel_pi = [timeit(lambda: pi_parallel_monte_carlo(n, p), number=1) for p in range(1, 5)]
        # add each value to the list
        L.append([serial_pi, parallel_pi])
        # double n for next pass
        n *= 2
    return L

def runAndTimePi():
    """
    Helper function to create the tables and print results.
    """
    # create 2 lists to hold all values
    # call generate_table() and time() to populate the lists
    estimated_pi_values = generate_table()
    algorithm_runtimes = time()
    # print the header
    print("n\tSerial\tParallel (p=1)\tParallel (p=2)\tParallel (p=3)\tParallel (p=4)\t Time: Serial\t"
          "Parallel (p=1)\tParallel (p=2)\tParallel (p=3)\tParallel (p=4)")
    # print the list of results
    for i in range(len(algorithm_runtimes)):
        # print values then times
        print('\t'.join(map(str, estimated_pi_values[i] + algorithm_runtimes[i])))

if __name__ == "__main__":
    # testing table display
    runAndTimePi()

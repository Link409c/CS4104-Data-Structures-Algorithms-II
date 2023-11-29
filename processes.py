# example of multiprocessing in python
from multiprocessing import Pool

# some function
def f(x):
  4*x*x - 2*x + 17  

# call the function on a list of elements
def compute(L):
  return [ f(x) for x in L]

# call the function returning a list using map to apply function to each value
def compute_with_map(L):
  return list(map(f,L)

# call the function returning a list using parallel processes
def compute_with_pool(L, p=4):
  with Pool(p) as processes:
    return list(processes.map(f, L)

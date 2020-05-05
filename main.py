from timeit import default_timer as timer
from copy import copy
import numpy as np
from quicksort import quicksort
from quicksort1 import quicksort as quicksort1
from quicksort2 import quicksort as quicksort2
from quicksort3 import quicksort as quicksort3
from quicksort4 import quicksort as quicksort4
from quicksort5 import quicksort as quicksort5

# Test parameters
array_size = 10000  # size of test array
repeat = 5  # numbers of arrays to test
n_iter = 100  # number of tests for each array

functions = {
    "fonction numpy.sort": lambda x: np.sort(x, kind='quicksort'),
    "Python pur": lambda x: quicksort(x),
    "Cython, quicksort compilé sans indication": lambda x: quicksort1(x),
    "Cython, quicksort avec typage des variables": lambda x: quicksort2(x),
    "Cython, quicksort avec typage des variables et des fonctions": lambda x: quicksort3(x),
    "Cython, quicksort avec typage et décorateurs": lambda x: quicksort4(x),
    "Cython, quicksort avec typage, décorateurs et pointeurs": lambda x: quicksort5(x),
}
times = {k: 0 for k in functions.keys()}

# make tests
for i in range(repeat * n_iter):
    if i % n_iter == 0:  # initiate random array of size array_size if i is a multiple of n_iter
        array = np.random.rand(array_size)
    for f_name, f in functions.items():
        start = timer()
        f(copy(array))  # make a copy to avoid changing the original array
        times[f_name] += (timer() - start) * 1000 / (repeat * n_iter)  # store execution time in ms

# Print results
print(f"Test sur {repeat} listes aléatoires de taille {array_size}, {n_iter} itérations à chaque fois :")
for f_name, t in times.items():
    print(f"\t{np.round(t, 2)} ms par tri pour : {f_name}")
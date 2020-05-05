cimport numpy as np

cdef int partition(np.ndarray[np.float_t, ndim=1] xs, int start, int end):
    cdef int follower
    cdef int leader
    follower = leader = start
    while leader < end:
        if xs[leader] <= xs[end]:
            xs[follower], xs[leader] = xs[leader], xs[follower]
            follower += 1
        leader += 1
    xs[follower], xs[end] = xs[end], xs[follower]
    return follower


cdef void _quicksort(xs, start, end):
    cdef int p
    if start >= end:
        return
    p = partition(xs, start, end)
    _quicksort(xs, start, p - 1)
    _quicksort(xs, p + 1, end)


cpdef void quicksort(xs):
    _quicksort(xs, 0, len(xs) - 1)
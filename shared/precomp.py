import numpy as np
def prcmp(method, init_conditions, diff_fun, stp, frms):
    """
        Precomputes motion for each frame of animation
    """
    dims = sum( ((frms,), init_conditions.shape), ()) # flattening tuples
    motion = np.zeros(dims)

    motion[0] = init_conditions.copy()
    for i in range(1,frms):
        motion[i] = method(i*stp, motion[i-1], stp, diff_fun) 

    return motion



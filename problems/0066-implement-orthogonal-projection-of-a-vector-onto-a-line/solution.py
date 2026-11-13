
def orthogonal_projection(v, L):
    """
    Compute the orthogonal projection of vector v onto line L.

    :param v: The vector to be projected
    :param L: The line vector defining the direction of projection
    :return: List representing the projection of v onto L
    """
    s = sum([v[i] * L[i] for i in range(len(v))])
    l = length(L)
    x = (s / l) 
    return [l * x for l in L]

def length(L):
    return sum([i ** 2 for i in L])
        
        

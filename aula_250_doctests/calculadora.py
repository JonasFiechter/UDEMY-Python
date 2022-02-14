from pydoc import doc


def soma(x, y):
    """ soma x e y

    >>> soma(10, 20)
    30
    >>> soma(-10, 20)
    10
    """
    return x + y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
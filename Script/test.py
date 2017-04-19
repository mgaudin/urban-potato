import doctest

def produit(a,b):
    """
    >>> produit(2,3)
    6
    """
    return a*b
    
def _test():
    "self-test routine"
    # load the doctest module, part of the std Python API
    import doctest
    # invoke the testmod function that will parse
    # the whole content of the file, looking for
    # docstrings and run all tests they contain
    doctest.testmod()
 
POTATO = (1,2)
    
if __name__ == '__main__':
    _test()

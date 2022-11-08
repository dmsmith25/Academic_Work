def iterable_to_string(iterable):
    """
    This function takes an iterable as a parameter and returns
    all of the items in the iterable as one string.
    Inputs: iterable
    """
    string = ''
    for item in iterable:
        string += str(item) + ' '
        
    return string
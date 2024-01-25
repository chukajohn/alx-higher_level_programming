#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer wwith "{:d}".format ()
    Argv:
        value (int): the interger to print

    Return:
        if a TypeError or ValueError occurs - false-
        otherwise - true.
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return (false)

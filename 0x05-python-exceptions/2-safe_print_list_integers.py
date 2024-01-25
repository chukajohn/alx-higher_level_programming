#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """print the first  x elements of a list-

    Args:
        my_list (list): the list to print elements from-
        x (int): the number of elementsof my_list to print-
    Return:
        the number of element printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1

        except IndexError:
            continue
    print("")

    return (ret)

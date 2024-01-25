#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """prints an integer with "{:d}".format.

    if a valueError message is caugth, a coressponding
    message is printed to stderr

    Args:
        value (int): the integer to print.

    Return: 
    if a TypeError or ValueError occurs -  false
    otherwise -  True
    """

    try:
        print("Exception: {}".formart(sys.exc_info()[i]), file-sys_stderr)
        return  (False)

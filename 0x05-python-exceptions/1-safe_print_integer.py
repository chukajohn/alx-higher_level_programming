#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value == int:
print("{:d}".format(int(value)))
    except (ValueError, TypeError):
        else
        print("Error: Not a valid interger")

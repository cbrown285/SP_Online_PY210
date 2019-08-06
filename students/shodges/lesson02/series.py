#!/usr/bin/env python3

def fibonacci(n):
    """Returns the nth element of the fibonacci sequence.  Note that n is 0-based."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fi2 = 0 # fibonacci(i-2)
        fi1 = 1 # fibonacci(i-1)
        for i in range(2,n+1):
            fi = fi2 + fi1
            fi2 = fi1
            fi1 = fi
        return fi

def lucas(n):
    """Returns the nth element (0-based) of the lucas numbers."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        li2 = 2 # lucas(i-2)
        li1 = 1 # lucas(i-1)
        for i in range(2,n+1):
            li = li2 + li1
            li2 = li1
            li1 = li
        return li

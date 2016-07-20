

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"

    length = 1
    while n != 1:
        print(n)
        length += 1
        if n % 2 == 0:
            n =  n // 2




        else:
            n = n*3 + 1

    print(n) 


    return length




a = hailstone(10)
print(a)

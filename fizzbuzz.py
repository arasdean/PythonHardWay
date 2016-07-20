from operator import add, sub


def largest_factor(n):


    fac = []
    for i in range(n):
        try:
            if n % i == 0:
                fac.append(i)
        except:
            if ZeroDivisionError:
                continue
    return max(fac)
print(largest_factor(150))

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return False

def t():
    return 12

def f():
    return 1


print(with_if_function())

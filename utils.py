def sum_tuples(a: (int, int), b: (int, int)):
    return tuple(x + y for x, y in zip(a, b))

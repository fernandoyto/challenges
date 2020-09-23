import numpy

def get_products_of_all_ints_except_at_index(int_list):
    n = len(int_list)
    if n <= 1:
        raise Exception("List must have at least 2 elements")

    results = [0] * n
    
    for i in range(n):
        if i == 0:
            results[i] = numpy.prod(int_list[i + 1:])
        elif i == n - 1:
            results[i] = numpy.prod(int_list[:i])
        else:
            results[i] = numpy.prod(int_list[i + 1:]) * numpy.prod(int_list[:i])

    return results
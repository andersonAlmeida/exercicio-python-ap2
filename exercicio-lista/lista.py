li = []

def test():
    for i in range(10000):
        li.append(i)

def contadorInsert():
    for i in range(10000):
        li.insert(i)


# def test():
#     """Stupid test function"""
#     L = [i for i in range(100)]

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))
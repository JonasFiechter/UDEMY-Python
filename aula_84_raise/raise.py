def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('erro 1', error)
        raise

print(divide(2, 0 ))

def divide2(n1, n2):
    if n2 == 0:
        raise ValueError
    return n1 / n2

print(divide2(5, 0))
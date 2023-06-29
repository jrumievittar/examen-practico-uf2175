def sum(a, b):
    return a + b


def mult(a, b):
    return a * b


def lista(n):
    numeros = []
    for numero in range(n):
        numeros.append(numero)
        return numeros

if __name__ == '__main__':
    print(sum(2, 3))
    print(mult(2, 2))
    print(lista(3))


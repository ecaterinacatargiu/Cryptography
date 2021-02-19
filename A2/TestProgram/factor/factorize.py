from math import sqrt


def getTable(number, iterations):
    ai = []
    bi = []
    xi = []
    square = int(sqrt(number))
    ai.append(square)
    bi.append(square)
    x0 = sqrt(number) - ai[0]
    xi.append(x0)
    for i in range(1, iterations + 1):
        ai.append(int(1 / float(xi[i - 1])))
        xi.append((1 / xi[i - 1]) - ai[i])
        if i == 1:
            bi.append((ai[i] * bi[i - 1] + 1) % number)
        else:
            bi.append((ai[i] * bi[i - 1] + bi[i - 2]) % number)

    return ai, bi


def main():
    print(getTable(7987, 12))


main()






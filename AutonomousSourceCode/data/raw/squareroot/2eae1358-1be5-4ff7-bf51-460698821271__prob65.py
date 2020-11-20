import time


def numberSum(n):
    num_sum = 0
    for m in str(n):
        num_sum += int(m)
    print num_sum


def squareRootConvergentsOfE():
    numretor1, demenator1 = 8, 3
    numretor2, demenator2 = 11, 4
    out_put = 0
    p = 4
    for i in range(5, 101):
        if i % 3 == 0:
            numretor = numretor2 * p + numretor1
            demenator = demenator2 * p + demenator1
            p += 2
        else:
            numretor = numretor2 + numretor1
            demenator = demenator2 + demenator1
        numretor1, demenator1 = numretor2, demenator2
        numretor2, demenator2 = numretor, demenator
        # print numretor2, demenator2
    return numberSum(numretor)

if __name__ == "__main__":
    start_time = time.time()
    squareRootConvergentsOfE()
    print time.time() - start_time, 'Seconds'

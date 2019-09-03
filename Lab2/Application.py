
from Algorithm import Algorithm


if __name__ == '__main__':
    alg = Algorithm()
    method = alg.run()
    list = []
    for i in range(0, 30):
        print("This was iteration ", i + 1)
        algorithm = Algorithm()
        list.append(algorithm.run())
    algorithm.statistics(list)



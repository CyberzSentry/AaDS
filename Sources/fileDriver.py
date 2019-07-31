import random
import numpy as np


def getArray():
    file = open("./input.txt", "r")
    values = file.read().split(' ')
    result = list(map(int, values))
    file.close()
    return result


def getIntArrayPath(path):
    file = open(path, "r")
    values = file.read().splitlines()
    result = list(map(int, values))
    file.close()
    return result


def getStringArrayPath(path):
    file = open(path, "r")
    values = file.read().splitlines()
    file.close()
    return values


def generateRandoms(n, m):
    file = open("./input.txt", "w")
    file.truncate(0)
    file.write(str(random.randint(0, m)))
    for n in range(n - 1):
        file.write(" " + str(random.randint(0, 100)))
    file.close()


def readWords(n):
    file = open("./google-10000-english-no-swears.txt", "r")
    values = file.read().split('\n')
    return values[0:n]


def arrayToFile(array):
    outputArray = np.array(array)
    np.save("compressionArray", outputArray)


def arrayFromFile():
    return np.load("compressionArray.npy", allow_pickle=True)


def graphFromFile(path):
    file = open(path, "r")
    values = file.read().split()
    values = list(map(int, values))
    result = []
    for i in range(values[0]):
        result.append([0] * values[0])

    for i in range(2, values[1] * 2 + 1, 2):
        result[values[i]][values[i + 1]] = 1

    return result

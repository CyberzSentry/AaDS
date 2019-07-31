def selectionSort(A):
    for i in range(len(A) - 1):
        index_min = i
        value_min = A[i]
        for j in range(i + 1, len(A)):
            if A[j] < value_min:
                index_min = j
                value_min = A[j]

        A[index_min] = A[i]
        A[i] = value_min

    return A


def insertionSort2(A):
    min_index = 0
    for i in range(len(A)):
        if A[i] < A[min_index]:
            min_index = i

    temp = A[0]
    A[0] = A[min_index]
    A[min_index] = temp

    for i in range(2, len(A)):
        value_min = A[i]
        j = i - 1
        while value_min < A[j]:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = value_min
    return A


def insertionSort1(A):
    for i in range(1, len(A)):
        value_min = A[i]
        j = i - 1
        while (j >= 0) & (value_min < A[j]):
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = value_min
    return A


def bubbleSort1(A):
    for i in range(len(A)):
        for j in range(1, len(A)):
            if (A[j - 1] > A[j]):
                temp = A[j - 1]
                A[j - 1] = A[j]
                A[j] = temp
    return A


def bubbleSort2(A):
    for i in range(len(A)):
        for j in range(1, len(A) - i):
            if (A[j - 1] > A[j]):
                temp = A[j - 1]
                A[j - 1] = A[j]
                A[j] = temp
    return A


def bubbleSort3(A):
    for i in range(len(A)):
        done = True
        for j in range(1, len(A) - i):
            if (A[j - 1] > A[j]):
                done = False
                temp = A[j - 1]
                A[j - 1] = A[j]
                A[j] = temp
        if done:
            return A
    return A


def checkSorted(A):
    for i in range(1, len(A)):
        if A[i - 1] > A[i]:
            return False
    return True

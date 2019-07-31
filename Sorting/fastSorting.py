import random

#first pivot
def quickSort1(A, l, r):
    if l < r:
        pivot = A[l]
        s = l
        for i in range(l+1, r):
            if A[i] < pivot:
                s = s + 1
                temp = A[s]
                A[s] = A[i]
                A[i] = temp

        temp = A[s]
        A[s] = A[l]
        A[l] = temp

        quickSort1(A, l, s)
        quickSort1(A, s + 1, r)
    return A

#ranndom pivot
def quickSort2(A, l, r):
    if l < r:
        x = random.randint(l, r-1)
        temp = A[l]
        A[l] = A[x]
        A[x] = temp
        pivot = A[l]
        s = l
        for i in range(l + 1, r):
            if A[i] < pivot:
                s = s + 1
                temp = A[s]
                A[s] = A[i]
                A[i] = temp

        temp = A[s]
        A[s] = A[l]
        A[l] = temp

        quickSort2(A, l, s)
        quickSort2(A, s + 1, r)
    return A

#ranndom pivot
def quickSort22(A, l, r):
    if l < r:
        x = random.randint(l, r-1)
        pivot = A[x]
        s = x
        for i in range(l + 1, r):
            if A[i] < pivot:
                s = s + 1
                temp = A[s]
                A[s] = A[i]
                A[i] = temp
            if A[i] >= pivot:
                s = s - 1
                temp = A[s]
                A[s] = A[i]
                A[i] = temp

        temp = A[s]
        A[s] = A[x]
        A[x] = temp

        quickSort2(A, l, s)
        quickSort2(A, s + 1, r)
    return A


#median of three pivot
def quickSort3(A, l, r):
    if l < r:

        low = l
        high = r - 1
        mid = int((high - low) / 2)
        if A[low] > A[high]:
            temp = low
            low = high
            high = temp
        if A[low] > A[mid]:
            temp = low
            low = mid
            mid = temp
        if A[high] < A[mid]:
            temp = high
            high = mid
            mid = temp

        temp = A[l]
        A[l] = A[mid]
        A[mid] = temp
        pivot = A[l]
        s = l
        for i in range(l + 1, r):
            if A[i] < pivot:
                s = s + 1
                temp = A[s]
                A[s] = A[i]
                A[i] = temp

        temp = A[s]
        A[s] = A[l]
        A[l] = temp

        quickSort1(A, l, s)
        quickSort1(A, s + 1, r)
    return A


def quickSortIns(A, l, r, trigger):
    if l < r:
        if r-l < trigger:
            insertionQ(A, l, r)
        else:
            pivot = A[l]
            s = l
            for i in range(l + 1, r):
                if A[i] < pivot:
                    s = s + 1
                    temp = A[s]
                    A[s] = A[i]
                    A[i] = temp
            temp = A[s]
            A[s] = A[l]
            A[l] = temp

            quickSort1(A, l, s)
            quickSort1(A, s + 1, r)
    return A


def shell1(A):
    h = 1
    while h < (len(A) / 9):
        h = int(3 * h + 1)

    while h - 1 >= 0:
        for i in range(h, len(A)):
            x = A[i]
            j = i
            while (j >= h) & (x < A[j - h]):
                A[j] = A[j - h]
                j = j - h
            A[j] = x
        h = int(h / 3)
    return A


def shell2(A):
    h = len(A)

    while h - 1 >= 0:
        for i in range(h, len(A)):
            x = A[i]
            j = i
            while (j >= h) & (x < A[j - h]):
                A[j] = A[j - h]
                j = j - h
            A[j] = x
        h = int(h / 2)
    return A

def insertionQ(A, l, r):
    for i in range(l, r):
        index_min = i
        value_min = A[i]
        for j in range(i + 1, len(A)):
            if A[j] < value_min:
                index_min = j
                value_min = A[j]

        A[index_min] = A[i]
        A[i] = value_min

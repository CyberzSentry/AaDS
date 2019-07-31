from Sources import fileDriver
import time
from Sorting import fastSorting, sorting

file = open("./output.txt", "w")

#n = [1280, 5120, 10240, 20480, 40960]
n = [3200, 6400, 12800, 51200, 102400]

for value in n:
    #fileDriver.generateRandoms(value, value)
    #A = fileDriver.getArray()
    A = fileDriver.readWords(value)

    start = time.time()
    result = fastSorting.quickSort1(A[:], 0, len(A))
    end = time.time()
    if sorting.checkSorted(result):
        print("quickSort1 ", value, " elements. Execution time: ", end - start)
        file.write("quickSort1 " + str(value) + " elements. Execution time: " + str(end - start))
    else:
        print("quickSort1 failed to sort")
        file.write("quickSort1 failed to sort")

    start = time.time()
    result = fastSorting.quickSort2(A[:], 0, len(A))
    end = time.time()
    if sorting.checkSorted(result):
        print("quickSort2 ", value, " elements. Execution time: ", end - start)
        file.write("quickSort2 " + str(value) + " elements. Execution time: " + str(end - start))
    else:
        print("quickSort2 failed to sort")
        file.write("quickSort2 failed to sort")

    start = time.time()
    result = fastSorting.quickSort3(A[:], 0, len(A))
    end = time.time()
    if sorting.checkSorted(result):
        print("quickSort3 ", value, " elements. Execution time: ", end - start)
        file.write("quickSort3 " + str(value) + " elements. Execution time: " + str(end - start))
    else:
        print("quickSort3 failed to sort")
        file.write("quickSort3 failed to sort")

    start = time.time()
    result = fastSorting.quickSortIns(A[:], 0, len(A), 10)
    end = time.time()
    if sorting.checkSorted(result):
        print("quickSortIns ", value, " elements. Execution time: ", end - start)
        file.write("quickSortIns " + str(value) + " elements. Execution time: " + str(end - start))
    else:
        print("quickSortIns failed to sort")
        file.write("quickSortIns failed to sort")

    start = time.time()
    result = fastSorting.shell1(A[:])
    end = time.time()
    if sorting.checkSorted(result):
        print("shell1 ", value, " elements. Execution time: ", end - start)
        file.write("shell1 " + str(value) + " elements. Execution time: " + str(end - start))
    else:
        print("shell1 failed to sort")
        file.write("shell1 failed to sort")

    start = time.time()
    result = fastSorting.shell2(A[:])
    end = time.time()
    if sorting.checkSorted(result):
        print("shell2 ", value, " elements. Execution time: ", end - start)
        file.write("shell2 " + str(value) + " elements. Execution time: " + str(end - start))
    else:
        print("shell2 failed to sort")
        file.write("shell2 failed to sort")

file.close()

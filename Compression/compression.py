# output needs to contain first sign and dictionary size


def compress(text, dictionarySize=8, lookAheadSize=4, minEncoed=0, debug=False):
    workingText = ""
    result = []
    found = False
    result.append([dictionarySize, text[0]])

    for i in range(dictionarySize):
        workingText += text[0]
    workingText += text

    if debug:
        print("Dictionary\t\tLook ahead buffer\t\tOutput")

    position = 0
    while position + dictionarySize < len(workingText):
        currDict = workingText[position: position + dictionarySize]
        lookAhead = workingText[position + dictionarySize:position + dictionarySize + lookAheadSize]

        for i in reversed(range(1, len(lookAhead) + 1)):
            searchResult = currDict.find(lookAhead[0:i])
            if searchResult != -1:
                if i > minEncoed:
                    result.append([0, searchResult, i])
                    found = True
                    break

        if found:
            position += result[-1][2]
        else:
            result.append([1, lookAhead[0]])
            position += 1

        if debug:
            print(currDict, "\t\t", lookAhead, "\t\t\t\t", result[-1])

        found = False

    return result


def decompress(array, debug=False):
    result = ""
    dictionarySize = int(array[0][0])
    position = 0

    for i in range(dictionarySize):
        result += array[0][1]

    if debug:
        print("Dictionary\t\tCurrent text")

    for i in range(1, len(array)):
        dictionary = result[position:position + dictionarySize]

        if array[i][0] == 1:
            result += array[i][1]
            position += 1
        else:
            result += dictionary[array[i][1]:array[i][1] + array[i][2]]
            position += array[i][2]

        if debug:
            print(dictionary, "\t\t", result)

    result = result[dictionarySize:]

    if debug:
        print("Final string ", result)

    return result

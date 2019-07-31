from Compression import compression
from Sources import fileDriver

toFile = True

text1 = "ABABCDABCABCDCADABCA"
text2 = "Six sick hicks nick six slick bricks with picks and sticks"
text3 = "can you can cans as a canner can can cans"

text = text2

print("String to compress: ", text)
array = compression.compress(text, minEncoed=3)

if toFile:
    fileDriver.arrayToFile(array)

if toFile:
    arrayFromFile = fileDriver.arrayFromFile()
    print("Compressed: \n", arrayFromFile.tolist())
    result = compression.decompress(arrayFromFile.tolist())
else:
    print("Compressed: \n", array)
    result = compression.decompress(array)

print("Compressed and decompresed for comparison: \n", text, "\n", result)
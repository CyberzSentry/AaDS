from Sources import fileDriver
from Graphs import graphs

source = fileDriver.graphFromFile("graph1.txt")
graphs.breathFirst(source, 1, 2)

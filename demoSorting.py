# coding: utf-8 
import matplotlib.pyplot as plt
import pandas as pd
from time import time
import random
import numpy as np
from sorting import Sorting
from selectionLib import Selection
from __init__ import printSwitch
columns=['b', 'h', 'i1', 'i2', 'm', 'so', 'se', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'r1', 'r2', 'r3']
columnsb=['b', 'h', 'i1', 'i2', 'm', 'so', 'se', 'q1', 'q2', 'q3', 'q4', 'q5', 'q7', 'r1', 'r2', 'r3']
columnsc=['h', 'm', 'so', 'q1', 'q2', 'q3', 'q4', 'q5', 'r1', 'r2', 'r3']
# Esiste un modo migliore per passare un numero arbitrario di argomenti alle funzioni, ed un modo molto semplice per gestirli in fase di chiamata...!
def sortingTest(inputList, sortingFunction, secondPar=None, thirdPar=None):
    l = list(inputList)  # copy the list. Equivalent to l=input[:].
    start = time()
    if secondPar != None and thirdPar != None:
        sortingFunction(l, secondPar, thirdPar)
    elif secondPar != None:
        sortingFunction(l, secondPar)
    else:
        sortingFunction(l)
    return time() - start
def sortTest(inputList):
    l = list(inputList)  # copy the list. Equivalent to l=input[:].
    start = time()
    l.sort()
    return time() - start
def printTest():
    # Inizializzazione
    inputType = 0  # 1 crescente, -1 decrescente, 0 random
    slowAlgorithms = True
    steps=[10,20,50,100]#  lista che indica la frequenza,la cui lunghezza determina il numero di test da eseguire
    for item in steps:
     inputList = [None] * item
     for i in range(0, item):
        if inputType == 1:
            inputList[i] = i
        elif inputType == -1:
            inputList[i] = item - i
        elif inputType == 0:
            inputList[i] = random.randint(0, item)
        else:
            raise Exception("You used an invalid inputType parameter!")
     printSwitch.dumpOperations = False

     if slowAlgorithms:

        runningTime=sortingTest(inputList, Sorting.selectionSort)
        print("selectionSort required {} seconds.".format(runningTime))
        print('')
        runningTime=sortingTest(inputList, Sorting.insertionSortUp)
        print("insertionSortUp required {} seconds.".format(runningTime))
        print('')

        runningTime=sortingTest(inputList, Sorting.insertionSortDown)
        print("insertionSortDown required {} seconds.".format(runningTime))
        print('')

        runningTime=sortingTest(inputList, Sorting.bubbleSort)
        print("bubbleSort required {} seconds.".format(runningTime))
        print('')

     runningTime=sortingTest(inputList, Sorting.quickSortIter, True)
     print("quickSortIter-Det required {} seconds.".format(runningTime))
     print('')

     runningTime=sortingTest(inputList, Sorting.quickSortIter)
     print("quickSortIter-NonDet required {} seconds.".format(runningTime))
     print('')

     runningTime=sortingTest(inputList, Sorting.quickSort, True)
     print("quickSort(Rec)-Det required {} seconds.".format(runningTime))
     print('')

     runningTime=sortingTest(inputList, Sorting.quickSort)
     print("quickSort(Rec)-NonDet required {} seconds.".format(runningTime))
     print('')


     runningTime=sortingTest(inputList, Sorting.quickSortSampleSelect)
     print("quickSortSampleSelect(Rec) required {} seconds.".format(runningTime))
     print('')

     #runningTime = sortingTest(inputList, Sorting.quickSortDetSelect)
     #print("quickSortDetSelect(Rec) required {} seconds.".format(runningTime))
     #print('')

     runningTime = sortingTest(inputList, Sorting.quickSortRandSelect)
     print("quickSortRandSelect(Rec) required {} seconds.".format(runningTime))
     print('')

     runningTime=sortingTest(inputList, Sorting.mergeSort)
     print("mergeSort required {} seconds.".format(runningTime))
     print('')


     runningTime=sortingTest(inputList, Sorting.heapSort)
     print("heapSort required {} seconds.".format(runningTime))
     print('')


     base = 400
     runningTime=(sortingTest(inputList, Sorting.radixSort, item, base))
     print("radixSort({},{}) required {} seconds.".format(item, base, runningTime))
     print('')

     base = 100
     runningTime=(sortingTest(inputList, Sorting.radixSort, item, base))
     print("radixSort({},{}) required {} seconds.".format(item, base, runningTime))
     print('')

     base = 10
     runningTime=(sortingTest(inputList, Sorting.radixSort, item, base))
     print("radixSort({},{}) required {} seconds.".format(item, base, runningTime))
     print('')

     runningTime=(sortTest(inputList))
     print("pythonSort required {} seconds.".format(runningTime))
     print('')
     print('\n')

if __name__ == "__main__":
    plt.title('Andamento algoritmi \n')
    plt.ylabel('Time (S)')
    plt.xlabel('Frequency(F)')
    c=0
    for alg in columns:#utilizza columns se vuole calcolare
        plt.legend(loc="lower right")
        d = pd.read_csv(alg + ".csv", sep=',', header=None)  # read file
        # d e' un dataframe: in pratica è una matrice. In d[i] c'è l'i-esima colonna
        x = d[0].values
        y = d[1].values
        plt.plot(x, y, c=np.random.random(3), label=alg)
        c += 1

    plt.savefig("test0.png")
    plt.show()

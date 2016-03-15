#!/usr/bin/env python

# Name: Write Your Name Here
# Email: Your Email
# SUID: Your Student ID
#
# By submitting this file as my own work, I declare that this
# code has been written on my own with no unauthorized help. I agree to the
# CU Honor Code. I am also aware that plagiarizing code may result in
# a failing grade for this class.
from __future__ import print_function
import sys
import random
import time
import matplotlib.pyplot as plt


# --------- Insertion Sort -------------
# Implementation of getPosition
# Helper function for insertionSort
def getPosition(rList, elt):
    # Find the position where element occurs in the list
    #
    for (i,e) in enumerate(rList):
        if (e >= elt):
            return i
    return len(rList)

# Implementation of Insertion Sort
def insertionSort(lst):
    n = len(lst)
    retList = []
    for i in lst:
        pos = getPosition(retList,i)
        retList.insert(pos,i)
    return retList

#------ Merge Sort --------------
def mergeSort(lst):
    if (len(lst) == 1):
        return lst
    else:
        half = round(len(lst)/2)
        l1 = mergeSort(lst[:half])
        l2 = mergeSort(lst[half:])
        return merge(l1, l2)

def merge(l1, l2):
    combined = []
    counter1 = 0
    counter2 = 0
    while (counter1 < len(l1) and counter2 < len(l2)):
        if (l1[counter1] >= l2[counter2]):
            combined.append(l2[counter2])
            counter2 += 1
        else:
            combined.append(l1[counter1])
            counter1 += 1
    if (counter1 >= len(l1)):
        combined.extend(l2[counter2:])
    else:
        combined.extend(l1[counter1:])
    return combined

#------ Quick Sort --------------
def quickSort(lst):
    pivot = partition(lst, 0, len(lst) - 1)
    quickSortsubList(lst, 0, pivot-1)
    quickSortsubList(lst, pivot+1, len(lst)-1)
    return lst

def quickSortsubList(lst, begin, end):
    if (begin < end):
        pivot = partition(lst, begin, end)
        quickSortsubList(lst, begin, pivot-1)
        quickSortsubList(lst, pivot+1, end)

def partition(lst, begin, end):
    pivot = random.randint(begin, end)
    i = begin
    for j in range(begin, end + 1):
        if (j != pivot and lst[j] <= lst[pivot]):
            if (i == pivot):
                pivot = j
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
            i += 1
    tmp = lst[pivot]
    lst[pivot] = lst[i]
    lst[i] = tmp
    return i


# ------ Timing Utility Functions ---------

# Code below is given only for demonstration purposes

# Function: generateRandomList
# Generate a list of n elements from 0 to n-1
# Shuffle these elements at random

def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst


def measureRunningTimeComplexity(sortFunction,lst):
    t0 = time.clock()
    sortFunction(lst)
    t1 = time.clock() # A rather crude way to time the process.
    return (t1 - t0)

def average(lst):
    return sum(lst)/len(lst)

insertionAvg = []
quickAvg = []
mergeAvg = []
insertionWorst = []
quickWorst = []
mergeWorst = []
x = list(range(5, 505, 5))

for n in range(5, 505, 5):
    insertionTime = []
    mergeTime = []
    quickTime = []
    for j in range(20*n):
        lst = generateRandomList(n)
        insertionTime.append(measureRunningTimeComplexity(insertionSort, lst))
        mergeTime.append(measureRunningTimeComplexity(mergeSort, lst))
        quickTime.append(measureRunningTimeComplexity(quickSort, lst))
    insertionAvg.append(average(insertionTime))
    insertionWorst.append(max(insertionTime))
    mergeAvg.append(average(mergeTime))
    mergeWorst.append(max(mergeTime))
    quickAvg.append(average(quickTime))
    quickWorst.append(max(quickTime))
    print("Finish n:", n)

plt.figure(0)
plt.plot(x, insertionAvg, label='Average Insertion')
plt.plot(x, insertionWorst, label='Worst Insertion')
plt.grid(True)
plt.ylabel("Time (s)")
plt.xlabel("Size of Array")
plt.title("Avg and Worst Case Running time for Insertion Sort")
plt.legend(loc='lower right')
plt.savefig("insertionSort.png")

plt.figure(1)
plt.plot(x, mergeAvg, label='Average Merge')
plt.plot(x, mergeWorst, label='Worst Merge')
plt.grid(True)
plt.ylabel("Time (s)")
plt.xlabel("Size of Array")
plt.title("Avg and Worst Case Running time for Merge Sort")
plt.legend(loc='lower right')
plt.savefig("mergeSort.png")

plt.figure(2)
plt.plot(x, quickAvg, label='Average QuickSort')
plt.plot(x, quickWorst, label='Worst QuickSort')
plt.grid(True)
plt.ylabel("Time (s)")
plt.xlabel("Size of Array")
plt.title("Avg and Worst Case Running time for Quick Sort")
plt.legend(loc='lower right')
plt.savefig("quickSort.png")

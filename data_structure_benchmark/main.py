from random import random
import time
import random
import sys

count = 10000
listAppendTimeSpent = 0
listForTimeSpent = 0
listDeleteTimeSpent = 0

def test_list_append(count):
    list = []

    startTimer = time.perf_counter()
    for i in range(count):
        list.append(random.randint(0,1000))
    stopTimer = time.perf_counter()

    timeSpent = stopTimer - startTimer
    return timeSpent

def test_list_for(count):
    list = []

    # Populates list
    for i in range(count):
        list.append(random.randint(0,1000))

    # Iterating
    startTimer = time.perf_counter()
    for i in range(len(list)):
        continue

    stopTimer = time.perf_counter()

    timeSpent = stopTimer - startTimer
    return timeSpent

def test_list_delete(count):
    list = []

    # Populates list
    for i in range(count):
        list.append(random.randint(0,1000))

    # Deleting items
    startTimer = time.perf_counter()
    for i in range(int(len(list) / 2)):
        list.remove(list[-i])
        continue

    stopTimer = time.perf_counter()

    timeSpent = stopTimer - startTimer
    return timeSpent

def printResults():
    print(f"Test with {count} itens")
    print(f"""
    ---------------------------
    -- LIST
    ---------------------------
    Append time: {round(listAppendTimeSpent, 5)}s
    Iterating time: {round(listForTimeSpent, 5)}s
    Delete arbitrary item time: {round(listDeleteTimeSpent, 5)}s
        """
    )

if(__name__  == "__main__"):
    # if(len(sys.argv) != 2):
    #     print("Check parameters\nUsage python3 main.py ITEM_COUNT")
    #     exit(1)

    if(len(sys.argv) == 2):
        count = int(sys.argv[1])

    listAppendTimeSpent = test_list_append(count)
    listForTimeSpent = test_list_for(count)
    listDeleteTimeSpent = test_list_delete(count)

    printResults()

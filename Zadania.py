#Lista do zadań
array_1 = [1, 2, 4, 5, 4, 3, 2, 5, 1, 10, 7, 5, 3, 4, 5, 1, 12, 3]

def Zadanie_1():
    for i in range(1,101): #Jak zrobić tak aby tutaj dać 100 a nie 101?
        print(i)
def Zadanie_2():
    for i in range(1,101,2):
        print(i)
def Zadanie_3():
    for i in range(-1,-101,-1):
        print(i)
def Zadanie_4():
    for i in range(-1,-101,-3):
        print(i)
def Zadanie_5():
    for i in range(100,0,-1):
        print(i)
def Zadanie_6():
    for i in range(1000,10,-10):
        print(i)
def Zadanie_7():
    for i in range(0,101):
        if (i % 3) == 0:
            print(i)
def Zadanie_8():
    for i in range(0,101):
        if (i % 2 == 0):
            print(i)
def Zadanie_9():
        for x in range(1,11):
            for y in range(0,10):
                print(y+x, end="  ") #Do omówienia
            print()
def Zadanie_10():
    array = []
    for x in range (1,11):
        array.append(x**2)
    print(array)
def Zadanie_11():
    for i in range (1,11):
        if i == 3 or i == 7:
            continue
        print(i)
def Zadanie_12():
    array = []
    for x in range (1,101):
        array.append(0)
    print(array)
    print(len(array))
## Zadanie_13 w ramach comprehenstion
def Zadanie_14():
    array =  list(range(1,101))
    print(array)
def Zadanie_15():
    print(array_1[-3])
def Zadanie_16():
    print(array_1)
    myArray = array_1
    myArray[8] = 3
    print(myArray)
def Zadanie_17():
    if 10 in array_1:
        return print(True)
    else:
        return print(False)
def Zadanie_18():
    print(array_1.count(5))
def Zadanie_19():
    array_1.sort(reverse=False)
    print(array_1)
    array_1.sort(reverse=True)
    print(array_1)
def Zadanie_20():
    print(max(array_1))
    print(min(array_1))
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
                print(x+y, end="  ") #Do omówienia
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
    array = list(range(1,101))
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
def Zadanie_21():
    avg = print(sum(array_1) / len(array_1))
def Zadanie_22():
    print(sum(array_1))
def Zadanie_23():
   array_1.reverse()## Nie można od razu w princie? Pokazuje wtedy "None"
   print(array_1)
def Zadanie_24():
    print(len(array_1))
def Zadanie_25():
    half = int(len(array_1) / 2) ## ale co w momencie kiedy to suma będzie niepodzielna przez 2?
    first_array = array_1[:half]
    second_array = array_1[half:]
    print(first_array)
    print(second_array)
def Zadanie_26():
    print(array_1)
    array_1.pop(-3)
    print(array_1)
def Zadanie_27():
    print(array_1)
    even_numbers = []
    for i in array_1:
        if i % 2 == 0:
            even_numbers.append(i)
    print(even_numbers)
def Zadanie_28():
    array = []
    for i in array_1:
        array.append(i**2)
    print(array)
def Zadanie_30():
    print(array_1)
    for i in array_1:
        if i == 4:
            array_1.remove(i)
    print(array_1)
def Zadanie_31():
    print(array_1)
    array = []
    for i in array_1:
        if i > 7:
            array.append(i)
    print(array)
def Zadanie_32():
    




#Lista do zadań
from test import Zadanie_48

array_1 = [1, 2, 4, 5, 4, 3, 2, 5, 1, 10, 7, 5, 3, 4, 5, 1, 12, 3]
array_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_1 = [3, 4, 5, 2, 3, 3, 2, 1, 4]
#Zadania




def zadanie_1():
    mylist = []
    for i in range(1,101):
        mylist.append(i)
    myList_Comprehension = [i for i in range(1,101)]
    print(mylist)
    print(myList_Comprehension)




def zadanie_2():
    mylist = []
    for i in range(1,101,2):
        mylist.append(i)
    myList_Comprehension = [i for i in range(1,101,2)]
    print(mylist)
    print(myList_Comprehension)


def zadanie_3():
    myList = []
    for i in range(-1,-101,-1):
        myList.append(i)
    myList_Comprehension = [i for i in range(-1,-101,-1)]
    print(myList)
    print(myList_Comprehension)


def zadanie_4():
    myList = []
    for i in range(-1,-101,-3):
        myList.append(i)
    myList_Comprehension = [i for i in range(-1, -101, -3)]
    print(myList)
    print(myList_Comprehension)


def zadanie_5():
    myList = []
    for i in range(100,0,-1):
        myList.append(i)
    mylist_comprehension = [i for i in range(100, 0, -1)]
    print(myList)
    print(mylist_comprehension)


def zadanie_6():
    myList = []
    for i in range(1000, 0, -10):
        myList.append(i)
    myList_Comprehension = [i for i in range(1000, 0, -10)]
    print(myList)
    print(myList_Comprehension)


def zadanie_7():
    myList = []
    for i in range(0,101):
        if i % 3 == 0:
            myList.append(i)

    myList_Comprehension = [i if i % 3 == 0 else None for i in range(0,101)]

    #myList_Comprehension = [i for i in range(0,101) if i % 3 == 0]
    print(myList)
    print(myList_Comprehension)
    
    


def zadanie_8():
    myList = []
    for i in range(0,101):
        if (i % 2 == 0):
            myList.append(i)
    myList_Comprehension = [i for i in range(0,101) if(i % 2 == 0)]
    print(myList)
    print(myList_Comprehension)
    
    


def zadanie_9():
        for x in range(1,11):
            for y in range(0,10):
                print(x+y, end="  ") #Do omówienia
            print()
            
            

def zadanie_10():
    myList = []
    for x in range (1,11):
        myList.append(x**2)
    myList_Comprehension = [i**2 for i in range(1,11)]
    print(myList)
    print(myList_Comprehension)
    

def zadanie_11():
    myList = []
    for i in range (1,11):
        if i == 3 or i == 7:
            continue
        myList.append(i)
    myList_Comprehension = [i for i in range(1,11) if i != 3 and i != 7]
    print(myList)
    print(myList_Comprehension)
    
    

def zadanie_12():
    my_list = []
    for _ in range(100):
        my_list.append(0)
    my_list_comprehension = [0 for _ in range(100)]
    print(my_list)
    print(my_list_comprehension)




def zadanie_14():
    array = list(range(100))
    print(array)




def zadanie_15():
    print(array_1[-3])




def zadanie_16():
    print(array_1)
    my_array = array_1
    my_array[8] = 3
    print(my_array  )




def zadanie_17():
    if 10 in array_1:
         print(True)
    else:
         print(False)
    my_list = [True if i == 10 else False for i in array_1] # DO NAUKI
    print(any(my_list)) #DO NAUKI ANY / ALL
    print(True if 10 in array_1 else False) # DO NAUKI


def zadanie_18():
    print(array_1.count(5))


def zadanie_19():
    array_1.sort(reverse=False)
    print(array_1)
    array_1.sort(reverse=True)
    print(array_1)


def zadanie_20():
    print(max(array_1))
    print(min(array_1))


def zadanie_21():
    avg = print(sum(array_1) / len(array_1))
    print(avg)


def zadanie_22():
    print(sum(array_1))


def zadanie_23():
   array_1.reverse()
   print(list(reversed(array_1)))

def zadanie_24():
    print(len(array_1))


def zadanie_25():
    half = int(len(array_1) / 2)
    first_array = array_1[:half]
    second_array = array_1[half:]
    print(first_array)
    print(second_array)


def zadanie_26():
    print(array_1)
    array_1.pop(-3)
    print(array_1)


def zadanie_27():
    print(array_1)
    even_numbers = []
    for i in array_1:
        if i % 2 == 0:
            even_numbers.append(i)
    print(even_numbers)


def zadanie_28():
    array = []
    for i in array_1:
        array.append(i**2)
    print(array)


def zadanie_30():
    print(array_1)
    for i in array_1:
        if i == 4:
            array_1.remove(i)
    print(array_1)


def zadanie_31():
    print(array_1)
    array = []
    for i in array_1:
        if i > 7:
            array.append(i)
    print(array)


def zadanie_32():
    a = 1
    b = 2
    a, b = b, a #Do zastosowania

    print(array_1)
    first_number = array_1.pop(5)
    last_number = array_1.pop()
    array_1.append(first_number) ##Append zawsze dodaje na koniec listy
    array_1.insert(5, last_number)
    print(array_1)


def zadanie_33():
    array_1.sort(reverse=True)
    print(array_1[1])


def zadanie_34():
    list = []
    for i in array_1:
        if array_1.count(i) > 1:
            list.append(i)
    print(list)


def zadanie_35():
    list = []
    for i in array_1:
        if array_1.count(i) > 1:
            continue
        list.append(i)
    print(list)


def zadanie_36():
    print(array_1)
    list = []
    for i in array_1:
        list.insert(0, i)
    print(list)
    print(array_1[::-1])


def zadanie_37():
    print(array_1)
    for i in array_1:
        if i > 5:
            x = array_1.index(i)
            array_1[x] = 'True'
    print(array_1)


def zadanie_38():
    print(sum([i for i in array_1 if i % 2 == 1]))

def zadanie_39():
    list = []
    for i in array_1:
        if array_1.index(i) % 2 == 0:
           list.append(i)
    print(sum(list))


def zadanie_40():
    list = []
    for i in array_1:
        if array_1.count(i) > 1:
            count = array_1.count(i)
            list.append([i, count])
    print(max(list[count]))


def zadanie_41():
    print(array_2[:2])


def zadanie_42():
    print(array_2[-3:])


def zadanie_43():
    print(array_2)
    print(array_2[1:-1])


def zadanie_44():
    print(array_2[4:8])


def zadanie_45():
    for i in array_2[::2]:
        print(i)


def zadanie_46():
    print(array_2[::-1])


def zadanie_47():
    list = []
    array_2.sort(reverse=True)
    for i in array_2[::2]:
        list.append(i)
    print(list)


def zadanie_48():
    numbers = [10,12,13]
    array_2[:3] = numbers
    print(array_2)



def zadanie_49():
    array_2[-1] = 999
    print(array_2)


def zadanie_50():
    empty_list = []
    array_2 = empty_list
    print(array_2)


def zadanie_51():
    x = array_2[2:5]
    y = x*2
    print(y)


def zadanie_52():
    l_1 = array_2[1:8]
    l_2 = array_2[7:0:-1]
    l_1.extend(l_2)
    print(l_1)


def zadanie_53():
    matrix = [[1, 2], [2, 3], [3, 4]]
    print(matrix[:][0])


def zadanie_54():
    matrix = [[1, 2], [3, 4], [5, 6]]
    print(matrix[1][1])


def zadanie_55(n: int):
    if n > 10:
        n = 10
    my_list = []
    for i in range(1, n+1):
        my_list.append(i)
        print(my_list)
zadanie_55(4)


def zadanie_56(): # Do omówienia
    print("do zrobienia")

def zadanie_57():
    # Sprawdź każdy element listy i jeżeli są takie same to nie zliczaj, a jak różne to dodaj
    print("")


def zadanie_58():
    myList = ["a", "b", "c", "d"]
    for x in enumerate(myList):
        print(x)



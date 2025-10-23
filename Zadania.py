#Lista do zadań
array_1 = [1, 2, 4, 5, 4, 3, 2, 5, 1, 10, 7, 5, 3, 4, 5, 1, 12, 3]
array_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list = [3, 4, 5, 2, 3, 3, 2, 1, 4]
#Zadania
def Zadanie_1():
    mylist = []
    for i in range(1,101):
        mylist.append(i)
    myList_Comprehension = [i for i in range(1,101)]
    print(mylist)
    print(myList_Comprehension)
def Zadanie_2():
    mylist = []
    for i in range(1,101,2):
        mylist.append(i)
    myList_Comprehension = [i for i in range(1,101,2)]
    print(mylist)
    print(myList_Comprehension)
def Zadanie_3():
    myList = []
    for i in range(-1,-101,-1):
        myList.append(i)
    myList_Comprehension = [i for i in range(1,101,-1)]
    print(myList)
    print(myList_Comprehension)
def Zadanie_4():
    myList = []
    for i in range(-1,-101,-3):
        myList.append(i)
    myList_Comprehenstion = [i for i in range(-1,101,-3)]
    print(myList)
    print(myList_Comprehension)
def Zadanie_5():
    myList = []
    for i in range(100,0,-1):
        myList.append(i)
    print(myList)
    print(myList_Comprehension)
def Zadanie_6():
    myList = []
    for i in range(1000,10,-10):
        myList.append(i)
    myList_Comprehension = [i for i in range(1000,10,-10)]
    print(myList)
    print(myList_Comprehension)
def Zadanie_7():
    myList = []
    for i in range(0,101):
        if (i % 3) == 0:
            myList.append(i)
    myList_Comprehension = [i for i in range(0,101) if (i % 3) == 0]
    print(myList)
    print(myList_Comprehension)
def Zadanie_8():
    myList = []
    for i in range(0,101):
        if (i % 2 == 0):
            myList.append(i)
    myList_Comprehension = [i for i in range(0,101) if(i % 2 == 0)]
    print(myList)
    print(myList_Comprehension)
def Zadanie_9():
        for x in range(1,11):
            for y in range(0,10):
                print(x+y, end="  ") #Do omówienia
            print()
def Zadanie_10():
    myList = []
    for x in range (1,11):
        myList.append(x**2)
    myList_Comprehension = [i**2 for i in range(1,11)]
    print(myList)
    print(myList_Comprehension)
def Zadanie_11():
    myList = []
    for i in range (1,11):
        if i == 3 or i == 7:
            continue
        myList.append(i)
    myList_Comprehension = [i for i in range(1,11) if i != 3 and i != 7]
    print(myList)
    print(myList_Comprehension)
def Zadanie_12():
    myList = []
    for x in range (1,101):
        myList.append(0)
    myList_Comprehension = [0 for i in range(1,101)]
    print(myList)
    print(myList_Comprehension)
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
         print(True)
    else:
         print(False)
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
    print(array_1)
    first_number = array_1.pop(5)
    last_number = array_1.pop()
    array_1.append(first_number) ##Append zawsze dodaje na koniec listy
    array_1.insert(5, last_number)
    print(array_1)
def Zadanie_33():
    array_1.sort(reverse=True)
    print(array_1[1])
def Zadanie_34():
    list = []
    for i in array_1:
        if array_1.count(i) > 1:
            list.append(i)
    print(list)
def Zadanie_35():
    list = []
    for i in array_1:
        if array_1.count(i) > 1:
            continue
        list.append(i)
    print(list)
def Zadanie_36():
    print(array_1)
    list = []
    for i in array_1:
        list.insert(0, i)
    print(list)
    print(array_1[-1::-1])
def Zadanie_37():
    print(array_1)
    for i in array_1:
        if i > 5:
            x = array_1.index(i)
            array_1.pop(x)
            array_1.insert(x, "True")
    print(array_1)
def Zadanie_38():
    list = []
    for i in array_1:
        if i % 2 == 1:
            list.append(i)
    print(sum(list))
def Zadanie_39():
    list = []
    for i in array_1:
        if array_1.index(i) % 2 == 0:
           list.append(i)
    print(sum(list))
def Zadanie_40():
    list = []
    for i in array_1:
        if array_1.count(i) > 1:
            count = array_1.count(i)
            list.append([i, count])
    print(max(list[count]))
def Zadanie_41():
    print(array_2[:2])
def Zadanie_42():
    print(array_2[-3:])
def Zadanie_43():
    print(array_2)
    print(array_2[1:-1])
def Zadanie_44():
    print(array_2[4:8])
def Zadanie_45():
    for i in array_2[::2]:
        print(i)
def Zadanie_46():
    print(array_2[::-1])
def Zadanie_47():
    list = []
    array_2.sort(reverse=True)
    for i in array_2[::2]:
        list.append(i)
    print(list)
def Zadanie_48():
    numbers = [10,11,12]
    for i in array_2[:3]:
        array_2[i] = numbers[i]
    print(array_2)
def Zadanie_49():
    array_2[-1] = 999
    print(array_2)
def Zadanie_50():
    empty_list = []
    array_2 = empty_list ## Do omówienia bo nie wiem czy dobrze zrozumiałem
    print(array_2)
def Zadanie_51(): ## Do omówienia
    x = []
    x = array_2[2:5]
    x.extend(x)
    print(x)
def Zadanie_52():
    l_1 = array_2[1:8]
    l_2 = array_2[7:0:-1]
    l_1.extend(l_2)
    print(l_1)
def Zadanie_53():
    matrix = [[1, 2], [2, 3], [3, 4]]
    print(matrix[:][0])
def Zadanie_54():
    matrix = [[1, 2], [3, 4], [5, 6]]
    print(matrix[1][1])
def Zadanie_55():
    min = 1
    max = 6
    for i in range(1,10):
        numbers = ""
        space = " "
        for j in range(min,max):
            numbers += str(j) * i + space
            print(numbers)
        break
def Zadanie_56(): # Do omówienia
    min = 1
    max = 4
    for i in range(1, 4):
        numbers = ""
        space = " "
        for j in range(min, max):
            numbers +=str(j) * i + space
            print(numbers)
        print(numbers)
        break
#def Zadanie_57() Do omówienia
def Zadanie_58():
    myList = ["a", "b", "c", "d"]
    for x, y in enumerate(myList):
        print(x, y)



import time

#Lista_zadań
array_1 = [1, 2, 4, 5, 4, 3, 2, 5, 1, 10, 7, 5, 3, 4, 5, 1, 12, 3]
array_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_1 = [3, 4, 5, 2, 3, 3, 2, 1, 4]
my_list = [1, 1, 4, 2, 3, 3, 2, 1, 4]


#Zadania


def exec_1():
    mylist = []
    for i in range(1,101):
        mylist.append(i)
    mylist_comprehension = [i for i in range(1,101)]
    print(mylist)
    print(mylist_comprehension)


def exec_2():
    mylist = []
    for i in range(1,101,2):
        mylist.append(i)
    mylist_comprehension = [i for i in range(1,101,2)]
    print(mylist)
    print(mylist_comprehension)


def exec_3():
    mylist = []
    for i in range(-1,-101,-1):
        mylist.append(i)
    mylist_comprehension = [i for i in range(-1,-101,-1)]
    print(mylist)
    print(mylist_comprehension)


def exec_4():
    mylist = []
    for i in range(-1,-101,-3):
        mylist.append(i)
    mylist_comprehension = [i for i in range(-1, -101, -3)]
    print(mylist)
    print(mylist_comprehension)


def exec_5():
    mylist = []
    for i in range(100,0,-1):
        mylist.append(i)
    mylist_comprehension = [i for i in range(100, 0, -1)]
    print(mylist)
    print(mylist_comprehension)


def exec_6():
    mylist = []
    for i in range(1000, 0, -10):
        mylist.append(i)
    mylist_comprehension = [i for i in range(1000, 0, -10)]
    print(mylist)
    print(mylist_comprehension)


def exec_7():
    mylist = []
    for i in range(0,101):
        if i % 3 == 0:
            mylist.append(i)

    mylist_comprehension = [i if i % 3 == 0 else None for i in range(0,101)]

    #mylist_comprehension = [i for i in range(0,101) if i % 3 == 0]
    print(mylist)
    print(mylist_comprehension)
    
    
def exec_8():
    mylist = []
    for i in range(0,101):
        if i % 2 == 0:
            mylist.append(i)
    mylist_comprehension = [i for i in range(0,101) if(i % 2 == 0)]
    print(mylist)
    print(mylist_comprehension)
    

def exec_9():
     print('\n'.join(map(str,[[x+y for x in range(1,11)] for y in range(0,10)])))



def exec_10():
    mylist = []
    for x in range (1,11):
        mylist.append(x**2)
    mylist_comprehension = [i**2 for i in range(1,11)]
    print(mylist)
    print(mylist_comprehension)
    

def exec_11():
    mylist = []
    for i in range (1,11):
        if i == 3 or i == 7:
            continue
        mylist.append(i)
    mylist_comprehension = [i for i in range(1,11) if i != 3 and i != 7]
    print(mylist)
    print(mylist_comprehension)
    

def exec_12():
    my_list = []
    for _ in range(100):
        my_list.append(0)
    my_list_comprehension = [0 for _ in range(100)]
    print(my_list)
    print(my_list_comprehension)


def exec_14():
    array = list(range(100))
    print(array)


def exec_15():
    print(array_1[-3])


def exec_16():
    print(array_1)
    my_array = array_1
    my_array[8] = 3
    print(my_array  )


def exec_17():
    my_list_1 = [True if i == 10 else False for i in array_1]
    print(my_list_1)


def exec_18():
    print(array_1.count(5))


def exec_19():
    array_1.sort(reverse=False)
    print(array_1)
    array_1.sort(reverse=True)
    print(array_1)


def exec_20():
    print(max(array_1))
    print(min(array_1))


def exec_21():
    avg_1 = (sum(array_1) / len(array_1))
    print(avg_1)


def exec_22():
    print(sum(array_1))


def exec_23():
   array_1.reverse()
   print(list(reversed(array_1)))

def exec_24():
    print(len(array_1))


def exec_25():
    half = int(len(array_1) / 2)
    first_array = array_1[:half]
    second_array = array_1[half:]
    print(first_array)
    print(second_array)


def exec_26():
    print(array_1)
    array_1.pop(-3)
    print(array_1)


def exec_27():
    print([i for i in array_1 if i % 2 == 0])


def exec_28():
    print([i**2 for i in array_1])


def exec_30():
    print([array_1.remove(i) for i in array_1 if i ==4])


def exec_31():
    print([i for i in array_1 if i > 7])


def exec_32():
    print(array_1)


def exec_33():
    array_1.sort(reverse=True)
    print(array_1[1])


def exec_34():
    my_list_1 = [i for i in array_1 if array_1.count(i) > 1]
    print(my_list_1)


def exec_35():
    my_list_1 = [i for i in array_1 if array_1.count(i) ==1]
    print(my_list_1)


def exec_36():
    print(array_1[::-1])


def exec_37():
    my_list_1 = [True if i > 5 else i for i in array_1]
    print(my_list_1)


def exec_38():
    print(sum([i for i in array_1 if i % 2 == 1]))

def exec_39():
    my_list_1 = [i for i in array_1 if array_1.index(i) % 2 ==0]
    print(sum(my_list_1))


def exec_40():
    my_list_1 = [(i, array_1.count(i)) for i in array_1 if array_1.count(i) > 1]
    print(max(my_list_1))


def exec_41():
    print(array_2[:2])


def exec_42():
    print(array_2[-3:])


def exec_43():
    print(array_2)
    print(array_2[1:-1])


def exec_44():
    print(array_2[4:8])


def exec_45():
    for i in array_2[::2]:
        print(i)


def exec_46():
    print(array_2[::-1])


def exec_47():
    array_2.sort(reverse= True)
    mylist = [i for i in array_2[::2]]
    print(mylist)


def exec_48():
    numbers = [10,12,13]
    array_2[:3] = numbers
    print(array_2)


def exec_49():
    array_2[-1] = 999
    print(array_2)


def exec_50():
    empty_list = []
    array_2 = empty_list
    print(array_2)


def exec_51():
    x = array_2[2:5]
    y = x*2
    print(y)


def exec_52():
    l_1 = array_2[1:8]
    l_2 = array_2[7:0:-1]
    l_1.extend(l_2)
    print(l_1)


def exec_53():
    matrix = [[1, 2], [2, 3], [3, 4]]
    print(matrix[:][0])


def exec_54():
    matrix = [[1, 2], [3, 4], [5, 6]]
    print(matrix[1][1])


def exec_55(n: int):
    if n > 10:
        n = 10
    my_list = []
    for i in range(1, n+1):
        my_list.append(i)
        print(my_list)


def exec_56(n: int):
    if n > 3:
        n = 3
    for i in range(1,n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()
    for i in range(n-1,0,-1):
        for j in range(1, i+1):
            print(j, end="")
        print()
        print()


def exec_57(x: list):
    previous_element = x[0]
    count_changes = 0
    for i in x[1:]:
       if i != previous_element:
            count_changes+=1
       previous_element = i
    print(count_changes)


def exec_58():
    mylist = ["a", "b", "c", "d"]
    for x in enumerate(mylist):
        print(x)





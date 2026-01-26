import sys


def exec_1():
    my_tuple = (1,2,3)
    my_tuple_function = tuple((1,2,3))
    print(my_tuple, my_tuple_function)


def exec_2():
    first_tuple = (1, 2, 3)
    second_tuple = (4, 5, 6)
    third_tuple = first_tuple + second_tuple
    print(third_tuple)


def exec_3():
    my_list = [1, 2, 3, 4]
    my_tuple = tuple(my_list)
    print(my_tuple)
    print(type(my_tuple))


def exec_4():
    my_tuple = (1,2,3)
    a,b,c = my_tuple
    print(b)


def exec_5():
    my_list = [1,2,2,3,4,4,5]
    my_set = set(my_list)
    print(my_set)


def exec_6():
    #Set traktuje 1 jako True oraz 0 jako False, nie przymuje duplikatów więc wyświetli pierwszą napotkoną wartość a pozostałe pominie
    #Jeżeli pierwsze było True a potem 1 wyświetli True, jeżeli pierwsze było 1 a potem True, wyświetli 1
    my_list = [0, True, 1]
    my_set = set(my_list)
    print(my_list)
    print(my_set)


def exec_7():
    my_set = set(({1,2,3}))
    #Dodawanie:
    #1 poprzez add
    my_set.add(3)
    #2 poprzez utworzenie listy i dodanie elementu
    my_list = list(my_set)
    my_list.insert(4, 4)
    my_set = set(my_list)
    #3 usuwanie poprzez remove
    my_set.remove(4)
    print(my_set)
    #4 poprze utworzenie listy i usuniecie elementu
    my_list_1 = list(my_set)
    my_list_1.pop(0)
    my_set = set(my_list_1)
    print(my_set)


def exec_8():
    my_set_a = {1,2,3,4}
    my_set_b = {3,4,5,6}
    sum_set = my_set_a | my_set_b
    product_set = my_set_a & my_set_b
    diff_set = my_set_a - my_set_b
    diff_sym_set = my_set_a ^ my_set_b
    print(sum_set)
    print(product_set)
    print(diff_set)
    print(diff_sym_set)


def exec_9(a: set, b: set):
    print(a.issubset(b))


def exec_10():
    my_set_a = {1,2,3,4}
    my_set_a.clear()
    print(my_set_a)


def exec_11():
    test_set = "test"
    print(type(test_set))
    my_set_a = set(test_set)
    print(my_set_a)
    test_set_2 = "Uczę się programowania w Pythonie"
    my_set_b = set(test_set_2.split())
    print(my_set_b)


def exec_12(word_1: str, word_2: str):
    same_words = set(word_1) & set(word_2)
    print(same_words)


def exec_13():
    blue_team = {"Ala", "Ola", "Tomek"}
    green_team = {"Jan", "Piotr", "Ola"}
    exec_a = blue_team - green_team
    exec_b = green_team - blue_team
    print(f"Zadanie A {exec_a} \n" f"Zadanie B {exec_b}")


def exec_14():
    a = tuple(([1,2], [3,4]))
    a[0][0] = 99
    print(a)
    #Ja nie zmieniłem niczego w tuplach, tylko w liście, która jest częścią tupli
    #a elementy w liscie są modyfikowalne

def exec_15():
    a = tuple((1,2,3,4))
    print(a)


def exec_16_a():# Czy o to chodziło?
    emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
    email_list = list(dict.fromkeys(emails))
    print(email_list)


def exec_16_b():# Czy o to chodziło?
    emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
    email_set = set(emails)
    print(email_set)


def exec_17(lat: float, long: float):
    miasta = {
        ("Warszawa", 52.23, 21.01): 1793579,
        ("Kraków", 50.06, 19.94): 779115,
        ("Gdańsk", 54.35, 18.64): 486022
    }
    dict_with_euclides_range= {key: round((((lat - lat_key)**2 + (long-long_key)**2)**0.5), 2)
                               for key, lat_key, long_key in miasta.keys()}
    print(min(dict_with_euclides_range, key = dict_with_euclides_range.get))


def exec_18(): ## Do zmiany, sortowanie całej listy po drugiem argumencie w tupli
    points = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4)]
    exec_a = set(points)
    my_list_comprehension = [tuple(sorted(i, reverse= True)) for i in exec_a]
    print(my_list_comprehension)


def exec_19():
    test = {(1, 2), (3, 4), [5, 6]} #Do omówienia
    #Ja ten błąd rozumiem tak: "Używasz zmiennej listy jako klucza, która
    # może się zmienić, a ja nie jestem w stanie dla niej wygenerować stabilnej wartości (hash value)
    test_corrected = {(1,2), (3,4), (5,6)}
    print(test_corrected)


def exec_20():
    words = ["python", "ai", "data", "python", "ml", "data", "ml"]
    my_dict =  {k: {idx for idx, val in enumerate(words) if val == k} for k in words}
    print(my_dict)


def exec_21():
    my_set = set(({1,2,3}))
    my_set.add(4)
    print(my_set)
    my_set_frozen = frozenset(my_set)

def exec_22():
    list_comprehension = [i for i in range(1,1001)]
    tuple_comprehension_gen = (i for i in range(1, 1001))
    tuple_comprehension_tuple = tuple((i for i in range(1, 1001)))

    print(type(list_comprehension))
    print(type(tuple_comprehension_gen))
    print(type(tuple_comprehension_tuple))
    print(sys.getsizeof(list_comprehension))
    print(sys.getsizeof(tuple_comprehension_gen))
    print(sys.getsizeof(tuple_comprehension_tuple))


def exec_generator(n):
    for i in range(n):
        yield i

print(next(exec_generator(1000000)))

#Collatz
collatz_list = list()
def collatz(n: float):
    if n == 1:
        print(n)
    else:
        if n % 2 == 0:
            n = n * 0.5
            collatz_list.append(n)
            collatz(n)
        else:
            n = (3 * n) + 1
            collatz_list.append(n)
            collatz(n)

collatz(6034302301)
print(collatz_list)



import time

#DICTIONARIES
students = {"Anna Kowalska": 5, "Celina Wiśniewska": 3, "Damian Wójcik": 2.5, "Iga Dąbrowska": 2,
            "Elżbieta Kamińska": 5, "Filip Zieliński": 4, "Gabriela Szymańska": 3, "Hubert Lewandowski": 5,
            "Jakub Kozłowski": 4, "Karolina Jankowska": 5, "Łukasz Mazur": 3.5, "Magdalena Krawczyk": 2,
            "Bartosz Nowak": 4.5, "Norbert Król": 4, "Oliwia Pawlak": 5, "Damian At-": 5}
def exec_1_2():
    d_1 = {}
    d_2 = dict()
    print(type(d_1), type(d_2))


def exec_2_2():
    d_1 = {"name": "Lorem", "surname": "Ipsum", "age": 25}
    print(d_1)


def exec_2_3():
    d_1 = {"name": "Lorem", "surname": "Ipsum", "age": 25}
    print(d_1)
    d_1["City"] = "Radom"
    print(d_1)


def exec_2_4():
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 25})
    print(d_1)
    d_1["name"] = "Lorem_1"
    print(d_1)


def exec_2_5():
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 25})
    d_1["City"] = "Radom"
    print(d_1)
    d_1.pop("City")
    print(d_1)


def exec_2_6():
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 25})
    print("Lorem" in d_1)


def exec_2_7():
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 25})
    print(d_1["name"])


def exec_2_8():
    default_value = "Radom"
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 25})
    print(d_1.get("City", default_value))


def exec_2_9():
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 25})
    print(d_1.keys())


def exec_2_10():
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 25})
    print(d_1.values())


def exec_2_11():
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 25})
    print(d_1.items())


def exec_2_12():
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 25})
    print(len(d_1))


def exec_2_13():
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 25})
    d_1.clear()
    print(d_1)


def exec_2_14():
    #Metoda pop usuwa elementy z listy lub słownika
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 25})
    print(len(d_1), d_1)
    d_1.pop("age")
    print(len(d_1), d_1)
    l_1 = list(("name", "surname", "age"))
    print(len(l_1), l_1)
    l_1.pop(2)
    print(len(l_1), l_1)
    #Metoda get dostępna jest tylko dla słownika i pobiera konkretną wartość klucza
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 25})
    print(len(d_1), d_1)
    print(len(d_1), d_1.get("age"))


def exec_2_15():
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 25})
    d_2 = d_1.copy()
    print(d_2)


def exec_2_16():
    d_1 = dict({1: 9})
    d_2 = dict({2: 8})
    d_1.update(d_2)
    print(d_1)


def exec_2_17():
    tuple_list = tuple([("a", 1), ("b", 2)])
    ##d_1 = dict({})
    d_1 = {k:v for (k, v) in tuple_list}
    #Do wykorzystania dict comprehension
    print(d_1)


def exec_2_18():
    d_1 = dict({"name": "Lorem", "surname": "Ipsum", "age": 30, "City": None})
    print(d_1)
    if d_1.get("City") is None:
        d_1["City"] = "Radom"
    print(d_1)


def exec_2_19():
    mylist = [1,4,5,6,7,8,5,4,2,1]
    d_1 = dict()
    for i in mylist:
       d_1[i] = d_1.get(i, 0) + 1
    print(d_1)


def recurrent_function(n):
    if n >= 0:
        print(n)
        recurrent_function(n - 15)


def reccurent_function_1(n):
    if n == 10:
        print(10)
    else:
        print(n), reccurent_function_1(n+1)


def decorator(func):
    def wrapper():
        print("Start")

        time.sleep(1)
        func()
        print("Koniec")
    return wrapper()


#@decorator
def number_count():
    for i in range(1,11):
        print(i)
        time.sleep(1)


def exec_3_1():
    #Metoda setdefault
    #Dla istniejącego klucza funkcja nie zadziała, bo klucz już ma przypisaną wartość
    #Dla nowych kluczy, jeżeli nie będzie żadnej wartości podanej to wstawi domyślną.
    dic_1 = {"name": "Damian"}
    print(dic_1)
    dic_1.setdefault("name", "Kacper" )
    print(dic_1)
    dic_1.setdefault("surname", "Parjaszewski")
    print(dic_1)


def exec_3_2():
    dic_0 = {
        "Marcin":
            {
            "wiek": 15,
            "gatunek": "kot",
            "odgłos": "miau",
            "ilość_nóg": 4
            },
        "Paweł":
            {
            "wiek": 20,
            "gatunek": "pies",
            "odgłos": "hau",
            "ilość_nóg": 4
            },
        "Szymon":
            {
            "wiek": 5,
            "gatunek": "jaszczurka",
            "odgłos": "__",
            "ilośc_nóg": 4
            }
    }
    print(dic_0)


def exec_3_4():
    dic_0 = {
        "Marcin":
            {
                "wiek": 15,
                "gatunek": "kot",
                "odgłos": "miau",
                "ilość_nóg": 4
            },
        "Paweł":
            {
                "wiek": 20,
                "gatunek": "pies",
                "odgłos": "hau",
                "ilość_nóg": 4
            },
        "Szymon":
            {
                "wiek": 5,
                "gatunek": "jaszczurka",
                "odgłos": "__",
                "ilość_nóg": 4
            }
    }
    my_list = []
    for i in dic_0.keys():
        my_list.append(i)
        if my_list.index(i) == 1:
             print(i, dic_0[i]["ilość_nóg"])


def exec_3_5():
    dic_temp = dict({
        "Marcin":
            {
                "wiek": 15,
                "gatunek": "kot",
                "odgłos": "miau",
                "ilość_nóg": 4
            },
        "Paweł":
            {
                "wiek": 20,
                "gatunek": "pies",
                "odgłos": "hau",
                "ilość_nóg": 4
            },
        "Szymon":
            {
                "wiek": 5,
                "gatunek": "jaszczurka",
                "odgłos": "__",
                "ilość_nóg": 4
            }
    })
    dic_temp["Krzysztof"] ={"wiek": 15, "gatunek": "tygrys", "odgłos": "miau", "ilość_nóg": 4}
    dic_temp.update({"Krzysztof":
            {
                "wiek": 15,
                "gatunek": "tygrys",
                "odgłos": "__",
                "ilość_nóg": 4
            }
    })
    print(dic_temp)


def exec_3_6():
    dic_0 = {
        "Marcin":
            {
            "wiek": 15,
            "gatunek": "kot",
            "odgłos": "miau",
            "ilość_nóg": 4
            },
        "Paweł":
            {
            "wiek": 20,
            "gatunek": "pies",
            "odgłos": "hau",
            "ilość_nóg": 4
            },
        "Szymon":
            {
            "wiek": 5,
            "gatunek": "jaszczurka",
            "odgłos": "__",
            "ilośc_nóg": 4
            }
    }
    for i in dic_0.keys():
        print(i, dic_0[i])


def exec_3_7():
    dic_0 = {"e": 5, "c": 3, "a":1, "b":2}
    print(dic_0)
    print(dict(sorted(dic_0.items(), reverse=False)))


def exec_3_8(n):
    dict_0 = {n: n+1 for n in range(n)}
    print(dict_0)


def exec_3_9(n):
    dict_0 = {n: n*2 for n in range(n)}
    print(sum(dict_0.values()))


def exec_3_10(): #D3 = d1.copy() i do tego
    d1 = {"a": 100, "b": 200, "c": 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    for i in d1.keys():
       if i in d2.keys():
           d1.update({i: d1[i] + d2[i]})
    for y in d2.keys():
       if y not in d1.keys():
          d1.update({y: d2[y]})
    print(d1)


def exec_3_11():
    user_input = input("Wpisz slowo: ")
    d_1 = dict()
    for i in user_input.lower():
        d_1[i] = d_1.get(i, 0) + 1
    print(d_1)


def exec_3_12(sentence: str):
    #dict_for_word = {i: 0 #Co tutaj można być#  for i in word.split()}
    dict_for_word = dict()
    for i in sentence.split():
        dict_for_word[i] = dict_for_word.get(i, 0) + 1
    print(dict_for_word)



def exec_3_13():
    dict_func = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
    check_value = [True if dict_func[i] == 12 else False for i in dict_func]
    print(all(check_value))

#14 do omówienia jak zrobić
def exec_3_14():
    element = 0
    my_dict= {"Człowiek": {"imie": "Damian", "nazwisko": "Parjaszewski"}}
    if isinstance(my_dict, dict):
        element = element + 1
        print(True)
        print(element)
    else:
        print(False)


def exec_3_15():
    students_new = {k:(v if v == 5 else v+1) for k, v in students.items()}
    print(students)
    print(students_new)


def exec_3_16():
    temp_dict = dict()
    for i in students:
        if students[i] == min(students.values()):
            temp_dict[i] = students[i]
    print(temp_dict)


def exec_3_17():
    mark_to_find = 5
    for i in students:
        if students[i] == mark_to_find:
            print(i,students[i])


def exec_3_18():
    temp_list_keys = [k for k in students.keys()]
    temp_list_values = [v for v in students.values()]
    avg = round(sum(temp_list_values) / len(temp_list_keys), 1)
    print(avg)


def exec_3_19():
    my_students = students
    for i in my_students.copy():
        if my_students[i] >=3:
            my_students.pop(i)
    print(my_students)


def exec_3_20():
    my_student = dict(sorted(students.items()))
    print(my_student)


def exec_3_21():
    sorted_surname_dict = dict()
    temporary_list = [i.split(" ") for i in students]
    surname_list = sorted([y[1] for y in temporary_list])
    #Obsługa małych liter w słowniku - należy pamiętać
    for surname in surname_list:
        for single_element in students:
            if surname in single_element:
                sorted_surname_dict[single_element] = students[single_element]
                break
    print(sorted_surname_dict)


def exec_3_22():
    surname_dict = dict()
    temporary_list = [i.split(" ") for i in students]
    surname_list = [y[1] for y in temporary_list]
    for surname in surname_list:
            surname_dict[surname] = None
    print(surname_dict)


def exec_3_23():
    temporary_list = list()
    for i in students.items():
        temporary_list.append(i)
    temporary_list = sorted([i for i in students.items()], key=lambda item: item[1], reverse=False)
    print(temporary_list[:3])


def exec_3_24():
    students.update({"Adam Ondra": None}) #Wartość może być pusta bez "None"? Jak wtedy to obsłużyć
    for i in students.copy():
        if students[i] is None:
            print(f"Usunięto {i, students[i]}")
            students.pop(i)
    print(students)


def exec_3_25():
    students.update({None: 3})
    for i in students.copy():
        if i is None:
            print(f"Usunięto {i, students[i]}")
            students.pop(i)
    print(students)


def exec_3_26():
    #Nie da się tego zamienić jeżeli klucze się powtarzają (np. 5)
    temporary_dict = dict({w: k for k, w in students.items()})
    print(temporary_dict)





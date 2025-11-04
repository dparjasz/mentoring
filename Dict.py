import time
#DICTIONARIES
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
def NumberCount():
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
    dic_0["Krzysztof"] ={"wiek": 15, "gatunek": "tygrys", "odgłos": "miau", "ilość_nóg": 4}
    dic_0.update({"Krzysztof":
            {
                "wiek": 15,
                "gatunek": "tygrys",
                "odgłos": "__",
                "ilość_nóg": 4
            }
    })
    print(dic_0)


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


def exec_3_10():
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

exec_3_11()
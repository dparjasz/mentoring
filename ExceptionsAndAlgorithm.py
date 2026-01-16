from datetime import date
from itertools import count
from math import sqrt

from Lists import my_list


#Wyjątki do opracowania

#Zadanie 8
class PythonTasksError(Exception):
    if date.today().weekday() == 0:
        print("Dzisiaj jest poniedziałek")

class WednesdayError(PythonTasksError):
    def is_it_wednesday_my_dudes(self):
        raise WednesdayError



#Zadanie 9
class SmallScreenError(Exception):
    """Raised when needed"""

class NegativeRootError(Exception):
    """Raised when needed"""

class Calculator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def add(self):
        sum_numbers = self.a + self.b
        if sum_numbers > 1000000:
            raise SmallScreenError("Milion przekroczony")
        else:
            return sum_numbers

    def substract(self):
        return self.a - self.b

    def divide(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            raise ZeroDivisionError("Nie dzielimy przez zero")

    def sqrt_1(self): #Do omówienia
        try:
            sqrt(self.x)
        except ValueError:
            raise NegativeRootError("Liczba jest ujemna")
        else:
            return sqrt(self.x)

# while True:
#     first_user_character = int(input("Pierwsza liczba: "))
#     second_user_character = int(input("Druga liczba: "))
#     print("Co mam wykonać? \n 1.Dodawanie \n 2.Odejmowanie  \n 3.Dzielenie")
#     user_choice = int(input("Co zrobić: "))
#     new_calculating = Calculator(first_user_character, second_user_character)
#     if user_choice == 1:
#         print(new_calculating.add())
#         break
#     if user_choice == 2:
#         print(new_calculating.substract())
#         break
#     if user_choice == 3:
#         print(new_calculating.divide())
#         break
#     if user_choice > 3:
#         print("Brak działania. Spróbujmy jeszcze raz")
#         continue

#Zadanie 10
user_data = {
    "name": "Jan",
    "age": 17,
    "email": "jan@gmail.com",
}
len_name = 50
max_age = 130
class StringCheck(Exception):
    """No string"""
class FirstCharacterCheck(Exception):
    """First string is upper"""
class CharacterCheck(Exception):
    """Other characters check"""
class NameLenCheck(Exception):
    """Len of string out of range"""
class IntCheck(Exception):
    """No int"""
class AgeCheck(Exception):
    """Age check """
class LackOfAt(Exception):
    """At"""
class DomainCheck(Exception):
    """DomainCheck"""

class Values:
    def __init__(self, x: dict):
        self.x = x
        self.name = x["name"]
        self.age = x["age"]
        self.email = x["email"]

    def check_type(self):
        if type(self.x) == dict:
            return True
        return False

    def check_name(self):
        if type(self.name) != str:
            raise StringCheck("Typ danej dla tekstu jest nieprawidłowy")
        if len(self.name) > len_name:
            raise NameLenCheck("Imie jest za długie. Sprawdz jeszce raz")
        print("Name ok")

    def check_age(self):
        if type(self.age) != int:
            raise IntCheck("Typ danej dla wieku jest nieprawidłowy")
        if self.age > max_age:
            raise AgeCheck("Trochę dużo. Sprawdź jeszcze raz")
        print("Age ok")

    def check_email(self):
        popular_domains = ["outlook.com", "gmail.com", "wp.pl", "op.pl"]
        if not '@' in self.email:
            raise LackOfAt("Brak '@' w adresie. Sprawdź jeszce raz")
        x = list(self.email.split('@'))
        if x[1] not in popular_domains:
            raise DomainCheck("Domena niepoprawna. Sprawdź jeszcze raz")
        print("Email ok")

#Zadanie 11
def buble_sort(number_list):
    size = len(number_list)
    for i in range(size):
       for j in range(0, size-i-1):
           if number_list[j] > number_list[j+1]:
               number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
               print(number_list)

#Zadanie 11A
def buble_sort_1(x):
    not_sorted = True
    while not_sorted:
        for i in range(0, len(x)-1):
            if x[i] > x[i+1]:
                 x[i], x[i+1]= x[i+1], x[i]
                 break
            else:
                not_sorted = False
    return x

#Zadanie 12


#Zadanie 13
class NoneType(Exception):
    """Exception for NoneType"""


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.count = 0

    def append_value(self, data):
        new_element = Node(data)
        if self.head is None:
            self.head = new_element
            self.count = self.count + 1
            return
        curr_item = self.head
        while True:
            if curr_item.next is None:
                curr_item.next = new_element
                self.count = self.count + 1
                return
            curr_item = curr_item.next

    def find_value(self, value):
        curr_item = self.head
        if curr_item is None:
            print("Lista jest pusta")
        while curr_item.data != value: #Jak obsłuzyć błąd jak na przykład wpisze "C"?
            curr_item = curr_item.next
        print(f"Odnaleziono {value} w {curr_item}")


    def delete_first_value(self, value):
        curr_item = self.head
        if curr_item.data == value:
            self.head = curr_item.next
            self.count = self.count - 1
            return

    def display_elements(self):
        elements = []
        curr_item = self.head
        while curr_item is not None:
            elements.append(curr_item.data)
            curr_item = curr_item.next
        elements.append("None")
        print(elements)

    def __len__(self):
        return self.count

    def __iter__(self):
        return self.head.data

    def __next__(self):
        curr_item = self.head
        if curr_item is None:
            print("brak")
        curr_item = curr_item.next
        return curr_item.data

ll = LinkedList()
ll.append_value("A")
print(f"Liczba elementów na liście: {ll.__len__()}")
ll.display_elements()
ll.append_value("B")
print(f"Liczba elementów na liście: {ll.__len__()}")
print(ll.__iter__())
print(ll.__next__())

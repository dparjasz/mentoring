from idlelib.debugobj_r import remote_object_tree_item
from idlelib.sidebar import temp_enable_text_widget


class ExecOne:
        def __init__(self, name, breed, number_of_legs, age):
            self.breed = breed
            self.name = name
            self.age = age
            self.number_of_legs = number_of_legs

        def __str__(self):
            return f"Hej, w tej klasie jest: {self.name}" ##Wyświetlanie konkretnych informacji o klasie lub atrybuty

        def __repr__(self):
            return f"ExecOne (breed = {self.breed})"

        def make_sound(self):
            print(f"{self.name} daje głos Woof")


class Animal:
    def __init__(self, name, breed, number_of_legs, age):
        self.breed = breed
        self.name = name
        self.age = age
        self.number_of_legs = number_of_legs

    def make_sound(self):
        raise NotImplemented

    def __str__(self):
        return f"{self.name},{self.breed}"

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} daje głos Woof")


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} daje głos miau")


class ExecTwoCounter:
        def __init__(self, counter):
            self.counter = counter

        def increment(self):
            self.counter += 1

        def show(self):
            print(self.counter)

        def reset(self):
            self.counter = 0
            self.show()


class ExecThreePerson:
      def __init__(self, name: str, surname: str):
          self.name = name
          self.surname = surname
          self.full_name = self.name + " " + self.surname

      def introduce(self):
          print(f"Cześć, nazywam się {self.full_name}")

      def __eq__(self, other):
          return (self.name == other.name and
                  self.surname == other.surname)

class ExecSixBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        return self.pages


#Zadanie 10
class Mother:
    def __init__(self, eye_color="Blue", account = 1000):
        self.eye_color = eye_color
        self.__account = account

    def __str__(self):
        return f"Kolor oczu: {self.eye_color}"

class Father:
    def __init__(self, eye_color="Brown"):
        self.eye_color = eye_color


class Child(Mother):
   # def __str__(self):
        #return f"Show{self.__account}"
    pass
    #def __str__(self):
        #return f"Kolor oczu dziecka to {self.eye_color}"

objectFather = Father()
objectMother = Mother()
objectChild = Child()



#Zadanie 11
class PersonChild(ExecThreePerson):
    def __eq__(self, other):
        return self.name == other.name


newChild = PersonChild("Patryk", "Parjaszewski")
newPerson = ExecThreePerson("Damian", "Parjaszewski")
#print(newChild==newPerson)

#Zadanie 12
newPerson_1 = ExecThreePerson("Damian", "Bambaro")
newChild_1 = PersonChild("Damian", "Parjaszewski")



#Zadanie 13
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        #Zadanie 14
        if self.__balance < 0:
            print("Posiadasz ujemny balans")
        else:
            print(self.__balance)

    def set_balance(self, value):
        self.__balance = value


newObject_1 = BankAccount(500)


#Zadanie 15 - do omówienia
class RivalBankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @balance.deleter
    def balance(self):
        del self.__balance

newObject = RivalBankAccount(100)
print(newObject.balance)

#Zadanie 16
class Temperature:
    def __init__(self, temperature = 101):
       self._celsius = temperature
       self._fahrenheit = temperature

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, temperature):
        if temperature < 5:
            self._celsius = temperature
        else:
            self._celsius = 3

    @property
    def fahrenheit(self):
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, value):
        if value > 3:
            self._fahrenheit = value
        else:
            self._fahrenheit = value


class Parent:
    def __init__(self, surname):
        self.surname = surname

    def speak(self):
        print("testestest")

class Parent1:
    def __init__(self, surname):
        self.surname = surname

    def speak(self):
        print("Wolno")
        print(self.surname)



class Child(Parent, Parent1):
     def speak(self):
         Parent.speak(self)
         Parent1.speak(self)


newParent = Parent("Lorem_1")

newChild_2 = Child("Lorem")

newChild_2.speak()





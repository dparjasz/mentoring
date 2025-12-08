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
    #def __init__(self, eye_color="Blue"):
        #self.eye_color = eye_color
    eye_color = "Blue"
    def __str__(self):
        return f"Kolor oczu matki to {self.eye_color}"

class Father:
    def __init__(self, eye_color="Brown"):
        self.eye_color = eye_color

    def __str__(self):
        return f"Kolor oczu ojca: {self.eye_color}"

class Child(Mother):
    def __str__(self):
        return f"Kolor oczu dziecka to {Mother.eye_color}"

objectFather = Father()
objectMother = Mother()
objectChild = Child()
print(objectChild)

#Zadanie 11
class PersonChild(ExecThreePerson):
    def __eq__(self, other):
        return self.name == other.name


newChild = PersonChild("Patryk", "Parjaszewski")
newPerson = ExecThreePerson("Damian", "Parjaszewski")
print(newChild==newPerson)

#Zadanie 12
newPerson_1 = ExecThreePerson("Roberto", "Alwaro")
newChild_1 = PersonChild("Roberto", "Bambaro")

print(newPerson_1==newChild_1)
print(newChild_1 == newPerson_1)






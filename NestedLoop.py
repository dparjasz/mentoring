

def exec_1():
    for i in range(1,11):
        for j in range(1,11):
            print(i*j, end="  ")
        print()

def exec_2(x, y):
    for i in range(x):
        for j in range(y):
            print("*", end="")
        print()

def exec_3(n):
    #n = bok kwadratu
    if n % 2 == 0:
        print("Musi być nieparzysta")
    else:
        for i in range(0, n):
            for j in range(1, n+1):
                if (i+j) % 2 == 0:
                    print("", end="  ")
                else:
                    print("*", end="  ")
            print()

def exec_3a(n):
    print("")



def exec_4(n):
    for j in range(n):
        for i in range(j, n):
            print("", end="   ")
        for i in range(j):
            print("*", end="  ")
        for i in range(j + 1):
            print("*", end="  ")
        print()

def exec_6():
    for i in range(8):
        for j in range(8):
            print("#", end = "  ")
        print()


def exec_7():
    for i in range(17,0,-1):
       for j in range(8):
            print("+", end = " ") if i % 2 !=0 else print("|", end = " ")
            for k in range(1):
                print(" ", end = " ") if i % 2 == 0 else print("", end = "") if j == 8 else print("-", end = " ")
       print("+", end=" ") if i % 2 != 0 else print("|", end=" ")
       print(int(i/2) if i % 2 ==0 else "")


def exec_8(r: int, c: int, m: list):

    #obsługa zera dodatkowo
    this_r = r - 1
    this_c = c - 1
    row_list = [j for j in m[this_r]]
    print(f"Wybrany wiersz {r} \n"
          f"Suma wszystkich elementów: {sum(row_list)} \n"
          f"Oto elementy: {row_list}")
    column_list = [i[this_c] for i in m]
    print(f"Wybrana kolumna {c} \n"
          f"Suma wszystkich elementów: {sum(column_list)} \n"
          f"Oto elementy: {column_list}")


# row = input("Podaj wiersz: ")
# column = input("Podaj kolumne: ")
# matrix = [[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]]
#
# exec_8(int(row), int(column), matrix)

def exec_11(n):
    #Do ogarnięcia trójkąt Pascala w ramach pętli
    for i in range(1, n+1):
        for j in range(i):
            print(i-j, end = " ")
        print()
exec_11(4)


def exec_12(n):
    for i in range(1,n+1):
        for j in range(1, n+1):
            print(i,j)
        print()


def decorator(func):
    def wrapper():
        my_function = func()
        for i in my_function:
            print("*", end = "")
        print(my_function)
    return wrapper()

@decorator
def exec_14():
    return "Hello"

exec_14
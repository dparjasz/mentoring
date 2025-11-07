

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
#exec_2(5,5)

def exec_3(n):
    #n = bok kwadratu
    for i in range(0, n):
        for j in range(1, n+1):
            if (i+j) % 2 != 0:
                print("*", end = "  ")
            else:
                print("", end = "   ")
        print()


def exec_3a(n):
    #n = bok kwadratu
    if n <= 4:
        n = 4
    for i in range(0, n):
        for j in range(1, n+1):
            print(i+j, end = "")
            #if (i+j) % 2 != 0:
              #  print("", end = "  ")
           # else:
                #print("*", end = "   ")
        print()
#exec_3a(2)

def exec_4(n):
    if n < 3:
        n = 3
    for i in range(1, n+1):
        for j in range(n-i):
            print(j , end = "   ")
        for k in range(1,2*i):
            print(k, end = "   ")
        print()



def exec_6():
    for i in range(8):
        for j in range(8):
            print("#", end = "  ")
        print()


def exec_7():
    #znaki: +, -, |
    for i in range(17,0,-1):
       for j in range(9):
            if i % 2 != 0:
                print("+", end=" ")
            else:
                print("|", end=" ")
            for k in range(2):
                if i % 2 == 0:
                    print(" ", end = " ")
                else:
                    if j == 8:
                        print("", end = "")
                    else:
                        print("-", end = " ")
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


row = input("Podaj wiersz: ")
column = input("Podaj kolumne: ")
matrix = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

exec_8(int(row), int(column),matrix)




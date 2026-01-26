def exec_3_27(n):
    if n == 1:
        print(n)
    else:
        print(n)
        exec_3_27(n-1)


def exec_3_28(from_one, n):
    if from_one > n:
        return
    print(from_one)
    exec_3_28(from_one + 1, n)
    print(from_one) #W ten sposób rekurencja wróci do 1 (z 20)


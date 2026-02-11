import random

import numpy as np
from pandas.core.apply import normalize_keyword_aggregation
from pandas.core.computation.expressions import where

#1
temp_list = [x for x in range(0,11)]

#2
new_list = np.array(temp_list)

#3
#print(type(new_list))
#print(np.shape(new_list))

#4
new_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#print(new_array)

#5
dim_one_zeros = np.zeros((10, 1))
#print(dim_one)
dim_two_zeros = np.zeros((5, 4))
#print(dim_two)

#6
dim_one_ones = np.ones((10, 1))
#print(dim_one_ones)
dim_two_ones = np.ones((5,4))
#print(dim_two_ones)

#7
array_with_range = np.arange(0,21,2)
#print(array_with_range)

#8
array_with_lind = np.linspace(0, 1, num=5)
#print(array_with_lind)

#9
array_eye = np.eye(4,4, k=0)
#print(array_eye)

#10
array_random = np.random.randint(1,100, 10)
#print(array_random)

#11
a = np.array([1, 2, 3])
b = np.array([5, 4, 6])

array_substract = a - b
array_sum = a + b
array_multiply = a * b

#print(array_substract)
#print(array_sum)
#print(array_multiply)

#12
pow_a = np.power(a,2 )
#print(pow_a)

#13
maks_value = b.max()
#print(maks_value)
min_value = b.min()
#print(min_value)
avg_value = b.mean()
#print(avg_value)

#14
sq = np.sqrt(b)

#15
arr = np.arange(10,20)
#print(arr)
#print(arr[0])
#print(arr[2])
#print(arr[-1])
#print(arr[2:8])
#print(arr[::-1])

#16
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#print(m)
#print(m[0])
#print(m[:,1])
#print(m[m > 5])

#17
x = np.arange(1,21)
# print(x)
t = x[x % 3 == 0]
#print(t)
#s = x
#s[s > 10] = 99
#print(s)
# print((x < 8).sum())
# print(sum(x[x % 2 ==0]))

#18
one = np.where(x>10,1,x)
zero = np.where(x<=10, 0, x)
both = np.where((x<10) & (x<=10), 0, 1)
#print(one)
#print(zero)
#print(both)


#19
temp_array = np.random.randint(1, 100, np.array(15))
average = round(np.average(temp_array))
#print(temp_array)
#print(f"Średnia: {average}")
#print(temp_array[temp_array < average])

#20
arr_test = np.array([3,-7,0,5,-2,9])
arr_test[(arr_test < 0)] = 0
arr_test[(arr_test > 5)] = 5
#print(arr_test)

#21
new_arr = np.random.randint(1, 10, np.array([4,4]))
new_arr_2 = np.random.default_rng()
# print(new_arr)
# print(np.where(new_arr % 2 == 0, 1, -1))

#22
arr_3 = np.arange(1,10).reshape(3,3)
# print(arr_3)
# print(np.sum(arr_3, axis=1))
# print(np.sum(arr_3, axis=0))
# print(arr_3.max())
# print(arr_3.min())
# print(np.mean(arr_3, axis=1))

#23
A = np.array([[2,3], [1,3]])
B = np.array([[5,5], [3,1]])

sum_ = np.add(A, B)
substract_ = np.subtract(A,B)
multiply_ = np.multiply(A,B)

#23 - B
C = np.matmul(A, B)
#print(C)

#23 - C
D = np.linalg.inv(A)
#print(np.matmul(A, D))

#24
matrix_A = np.arange(1,17).reshape(4,4)
#24a
#print(np.diag(matrix_A))
#24b,c
row_reverse = np.flip(matrix_A, axis=1)
col_reverse = np.flip(matrix_A, axis = 0)

#24d
matrix_A[[0,-1]] = matrix_A[[-1,0]]
#print(matrix_A)

#24e
one_dim = np.reshape(matrix_A, -1) #lub ravel
#print(one_dim)

#26 #Normalizacja do ogarnięcia
c = np.array(np.random.randint(1,100, size = 10), dtype= float)
normalized = (c - np.min(c)) / (np.max(c) - np.min(c))

#26a
arr_4 = np.array(np.random.rand(20))
#print(np.mean(arr_4))
#print(np.median(arr_4))
#print(np.var(arr_4))
#print(np.std(arr_4))

#26b
arr_mean = np.mean(arr_4)
absolute_arr = np.absolute(arr_4 - arr_mean)
get_min= absolute_arr.argmin()
#print(arr_4[get_min])

#27
arr_5 = np.random.randint(1,100, np.array([3,5]))
#print(np.mean(arr_5, axis=0))
#print(np.mean(arr_5, axis=1))

#28
arr_6 = np.random.rand(100)
#Do zrobienia


#29
arr_7 = np.random.randint(1,100, np.array([10,10]))
#print(arr_7)
arr_7_max = arr_7.max()
#print(f"Max: {arr_7_max}")
arr_7_min = arr_7.min()
#print(f"Min: {arr_7_min}")
#print(f"Max index: {np.argmax(arr_7)}")
#print(f"Min index: {np.argmin(arr_7)}")

#30
prices = np.array([9.99, 12.49, 7.50, 14.90, 3.99])
#print(f"Średnia: {np.mean(prices)}, Mediana: {np.median(prices)}")
prices = prices + (prices * 23 / 100)
index = np.where(prices>10)
#print(prices[index])

#31
scores = np.array([56, 78, 45, 89, 90, 67, 73, 100, 59])
scores_average = np.mean(scores)
scores_add = np.where(scores<60, scores+10, scores)
scores_above = np.size(np.where(scores>80))
check_rate = round((np.size(np.where(scores>50)) / np.size(scores)) * 100, 1)
#print(f"{check_rate}%")

#32
temps = np.array([[22, 25, 21], [18, 20, 19], [25, 27, 26], [23, 22, 24]])
temps_avg = np.mean(temps, axis=1)
temps_min = np.min(temps)
temps_max = np.max(temps)
temps_F = np.multiply(temps, 2) + 30

#33
random_array = np.array(np.random.choice([0,1], 1000))
no_zero = np.count_nonzero(random_array)
zero_number  =  np.size(random_array) - no_zero
#print(f"Orzeł: {zero_number} \nReszka: {no_zero}")

#34
array_rand = np.random.randint(1,7,100)
print(array_rand)
count = np.bincount(array_rand, weights=None, minlength=0)

#35
array_rand_2 = np.random.randint(1,49, 6)
print(np.random.choice(array_rand_2, size=6, replace=False))


"""

斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，
按照这个规律，斐波那契数列的前10个数是：1, 1, 2, 3, 5, 8, 13, 21, 34, 55。

输出斐波那契数列前20个数

"""

a, b = 1 , 1
print(a, b, end =' ')
for _ in range(18):
    a, b = b, a + b
    print(b, end = ' ')

"""
输出100以内的素数

"""

for num in range(2, 100):
    prime = True # 假设num是素数
    for factor in range(2, num):
        if num % factor == 0:
            prime = False
            break
    if prime:
        print(num)
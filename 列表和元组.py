# 列表 可变类型

"""

将一颗色子掷6000次，统计每个点数出现的次数。



# 麻烦的方法
import random

f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
for _ in range(6000):
    face = random.randint(1, 6)
    if face == 1:
        f1 += 1
    elif face == 2:
        f2 += 1
    elif face == 3:
        f3 += 1
    elif face == 4:
        f4 += 1
    elif face == 5:
        f5 += 1
    else:
        f6 += 1
print(f'1点出现了{f1}次')
print(f'2点出现了{f2}次')
print(f'3点出现了{f3}次')
print(f'4点出现了{f4}次')
print(f'5点出现了{f5}次')
print(f'6点出现了{f6}次')



# 使用列表重写一遍
import random

counters = [0] * 6
for _ in range(6000):
    face = random.randint(1, 6)
    counters[face - 1] += 1
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')

"""

"""

列表的生成式

# 方法一
# 创建一个由1到9的数字构成的列表
items1 = []
for x in range(1, 10):
    items1.append(x)
print(items1)

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = []
for x in 'hello world':
    if x not in ' aeiou':
        items2.append(x)
print(items2)

# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = []
for x in 'ABC':
    for y in '12':
        items3.append(x + y)
print(items3)

# 方法二
# 创建一个由1到9的数字构成的列表
items1 = [x for x in range(1, 10)]
print(items1)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = [x for x in 'hello world' if x not in ' aeiou']
print(items2)    # ['h', 'l', 'l', 'w', 'r', 'l', 'd']

# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = [x + y for x in 'ABC' for y in '12']
print(items3)    # ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']

"""

# 元组 不可变类型

"""

一个元组中如果有两个元素，我们就称之为二元组；一个元组中如果五个元素，我们就称之为五元组。
()表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，否则()就不是代表元组的字面量语法，而是改变运算优先级的圆括号，
所以('hello', )和(100, )才是一元组，而('hello')和(100)只是字符串和整数。

# 空元组
a = ()
print(type(a))    # <class 'tuple'>
# 不是元组
b = ('hello')
print(type(b))    # <class 'str'>
c = (100)
print(type(c))    # <class 'int'>
# 一元组
d = ('hello', )
print(type(d))    # <class 'tuple'>
e = (100, )
print(type(e))    # <class 'tuple'>

"""

"""

打包和解包



# 解包对所有序列都成立
a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)

def add(*args):
    print(type(args), args)
    total = 0
    for val in args:
        total += val
    return total

add(1, 10, 20)
add(1, 2, 3, 4, 5)

"""

"""

让函数返回多个值。
例如，编写一个找出列表中最大值和最小的函数。



def find_max_and_min(items):
    max_one, min_one = items[0], items[0]
    for item in items:
        if item > max_one:
            max_one = item
        elif item < min_one:
            min_one = item 
    return max_one, min_one

aha = (1, 20, 30, 100, 0.1)
print(find_max_and_min(aha))

"""

# 应用
"""

录入5个学生3门课程的考试成绩，计算每个学生的平均分和每门课的平均分。



names = ['金', '木', '水', '火', '土']
courses = ['语文', '数学', '英语']
scores = [[0] * len(courses) for _ in range(len(names))] # 用生成式创建列表嵌套

# 录入成绩
for i, name in enumerate(names):
    print(f'请输入{name}的成绩 ===>')
    for j, course in enumerate(courses):
        scores[i][j] = float(input(f'{course}: '))
print()

# 计算每个人的平均成绩
print('-' * 5, '学生平均成绩', '-' * 5)
for index, name in enumerate(names):
    avg_score = sum(scores[index]) / len(courses)
    print(f'{name}的平均成绩为：{avg_score:.1f}分')
print()

# 计算每门课的平均成绩
print('-' * 5, '课程平均成绩', '-' * 5)
for index, course in enumerate(courses):
    curr_course_scores = [score[index] for score in scores]
    avg_score = sum(curr_course_scores) / len(names)
    print(f'{course}的平均成绩为：{avg_score:.1f}分')

"""

"""

设计一个函数返回指定日期是这一年的第几天。



def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0 # 是闰年的话返回True，平年则返回False

def which_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ]
    days = days_of_month[is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days[index]
    return total + date

print(which_day(1980, 11, 28))    # 333
print(which_day(1981, 12, 31))    # 365
print(which_day(2018, 1, 1))      # 1
print(which_day(2021, 5, 5))      # 125

"""

"""

实现双色球随机选号。
说明：红球号码范围为01～33，蓝球号码范围为01～16。
双色球每期从33个红球中开出6个号码，从16个蓝球中开出1个号码作为中奖号码，
双色球玩法即是竞猜开奖号码的6个红球号码和1个蓝球号码。



from random import randint, sample

def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end= '')
        print(f'{ball:0>2d}', end='')
    print()

def random_select():
    red_balls = [x for x in range(1, 34)]
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls

n = int(input('机选几注：'))
for _ in range(n):
    display(random_select())

"""

"""

幸运的女人(约瑟夫环问题)
说明：有15个男人和15个女人乘船在海上遇险，为了让一部分人活下来，不得不将其中15个人扔到海里，
有个人想了个办法让大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，
他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到将15个人扔到海里。
最后15个女人都幸免于难，15个男人都被扔到了海里。
问这些人最开始是怎么站的，哪些位置是男人，哪些位置是女人。



persons = [True] * 30 # 活着就是True
counter, index, number = 0, 0, 0 # counter - 扔到海里的人，index - 索引，number - 报数的数字
while counter < 15:
    if persons[index]:
        number += 1
        if number == 9:
            persons[index] = False
            counter += 1
            number = 0
    index += 1
    index %= 30
for person in persons:
    print('女' if person else '男', end='')

"""
"""

例子1：设计一个生成指定长度验证码的函数。
说明：验证码由数字和英文大小写字母构成。
(默认4个字符)



import random
import string

ALL_CHARS = string.digits + string.ascii_letters

def generate_code(code_len = 4):
    return ''.join(random.choices(ALL_CHARS, k=code_len)) #如果使用sample代替choices，将会实现无放回抽样

for _ in range(10):
    print(generate_code())

"""

"""

例子2：设计一个函数返回给定文件名的后缀名。
说明：在Windows系统上，后缀名exe表示这是一个可执行程序，而后缀名txt表示这是一个纯文本文件。
需要注意的是，在Linux和macOS系统上，文件名可以以.开头，表示这是一个隐藏文件，
像.gitignore这样的文件名，.后面并不是后缀名，这个文件没有后缀名或者说后缀名为''。



#def get_suffix(filename):
#    pos = filename.rfind('.')
#    return filename[pos + 1:] if pos > 0 else ''

from os.path import splitext

def get_suffix(filename):
    return splitext(filename)[1][1:]

print(get_suffix('readme.txt'))       # txt
print(get_suffix('readme.txt.md'))    # md
print(get_suffix('.readme'))          #
print(get_suffix('readme.'))          #
print(get_suffix('readme'))           #

"""

"""

例子3：在终端中显示跑马灯（滚动）文字。
说明：把当前字符串的第一个字符放到要输出的内容的最后面，把从第二个字符开始后面的内容放到要输出的内容的最前面，通过循环重复这个操作，就可以看到滚动起来的文字。
两次循环之间的间隔可以通过time模块的sleep函数来实现，而清除屏幕上之前的输出可以使用os模块的system函数调用系统清屏命令来实现。


import time
import os

content = '老 溪 我 爱 你 '
while True:
    os.system('cls')
    print(content)
    time.sleep(0.5)
    content = content[1:] + content[0]


"""

## Computer-Programming-for-Kids-and-Other-Beginners
## 学习python，关于《与孩子一起学编程》的代码
中文书籍 链接：https://pan.baidu.com/s/1ZtNMKep-Zl62hKN18HzWUw 提取码：70us
=================================================================================
    这个项目的初衷是实践极客时间陈皓的《左耳听风》专栏中[***“程序员练级攻略（2018）”***](http://gk.link/a/100HQ)

    由此接触到了一门现在热火朝天的脚本语言python，这本书也很有意思，书名也叫做与孩子一起学编程，于是想到
    可以和一起在学这本书的小伙伴一起学习和进步，也学着用一下github来管理项目

    下面我列出一些使用这本书的一些资源
    Python Releases for Windows：
        python有2和3两个版本，初学建议从2开始学起，后面可以转3，这本书用的是2
        目前2最新版本地址：
          （64位）https://www.python.org/ftp/python/2.7.15/python-2.7.15.amd64.msi
          （32位）https://www.python.org/ftp/python/2.7.15/python-2.7.15.msi

        其中用到了Pygame、PythonCard和EasyGui三个模块，使用pip管理模块，但是有一些早期的模块还没加入pip，那么
        可以把下载来的模块放在C:\Python27\Lib\site-packages，如果你也和我一样没有改安装目录的话，另外在下载的
        时候一定要注意与python对应的版本，不同的版本可能不起作用，我在使用PythonCard的时候就遇到了这个问题，这个
        模块还要使用另外一个模块wxPython，开始的时候我把这个模块下错了版本，结果PythonCard无法正常使用，能启动，
        但是会报错，在折腾许久之后，终于找到了问题，是wxPython版本太高和PythonCard匹配不上，最后是根据它们两个
        发布的时间相近下载了wxPython。
        
        于是我整理了这些模块放在项目的Source文件夹中
        
        开发工具：前期使用的是Python自带的工具IDLE，后期因为IDLE工具和Pygame模块退出有冲突问题，使用Sublime Text3编辑器
                 关于这个编辑器这里有一些介绍https://www.cnblogs.com/sgal/
# 小试牛刀===

> 命令 计算机 说话:   print 打印 命令
```python
>>> print("你好")
你好
```

> 让计算机 算 算术题：
```python
# 数字运算====
>>> print(10 + 9)
19
>>> print(9 * 9)
81

# 字符的运算=======
>>> print("小明" + "小红")   # 排队，老鹰捉小鸡
小明小红

# 孙悟空 三根猴毛 特技 变 子子孙孙   牛魔王 也有 这个 特技
>>> print('孙悟空'*10)
孙悟空孙悟空孙悟空孙悟空孙悟空孙悟空孙悟空孙悟空孙悟空孙悟空

```
> 小明到饭店吃饭饭
```python
print('我叫小明')
print('我喜欢吃汉堡')
print('汉堡 '*5)
print('我吃饱了')
print('付钱 ')
print(10*5)
```


> 电脑出数字，小朋友猜数字
```python
# -*- coding: utf-8 -*-
# 电脑出数字，小朋友猜数字
# 另外一个 小朋友出数字，电脑猜数字
import random # 大脑 产生随机数

secret = random.randint(1,100)# 电脑出的一个整数，范围1~99
guess = 0 # 小朋友猜的数字
tries = 0 # 尝试的次数

print("小朋友，你将有6次机会猜出我出的数字，范围在1~99之间，开始吧")

# 做游戏，游戏结束的两个条件，1.小朋友猜对了；2.6次机会用完了
while guess != secret and tries < 6:  # 只要没猜对且机会没用完，游戏一直进行
    guess = input("小朋友这次猜多少?")  # 获取小朋友猜的数字 
    if guess < secret:  # 猜小了
        print("小了")
    elif guess > secret:# 猜大了
        print("大了")
    tries = tries + 1
        
if guess == secret:
    print("恭喜你，小朋友，你猜对了")
else:
    print("不要灰心，小朋友，看看答案是多少吧 ")
    print(secret)
```

# 内存和变量

    输入 ----接收外界数据(人类的 眼睛视觉、耳朵听觉、鼻子嗅觉、皮肤触感)
    处理 ----计算机小同学大脑处理数据---小明思考问题
    输出 ----可视化(人类的嘴巴说话、四只运动)
    
    上述猜字谜游戏 中使用的
    guess = input("小朋友这次猜多少?") 就是获取 外界输入的信息
    计算机使用 内存单元 记录 输入的内容 并给它们命名
    使用 guess 该 该内容 命名
```python
>>> student = "小明" # 字符串
>>> print(student)   # 输出 打印信息 到显示器上显示
小明
>>> age = 8     # 整数 数字
>>> print(age)  # 8岁 
8
>>> student = "小红"  # 名字指向了 另一个同学 变化多端
>>> print(student)   # 输出 打印信息 到显示器上显示

>>> age = age + 1  # 全新的我，长大一岁
>>> print(age)     # 9岁 
9

# 命名中的学问
Xiaoming  和 xiaoming一样么?   1.区别大小写
teacher 
teacher2
2teacher        必须以字母或者_开头
teacher_2       除了字母、数字、_外不能用其他字符
teaChen

```

# 基本数学运算
1.加 +   2.减 - 3.乘 *  4.除 //  5.整数除法 /   6.取余数 %  7. 指数运算 ** 8. 
```python
>>> 5/2
2
>>> 5//2
2.5
>>> 5.0/2
2.5
>>> 5%2
1
>>> 7 + 3    加数7 + 被加数3 
10

>>> 2 + 3 * 4
14
>>> (2 + 3) * 4
20

>>> 3*3*3*3
81
>>> 3 ** 4  四个 3 相乘

# 自增、自减、自乘...
>>> age = 8
>>> age += 1
>>> print(age)
>>> 9
>>> age -= 2
>>> print(age)
>>> 7
>>> age *= 3
>>> print(age)
>>> 21

# 科学计数法
>>> 3e2 # 3 乘以 10 的平方
300     # 3 * 10*10

```

# 数据类型
    内置函数实现类型强转
    整数int()    从一个字符串或整数创建一个新的整数(自然数+0+负自然数) 
    小数float()  从一个字符串或整数创建一个新的小数(浮点数 float 浮动的)
    字符str()    从一个任意类型的数创建一个新的字符串
```python
a=24        # 整数转浮点数
b=float(a)
print(b)
>>> 24.0
print(a)
>>> 24

c=38.6       # 浮点数转整数
d=int(c)     直接砍掉小数部分
print(d)
>>> 38
print(c)
>>> 38.6

h='99.9'    # 字符串转小数
i=float(h) 
print(i)
>>> 99.9
print(h)
>>> '99.9'

type(h) # 查看 数据 更多的信息
```


# 输入
```python
# 下朋友按键盘，这里会得到 按下的字符数组等
someName = raw_input()  

print('小朋友，你好，请输入你的名字')
someBody = raw_input()
print('你好 ',someBody,' 今天过得怎么样')

# 更简单的，使用 raw_input直接打印提示语
someBody = raw_input('小朋友，你好，请输入你的名字')

# 输入数据
ages = int(raw_input('小朋友，你好，请输入你的年龄'))
print('小朋友都长这么大了','真好')

# 3.0以后的版本， input() 得到的也只是字符串，需要使用一些函数进行转换才能得到数字


# 从互联网 中的一个文件 得到输入=====
# python2.0+========
import urllib
file = urllib.urlopen('http://helloworldbook.com/data/message.txt')
message = file.read()
print message 
# python 3.0+=======
import urllib.request
file = urllib.request.urlopen('http://helloworldbook.com/data/message.txt')
ssage = file.read()
print message 
```


# GUI 图形用户界面，可是化界面，人机交互界面，计算机的大脸蛋^_^

```python
# 使用 easygui 包，利用这个模块可以很容易地建立简单的 GUI
# 使用前需要先安装该模块
import easygui as eg # 导入该模块

# 显示一个带有 OK按钮的 简单消息框=======
eg.msgbox('Hello World!')
# 点击消息框上的 OK 按钮，该消息框会关闭

# 返回用户 的反馈信息
user_response = eg.msgbox('Hello World!')
print(user_response)

# 按钮框=======buttonbox============
flavor = eg.buttonbox("What is your favorite ice cream flavor?", choices = [' Vanilla', 'Chocolate', 'Strawberry'])
# choices 列表选择框，三个按钮
# 再 显示消息框，显示 小朋友选择的 最爱
eg.msgbox("You picked " + flavor)  


# 选择框====choicebox===============
flavor = eg.choicebox("What is your favorite ice cream flavor?", choices = ['Vanilla', 'Chocolate', 'Strawberry'])
# 列表选择框
eg.msgbox ("You picked " + flavor) 

# 字符文本输入框====enterbox=========
flavor = eg.enterbox('what is your favorite ice cream flavor?', default = 'Vanilla')# 带默认字符
# 会出现一个文本输入框，按OK完成输入内容
easygui.msgbox('you entered ' + flavor) 


# 整数数字文本输入框====integerbox=======
age = eg.enterbox('what is your age')
# 输入整数，不支持输入小数，可以使用上面的文本输入，再使用float()转换到小数
# 会出现一个文本输入框，按OK完成输入内容
easygui.msgbox('you age ' + str(age)) 
```
> 可视化猜数字游戏…
```python
电脑出数字，小朋友猜数字

# -*- coding: utf-8 -*-
# 电脑出数字，小朋友猜数字
# 另外一个 小朋友出数字，电脑猜数字
import random # 大脑 产生随机数
import easygui as eg # 可视化界面

secret = random.randint(1,100)# 电脑出的一个整数，范围1~99
guess = 0 # 小朋友猜的数字
tries = 0 # 尝试的次数

# print("小朋友，你将有6次机会猜出我出的数字，范围在1~99之间，开始吧")
eg.msgbox('小朋友，你将有6次机会猜出我出的数字，范围在1~99之间，开始吧')

# 做游戏，游戏结束的两个条件，1.小朋友猜对了；2.6次机会用完了
while guess != secret and tries < 6:  # 只要没猜对且机会没用完，游戏一直进行
    # guess = input("小朋友这次猜多少?")  # 获取小朋友猜的数字 
    guess = eg.integerbox('What is your guess?')

    if guess < secret:  # 猜小了
        # print("小了")
        eg.msgbox('小了')
    elif guess > secret:# 猜大了
        # print("大了")
        eg.msgbox('大了')
    tries = tries + 1 # 用掉一次机会
        
if guess == secret:
    eg.msgbox("恭喜你，小朋友，你猜对了")
else:
    eg.msgbox("不要灰心，小朋友，看看答案是多少吧 " + str(secret))
    # print(secret)
    
```


# 判断判断判断 一修哥 福尔摩斯 田忌赛马 做决策 

```python
# 数1 == 数2  判断两个数是否相等   
# 数1 != 数2  不等于判断
# 数1 >  数2  大于判断
# 数1 <  数2  小于判断
>=  大于等于
<=  小于等于

区间判断
5 < age < 8
5 <= age <= 8

age = float(raw_input("小朋友输入你的年龄:"))
if age > 10:
    print('小朋友，你超过10岁啦')
else:
    print('小朋友还比较小哦')


结合 逻辑判断 
条件1 and 条件2    # 与，条件1 与 条件2都必须成立，才进入该分支
条件1 or 条件2     # 或，若条件1每成立，则查看条件2，有一个成立，就进入该分支
not 条件           # 非

```

# 循环，转圈圈，呼啦圈
```python
for id in [1,2,3,4,5]:
    print('你好', id)
>>>
你好 1
你好 2
你好 3
你好 4
你好 5

for id in range(1,5):
    print(id, '倍 8 = ', id*8)
>>>
1 倍 8 = 8
2 倍 8 = 16
3 倍 8 = 24
4 倍 8 = 32

# range(1, 5) 给出的列表是 [1,2,3,4]
# range(5) 给出的列表是  [0,1,2,3,4]
# range(l, 10, 2)  给出的列表是 [1,3,5,7,9]
# range (5, 26, 5) 给出的列表是 [5,10,15,20,25]
# range(10, 5, -1) 给出的列表是 [10,9,8,7,6]


while 条件:
    循环体;
    ...
    continue; # 跳过一次循环中的部分代码
    break;    # 结束循环，条件不成立时也会结束循环

```

# 游戏时间到了======

```python
>>>
```

```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```


```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```



```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```




```python
>>>
```


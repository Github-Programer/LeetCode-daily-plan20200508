:octocat:

# LeetCode-daily-plan20200508

 :calendar:力扣每日计划第一天2020\05\08

:hourglass_flowing_sand:练习C++和Python，以仓库来督促:eye:

## :cheese:语言C++，题库：LeetCode力扣

### 1：

## :bread:语言C++，逛论坛

## :cake:语言Python，题库：NowCoder牛客网

### 1：编程初学者入门训练-竞选社长

**题目描述**

假设你们社团要竞选社长，有两名候选人分别是A和B，社团每名同学必须并且只能投一票，最终得票多的人为社长.

**输入描述:**

一行，字符序列，包含A或B，输入以字符0结束。

**输出描述:**

一行，一个字符，A或B或E，输出A表示A得票数多，输出B表示B得票数多，输出E表示二人得票数相等。

**输入**

```
ABBABBAAB0
```

**输出**

```
B
```
**SRC_Code：**:rocket:

```python
# -*- coding: UTF-8 -*-
#!/usr/bin/python3

A = 0
B = 0
s = input()
for i in s:
    if i == 'A':
        A += 1
    elif i == 'B':
        B += 1
if A == B:
    print('E')
elif A > B:
    print('A')
else:
    print('B')
```

### 2：牛客小白月赛15回顾-诡异的因数

**题目描述：**

四舍五入下成功率，大概就是百分之百的样子。   

&emsp;&emsp;&emsp;&emsp;——韩信-逐梦之影  

小T喜欢玩数。这天他弄到了一个数n，他玩心大发，他让小s求它的正因数数量。  

小s并不会这道题，现在如果你是他，你会怎么做？  

小T为了防止小s作弊，他要询问T次。

**输入描述:**

```
第一行一个整数T。

后T行每行一个整数n。
```

**输出描述:**

```
T行一个整数代表答案。
```

**输入**

```
1
6
```

**输出**

```
4
```

**说明**

```
6的因数有1 2 3 6共4个

100% 1≤n,T≤104100\% \ 1 \le n,T \le 10^4100% 1≤n,T≤104
```

**SRC_Code：**:rocket:

```python
# -*- coding: UTF-8 -*-
#!/usr/bin/python3

def check(aNum):
    count = 0
    for i in range(1, aNum + 1):
        if aNum % i == 0:
            count += 1
    return count

T = int(input())
nums = []
for i in range(0, T):
    tmp = int(input())
    nums.append(tmp)

for i in range(0, T):
    tmp = check(nums[i])
    print(tmp)
```


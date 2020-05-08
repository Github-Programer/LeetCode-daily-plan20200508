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
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
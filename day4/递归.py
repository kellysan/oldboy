#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       递归
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-20
#    Change Activity:  2019-04-20:


def fb(n):
    if n == 1 or n == 2:
        return 1
    return fb(n-1) + fb(n-2)


print(fb(10))

# 递归用法
# 二分法查找  头,尾，中间

def binary_search(lst, n, left, right):
    if left <= right:
        mid = (left + right) // 2
        if n > lst[mid]:
            left = mid + 1
            return binary_search(lst, n, left, right)
        elif n < lst[mid]:
            right = mid - 1
            return binary_search(lst,n, left, right)
        else:
            print('找到了')
            return mid
    else:
        print('没找到')
        return -1

lst = [12,14,15,16,17,18,19,20]
n = 16
res = binary_search(lst, n, 0,len(lst) - 1)
print(res)

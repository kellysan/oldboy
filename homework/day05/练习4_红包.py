#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       练习4_红包
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-01
#    Change Activity:  2019-05-01:


import random

"""
基本单位 0.01 获取到的金额必须大于这个数，才能生效
金额和红包个数整除为基本数，那么金额就位0.01

第一个红包金额随机，但是必须得小于输入金额



"""

import random
# summoney=input("please input the amount of money:")
# divide_n=input("divide into?:")

def hongbao(money,n):
    k = n
    sum = 0#sum为前n个人抢得的总和，为了方便计算最后一个人的金额，初始值为0
    round = n#剩余人次
    while k > 1:
        current_money = money  # 当前剩余的钱，初始值为money
        for i in range(1, n+1):
            get_money = random.randint(0, int( 2 * current_money / round))
            print('id[%s] have geted money %s'%(i, get_money))
            current_money -= get_money
            round -= 1
            sum += get_money
            k-=1

    if k==1:#最后一个人，分得剩余的所有
        print('id[%s] have geted money %s'%(n,money-sum))

hongbao(100,10)

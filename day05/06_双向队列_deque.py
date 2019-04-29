#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       06_双向队列_deque
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-27
#    Change Activity:  2019-04-27:

"""
stack 栈
    特点：
        1. 先进来最后出去
        2. 砌墙的站头后来居上
        3. first in last out
deque 队列
    特点：
        1. 先进先出
"""

import queue

"""
step1 导入模块
    import queue

step2 创建队列
    q.queue.Queue()

"""

#### 双向队列

from collections import deque

q1 = deque()
q1.append("牡丹")
q1.append("百合")
q1.appendleft("罂粟")
q1.appendleft("白羊")


print(q1.pop())
print(q1.pop())
print(q1.pop())
print(q1.pop())






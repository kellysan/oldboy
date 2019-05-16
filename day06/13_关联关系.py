#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       13_关联关系
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-11
#    Change Activity:  2019-05-11:

class Teacher:
    def __init__(self, name ,stu_list=[]):
        self.name = name
        self.stu_list = stu_list

    def teach(self):
        print(f"{self.name}在上课")
        for stu in self.stu_list:
            stu.study()

class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name}在学习")


s1 = Student("蔡徐坤")
s2 = Student("潘长江")
s3 = Student("姚明")
s4 = Student("刘翔")

stu_list = [s1, s2, s3, s4]

t = Teacher("alex", stu_list)
t.teach()


def mul():
    return [lambda x: i*x for i in range(4)]


print(mul())

print([m(2) for m in mul()])

#第一次循环 lamdba x: 0 * x
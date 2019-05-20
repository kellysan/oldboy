#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       04
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-18
#    Change Activity:  2019-05-18:

class Person:
    pass


class It(Person):
    pass


a = Person()

b = It()

print(type(a))
print(type(b))

print(issubclass(It, Person))

print(issubclass(Person, It))

print(isinstance(a, Person))



def add(a,b):
    print(type(a))
    print(type(b))
    if type(a) == int or type():
        print(a)
    if type(a) is int or type(a) is float or type(b) is int or type(b) is float:
        return a + b


print(add(1, 2))
#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       装饰器
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-20
#    Change Activity:  2019-04-20:


def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper


@logging(level='INFO')
def say(something1, s2, s3, s4):
    print("say {}{}{}{}!".format(something1,s2,s3,s4))

# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)


@logging(level='DEBUG')
def do(something):
    print("do {}...".format(something))


if __name__ == '__main__':
    say('hello','小姐姐', '大姐姐', '夏哥哥')
    do("my work")
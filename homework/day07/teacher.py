#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       teacher
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-22
#    Change Activity:  2019-05-22:

from base import InfoMode, Base, Database

info = InfoMode()
b= Base()
db = Database()


def examine_all_course():
    course_info = db.db_select("course_info.json")
    print("全部课程".center(20,"#"))
    for c in course_info:
        print("课程名称:{}\n"
              "\t课程价格:{}\n" \
              "\t课程时间{}".format(c, course_info[c].get("price"), course_info[c].get("hour")))
    print("全部课程".center(20, "#"))
    return True


def examine_allot_class():
    """
    查找出老师所分配的班级
    :return:
    """
    user_name = b.check_login_account("name")
    user_info = db.db_select("user_info.json")
    if len(user_info[user_name].get("class")) == 0:
        print("{}老师还没有分配班级，请联系管理员".format(user_name))
        return False
    else:
        print("您所分配的班级:{}".format("|".join(user_info[user_name].get("class"))))
        return True

def examine_all_class_student():
    """

    :return: 显示所有班级的学生信息
    """
    user_name = b.check_login_account("name")
    user_info = db.db_select("user_info.json")
    class_info = db.db_select("class_info.json")
    if len(user_info[user_name].get("class")) == 0:
        print("{}老师还没有分配班级，请联系管理员".format(user_name))
        return False
    else:
        for c in user_info[user_name].get("class"):
            if len(class_info[c].get("student")) == 0:
                print("{}班级没有学生".format(c))
            else:
                print("班级名称：{}\n\t学生列表：{}".format(c, ''.join(class_info[c].get("student"))))


if __name__ == '__main__':
    examine_all_class_student()
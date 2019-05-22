#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       student
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-21
#    Change Activity:  2019-05-21:
"""
学生选课的时候，选择班级，班级人数不能超过30人，超过30人，选择不超过30人的班级 如果不满足条件，需要老师添加班级
"""

from base import InfoMode, Database, Base

info = InfoMode()
db = Database()
b = Base()

def examine_all_course():
    course_info = db.db_select("course_info.json")
    print("全部课程".center(20,"#"))
    for c in course_info:
        print("课程名称:{}\n"
              "\t课程价格:{}\n" \
              "\t课程时间{}".format(c, course_info[c].get("price"), course_info[c].get("hour")))
    print("全部课程".center(20, "#"))
    return True

# def examine_course_class(course_name):
#     """
#     此处是让学生选课之后，直接加入班级，和作业需求有冲突，但是逻辑可以借鉴，
#     在这里的想法是学生选课直接选择班级，分配班级是管理员的事情，这里只需要将课程加入学生的课程列表
#     :param course_name:
#     :return:
#     """
#     class_info = db.db_select("class_info.json")
#     for c in class_info:
#         if class_info[c].get("course") == course_name:
#             if len(class_info[c].get("student")) <= 30:
#                 print("班级信息".center(30, "#"))
#                 print("班级名称:{}\n\t班级讲师:{}".format(c, "||".join(class_info[c].get("teacher"))))
#     return True


def select_course():
    user_info = db.db_select("user_info.json")
    course_info = db.db_select("course_info.json")

    # 打印所有课程
    examine_all_course()

        # 输入选择课程
    while True:
        course_name = input("请输入要选择的课程，输入q退出选课：")
        if course_name == "q":
            break
        else:
            if course_name in course_info:
                user_name = b.check_login_account("name")
                print(user_name)
                print(user_info[user_name].get("course"))
                if course_name in user_info[user_name].get("course"):
                    print("您已经选择此课程，请重新输入")
                    continue
                else:
                    user_info[user_name]["course"].append(course_name)
                    db.db_insert("user_info.json", user_info)

                    print("{}学生选择的课程是:\n\t课程列表{}".format(user_name, "||".join(user_info[user_name].get("course"))))
            else:
                print("您输入的课程名称有误，请重新输入")
                continue

def examine_select_course():
    user_info = db.db_select("user_info.json")
    course_info = db.db_select("course_info.json")
    user_name = b.check_login_account("name")

    print("{}同学选择的课程".center(20, "#").format(user_name.upper()))
    for c in user_info[user_name].get("course"):
        print("课程名称:{}\n\t课程时长:{}\n\t课程价格{}".format(c, course_info[c].get("hour"), course_info[c].get("price")))
    return True


if __name__ == '__main__':
    examine_select_course()


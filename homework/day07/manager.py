#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       manager
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-20
#    Change Activity:  2019-05-20:

import re
from base import Base,Database,InfoMode
from wrapper import check_login_status

class Manager:

    def __init__(self):
        self.b = Base()
        self.db = Database()
        self.info = InfoMode()
        self.user_file = "user_info.json"


    def __all_class(self, type, stu_name=None):
        user_info = self.db.db_select("user_info.json")
        class_info = self.db.db_select("class_info.json")
        class_name_list = []
        if type == "stu":
            for c in class_info:
                if class_info[c].get("course") in user_info[stu_name].get("course") and len(class_info[c].get("student")) < 30:
                    class_name_list.append(c)

            print("班级列表".center(6,'#'))
            print("{}".format('|'.join(class_name_list)))
            print("班级列表".center(6,'#'))

            return class_name_list
        elif type == "teacher":
            for c in class_info:
                class_name_list.append(c)

            print("班级列表".center(6,'#'))
            print("{}".format('|'.join(class_name_list)))
            print("班级列表".center(6,'#'))
            return class_name_list




    def create_account(self, type):
        """

        :param type:
        :return:
        """
        user_info = self.db.db_select("user_info.json")
        while True:
            name = self.b.name()
            if name in user_info:
                print("该成员已经存在")
                continue
            else:
                age = self.b.age()
                password = self.b.password()
                if type == "stu":

                # 将数据写入字典
                    user_info[name] = self.info.write_info_to_dict(type="stu",
                                                                    password=password,
                                                                    age=age
                                                                    )

                    self.db.db_insert("user_info.json", user_info)
                    print("添加学生{}成功".format(name))
                    return True
                elif type == "teacher":
                    position = self.b.position()

                    # 将数据写入字典
                    user_info[name] = self.info.write_info_to_dict(type="staff",
                                                                    age=age,
                                                                    password=password,
                                                                    position=position,
                                                                    mold="teacher"
                                                                    )
                    self.db.db_insert("user_info.json", user_info)
                    print("添加{}讲师成功".format(name))
                    return True

    def create_course(self):
        """
        为了写的简单点，没有加入课程大纲，但是模板字典已经设置了这个选选项
        :return:
        """
        course_info = self.db.db_select("course_info.json")
        price_rgx = re.compile(r"\d{1,5}$")
        hour_rgx = re.compile(r"\d{1,2}$")

        while True:
            course_name = input("请输入课程名称")
            if course_name in course_info:
                print("该课程已经存在，请重新输入：")
                continue
            else:
                while True:
                    course_price = input("请输入课程价格：")
                    if price_rgx.match(course_price):
                        while True:
                            course_hour = input("请输入课程时长：")
                            if hour_rgx.match(course_hour):

                                #组合信息字典
                                course_info[course_name] = self.info.write_info_to_dict(type="course",
                                                                                        price=course_price,
                                                                                        hour=course_hour,
                                                                                        outline=[])
                                # 将信息写入数据库
                                self.db.db_insert("course_info.json", course_info)
                                print("\t\t\t{}课程信息已经创建".format(course_name))
                                return True
                            else:
                                print("您输入的课程时长不合理，时长必须是2位以内数字")
                                continue
                    else:
                        print("您输入的价格不合理，价格必须是5位以内数字")
                        continue
    def create_class(self):
        """
        创建班级
        :return:
        """
        class_info = self.db.db_select("class_info.json")
        course_info = self.db.db_select("course_info.json")

        while True:
            class_name = input("请输入班级名称")
            if class_name in class_info:
                print("该班级已经存在，请重新输入")
                continue
            else:
                course_name_list = []
                for c in course_info:
                    course_name_list.append(c)
                print("课程列表：{}".format("||".join(course_name_list)))
                print("\n")
                print("###" * 10)
                while True:
                    course_name = input("请输入课程名称：")
                    if course_name in course_info:
                        class_info[class_name] = self.info.write_info_to_dict(type="class",
                                                                              course=course_name)
                        self.db.db_insert("class_info.json", class_info)
                        print("创建{}班级成功，课程名称为：{}".format(class_name, course_name))
                        return True
                    else:
                        print("您输入的课程名称有误，请重新输入：")
                        continue

    def examine_all_course(self):
        """
        查看所有课程
        :return:
        """
        course_info = self.db.db_select("course_info.json")
        for name in course_info:
            print("课程名称：{};\t课程价格：{};\t课程周期：{}天".format(name,
                                                              course_info[name]["price"],
                                                              course_info[name]["hour"]))
    def examine_all_student(self):
        """
        查看所有学生信息
        :return:
        """
        user_info = self.db.db_select("user_info.json")
        for name in user_info:
            if user_info[name].get("mold") == "stu":
                print("学生姓名：{};\t学生年龄:{};学生班级：{}".format(name,
                                                         user_info[name].get("age"),
                                                         '|'.join(user_info[name].get("class"))))

    def examine_all_student_course(self):
        """
        查看所有学生选课情况
        :return:
        """
        student_info = self.db.db_select("user_info.json")
        if len(student_info) > 1:
            for user in student_info:
                if student_info[user].get("mold") == "stu":
                    if len(student_info[user].get("course")) > 0:
                        print("学生姓名:{};\t学生课程:{}".format(user, '|'.join(student_info[user].get("course"))))
                    else:
                        print("{}同学没有课程".format(user))
        else:
            print("没有学生报名,请添加学生")
    def allot_class(self, type):
        user_info = self.db.db_select("user_info.json")
        class_info = self.db.db_select("class_info.json")
        course_info = self.db.db_select("course_info.json")

        # 判断是学生还是老师
        while True:



            if type == "stu":
                stu_name_list = []
                for n in user_info:
                    if user_info[n].get("mold") == "stu":
                        stu_name_list.append(n)
                print("学生列表".center(20, '#'))
                print("{}".format('|'.join(stu_name_list)))
                print("学生列表".center(20, '#'))

                stu_name = self.b.name()

                # 输入学生姓名，打印学生可以选择的班级列表
                self.__all_class(type, stu_name)

                #输入班级信息
                class_name = self.b.allot_class_name()
                if stu_name in user_info and class_name in class_info and user_info[stu_name].get("mold") == type:

                    # 组合学生信息
                    user_info[stu_name]["class"].append(class_name)
                    class_info[class_name]["student"].append(stu_name)

                    #将信息写入数据库
                    self.db.db_insert("user_info.json", user_info)
                    self.db.db_insert("class_info.json", class_info)
                    print("{}学生分配的班级为{}".format(stu_name, class_name))
                    return True
                else:
                    print("输入的信息有误{}学生或{}课程未录入信息数据库".format(stu_name, class_name))
                    continue

            elif type == "teacher":
                self.__all_class(type)
                teacher_name_list = []
                for n in user_info:
                    if user_info[n].get("mold") == "teacher":
                        teacher_name_list.append(n)

                print("老师列表".center(20, '#'))
                print("{}".format('|'.join(teacher_name_list)))
                print("老师列表".center(20, '#'))

                teacher_name = self.b.name()
                class_name = self.b.allot_class_name()
                if teacher_name in user_info and class_name in class_info and user_info[teacher_name].get("mold") == "teacher":

                    # 组合老师信息
                    user_info[teacher_name]["class"].append(class_name)
                    class_info[class_name]["teacher"].append(teacher_name)

                    # 将信息写入数据库
                    self.db.db_insert("user_info.json", user_info)
                    self.db.db_insert("class_info.json", class_info)
                    print("{}老师分配的班级为{}".format(teacher_name, class_name))
                    return True
                else:
                    print("输入的信息有误{}学生或{}课程未录入信息数据库".format(teacher_name, class_name))
                    continue
            else:
                print("请指定正确的类型")
                continue



if __name__ == '__main__':
    m = Manager()
    print(m.create_account("teacher"))
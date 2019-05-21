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

    @check_login_status
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

    @check_login_status
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

                                return True
                            else:
                                print("您输入的课程时长不合理，时长必须是2位以内数字")
                                continue
                    else:
                        print("您输入的价格不合理，价格必须是5位以内数字")
                        continue



if __name__ == '__main__':
    m = Manager()
    print(m.create_course())
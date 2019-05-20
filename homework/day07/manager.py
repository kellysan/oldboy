#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       manager
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-20
#    Change Activity:  2019-05-20:


from base import Base,Database,InfoMode

class Manager:

    def __init__(self):
        self.b = Base()
        self.db = Database()
        self.info = InfoMode()
        self.user_file = "user_info.json"


    def create_account(self, type):
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

    def create_teacher_account(self):
        teacher_info = self.db.db_select("user_info.json")
        while True:
            name = self.b.name()
            if name in teacher_info:
                print("该成员已经存在")
                continue
            else:
                age = self.b.age()
                password = self.b.password()



if __name__ == '__main__':
    m = Manager()
    print(m.create_account("stu"))
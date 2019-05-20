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

    def create_student_account(self):
        name = self.b.name()
        age = self.b.

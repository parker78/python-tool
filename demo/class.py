#!/usr/bin/env python
#coding:utf8
class Bird(object):
    # class properties
    have_feather=True
    way_of_reproduction='egg'
#    dx=0
#    dy=0
# init方法相当于构造函数，初始化对象。
    def __init__(self):
        # object properties
        self.dx=0
        self.dy=0
    def move(self,dx,dy):
        self.dx=self.dx+dx
        self.dy=self.dy+dy
        return [self.dx,self.dy]
pretty=Bird()
print pretty.have_feather
print pretty.way_of_reproduction
print pretty.move(1,2),pretty.move(2,3)
park=Bird()
print park.move(3,3)

class Chicken(Bird):
    way_of_move='walk'
    possible_in_KFC=True
class Oriole(Bird):
    way_of_move='fly'
    possible_in_KFC=False
summer=Chicken()
print summer.have_feather
print summer.move(3,3)
print Bird.have_feather

# dir方法，查看对象的所有属性
# help查看相关所名文档

# list

class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
        print("My name is %s , My age is %d" % (self.name,self.age))

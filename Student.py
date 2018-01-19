class Student(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def say(self):
        print("My name is %s , My age is %d" % (self._name,self._age))

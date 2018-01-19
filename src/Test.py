from collections import Iterable
from collections import Iterator
from src.MyMethod import sum
from src.Student import Student
def d(n):
    return n%2==1
r=filter(d,[1,2,3,4,5,6,7,8,9])
for x in r:
    print(x)

s=sorted(["wang","xin","liu","jiang","tao"],key=str.lower)
print(s)

r=sum(1,23,3)
print(r())

name=sum.__name__
print(name)

s = Student("王鑫",18)
s.say();
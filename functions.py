#function without parameters
def a():
    print("a")
print(a())

#positional parameters
def b(a,b):
    return a+b
print(b(2,3))

#default parametrs
def c(a=2,b=3):
    return a-b
print(c(3,2))

#keyword parameters
def d(a,b):
    return a*b
print(d(b=5,a=1))

#*args variable positional arguments args-tuple
def e(*args):
    print(args)
e(1,2,3,4,5)

#**kwargs variable keyword arguments
def f(**kwargs):
    print(kwargs)
    for key , val in kwargs.items():
        print(key,val)
f(name=1,age=10,dno=12)


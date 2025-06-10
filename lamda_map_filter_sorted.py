#single value
l=lambda x:x*2
print(l(3))

#multiple values
m = lambda x , y : x+y
print(m(3,5))

#map
def fun(x):
    return x**2
a=[1,2,3,4,5]
n = list(map(fun,a))
print(n)


#map with lambda
o = list(map(lambda x:x**2 ,a))
print(o)

#filter
def even(x):
    return x%2==0
a=[1,2,3,4,5]
b = list(filter(even,a))
print(b)

#filter with lambda
a=[1,2,3,4,5]
b = list(filter(lambda x : x%2==0,a))
print(b)

#sorted
a=[2,3,4,1,6]
b = sorted(a)
print(list(b))

#reverse in sorted
d = sorted(a,reverse = True)
print(list(d))

#str len sorted
e = ["a","ab","abc"]
c = sorted(e,key=len)
print(list(c))

#pairs sorted
f = [(1,2),(3,4),(5,6)]
g = sorted(f,key= lambda x :x[0])
print(list(g))

#dict sorted 
h = [{"name":'a',"age":30},{"name":'b',"age":39},{"name":'c',"age":20},]
i = sorted(h,key=lambda x:x["age"])
print(list(i))

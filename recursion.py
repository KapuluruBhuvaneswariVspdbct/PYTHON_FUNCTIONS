#factorial
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
print(fact(5))

#fibonnaci
def fib(n):
    if n <=0 :
        return 0
    if n == 1 :
        return 1
    return fib(n-1)+fib(n-2)
print(fib(-1))

#sum of n natural
def sumo(n):
    if n == 1 :
        return 1
    return n+sumo(n-1)
print(sumo(3))

#print 1 to n 
def p(n):
    if n <1:
        return 
    p(n-1)
    print(n, end = ",")
p(3)
print()

#print n to 1
def p(n):
    if n <1:
        return 
    print(n, end = ",")
    p(n-1)
p(3)
print()

#sum of n natural nums
def p(n):
    if n <1:
        return 0
    return n+p(n-1)
print(p(3))


#rev a str
def p(s):
    if len(s)== 0:
        return ""
    return p(s[1:])+s[0]
print(p("abc"))

#str palindrome 
def p(s):
    if len(s)==0:
        return True
    if s[0]!=s[-1]:
        return False
    return p(s[1:-1])
print(p("abcba"))

#count dig of num
def p(n):
    if n == 0:
        return 0
    return 1+p(n//10)
print(p(222))

#sum of digs of num
def p(n):
    if n == 0:
        return 0
    return n%10 +p(n//10)
print(p(222))

#pow
def p(m,n):
    if n == 0 :
        return 1
    return m*p(m,n-1)
print(p(3,3))

#prod of array elements
def prod(a):
    if len(a)==0:
        return 1
    return a[0]*prod(a[1:])
print(prod([1,2,3,4,5]))

def prod(a,n):
    if n==0:
        return 1
    return a[n-1]*prod(a,n-1)
print(prod([1,2,3,4,5],5))

#array sorted or not 
def sor(a,n):
    if n<=1:
        return True
    if a[n-1]<a[n-2]:
        return False
    return sor(a,n-1)
print(sor([1,2,3],3))

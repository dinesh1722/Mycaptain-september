"""first n number of fibonacci numbers"""

n=int(input("enter n value:"))  
a=0
b=1
print(a)
for i in range(n-1):
    c=a+b
    a=b
    b=c
    print(a)

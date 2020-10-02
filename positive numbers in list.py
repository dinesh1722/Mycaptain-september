a=input("enter a series of numbers separated by space:")
b=a.split()
c=[]
for i in b:
    if int(i)>=0:
        print(i,end=" ")
        c.append(int(i))
print("\n")
print(c)
        
        

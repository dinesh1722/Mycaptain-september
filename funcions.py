def most_frequent(string):
    d=dict()
    for i in string:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    a=[(v,k) for (k,v) in d.items()]
    a.sort(reverse=True)
    b=[(k,v) for (v,k) in a]
    for i in b:
        print('{:<5s}'.format(i[0]) , '{:<5}'.format(i[1]))
    
    
s=str(input("please enter a string:"))
print(most_frequent(s))
 

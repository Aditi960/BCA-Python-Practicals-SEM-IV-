# Python code for Slip 15, Question 2
s=int(input("enter no :- "))
a,b=1,2
for x in range(s):
    print(a,end=",")
    a,b=b,a+b
    

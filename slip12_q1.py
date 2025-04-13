# Python code for Slip 12, Question 1

a,b=0,1
n=int(input("enter range n:- \n"))

for x in range(n):
    print(a,end=",")
    a,b=b,a+b
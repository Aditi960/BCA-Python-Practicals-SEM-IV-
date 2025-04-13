# Python code for Slip 13, Question 2
n=int(input("enter n:- "))
print(f"\nprime no b/w 2 to {n} are:- \n")

for i in range(2,n):
    if n%i==0:
        print(i)

# Python code for Slip 13, Question 1
def display(tup):
    print("the max no is ",max(tup))
    print("the min no is ",min(tup))
    print("the max no is ",sum(tup))
n=int(input("enter n"))
t=()
print("enter tuple members")
for x in range (n):
    num=int(input())
    t+=(num,)

display(t)




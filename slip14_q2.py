# Python code for Slip 14, Question 2

no=int(input("enter a number"))
total=0
while no>0:
    total+=no%10
    no=no//10

print(f"sum of digit of {no} is = {total}")

# Python code for Slip 10, Question 1

n=int(input("enter a number"))
rev=0
print("the number is :- ",n)
while n !=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10

print("number afte reversing is :- ",rev)

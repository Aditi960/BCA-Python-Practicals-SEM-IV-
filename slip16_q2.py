# Python code for Slip 16, Question 2

n=int(input("enter a no"))
print("prime no are")
for num in range(2,n+1):
    for i in range(2,num):
        if n%i==0:
            print(i)


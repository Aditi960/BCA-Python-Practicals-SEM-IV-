# Python code for Slip 14, Question 1
def is_palindrome(st):
    result=st[::-1]
    if result==st:
        return True
    else:
        False

str=input("enter a string:- ")
check=is_palindrome(str)
if check==True:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")


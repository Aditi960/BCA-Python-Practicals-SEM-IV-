# Python code for Slip 11, Question 2
def remove(s):
    return s[::2]

text=input("Enter string:- ")
print(f"\n string before removing the character:- {text}")

result=remove(text)
print(f"\n string after removing the characters :- {result}")
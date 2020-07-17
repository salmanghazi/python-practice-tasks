
num=input("Please enter a string: \n")

LETTERS=sum(i.isdigit() for i in num)
print("LETTERS %d"%LETTERS)

ALPHABETS=sum(i.isalpha() for i in num)
print("LETTERS %d"%ALPHABETS)

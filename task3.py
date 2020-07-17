
def generate_squares(num):
    my_dict={}
    j=1
    for j in range(1,num+1):
      my_dict[j]=j*j

    return my_dict


print("Please enter any number: ")
num=input()

#logic to validate whether the number is positive or not
while True:
  if num.isdigit() and int(num)<=0:
    print("Enter a positive number")
    num=input()
  elif not num.isdigit():
    print("Enter a number")
    num=input()
  else:
    break

#printing the dictionary of squares
diction = generate_squares(int(num))
print(diction)
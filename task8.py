
#this fucntion will generate squares of odd numbers only
def generate_odd_squares(num):
    my_arr=[int(i)*int(i) for i in num if int(i)%2!=0] 
    return my_arr


print("Please enter a list of numbers: ")
array=input()
array=array.split(',')

#printing the dictionary of squares
diction = generate_odd_squares(array)
print(diction)

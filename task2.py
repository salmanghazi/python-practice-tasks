
my_list=[]
for num in range(1000,2001):
  if num%7==0 and num%5!=0: #Divisble by 7 but not multiple of 5
    my_list.append(num)

print("The numbers which are divisible by 7 but are not a multiple of 5, between 1000 and 2000 are: ")
print(my_list)
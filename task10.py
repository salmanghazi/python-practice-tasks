

class Person:

  def __init__(self):
    pass
  

class Male(Person):
   gender="Male"
   
   def getGender(self):
     print(self.gender)

class Female(Person):
   gender="Female"
   
   def getGender(self):
     print(self.gender)

  

# Test Function 
def main():
  obj1 = Male()
  obj1.getGender()

  obj2 = Female()
  obj2.getGender()

if __name__ == "__main__":
    main()
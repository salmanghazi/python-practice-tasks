

class myClass:

  def __init__(self, inp):
    self.inp=inp
  def getString(self):
    self.inp=input("Give input\n")
  def printString(self):
    print("\nThis is printString Function's output")
    print(self.inp)
  

# Test Function 
def main():
  obj = myClass("salman")
  obj.getString()
  obj.printString()

if __name__ == "__main__":
    main()
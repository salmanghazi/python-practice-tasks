
# Test Function 
def main():
  words = input("please give the list\n")
  words=words.split(',')
  # words=words.sort()
  words=sorted(list(words))
  print(', '.join(words))

  

if __name__ == "__main__":
    main()
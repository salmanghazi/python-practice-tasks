import re

# Test Function
def main():
    with open("names.txt") as f:
        names = f.readlines()

        # This block will subtrat end-line character from names
        new_names = []
        for name in names:
            name = re.sub(r"\n", "", name)
            new_names.append(name)
        names = new_names

        # This loop filters unique names from names list and counts them
        unique_name = list(set(names))
        for name in unique_name:
            print(f"The count of '{name}' is {new_names.count(name)}")


if __name__ == "__main__":
    main()

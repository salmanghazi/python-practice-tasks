import re

# Test Function
def main():
    my_list = [
        "example (.com)",
        "w3resource",
        "github (.com)",
        "stackoverflow (.com)",
    ]

    for obj in my_list:
        remaining_string = re.sub(
            r" ?\((.*?)\)", "", obj
        )  # it will substitute everything in brackets with empty string
        print(remaining_string)


if __name__ == "__main__":
    main()

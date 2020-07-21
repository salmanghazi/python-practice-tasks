import re

# Test Function
def main():
    password_list = [
        "ABd1234@1",
        "a F1#",
        "2w3E*",
        "2We3345",
        "########02.2aaA",
        "@9zA",
    ]

    pattern = re.compile(
        r"(?=[\S\s]{6,12}$)(?=.*[A-Z])+(?=.*[a-z])+(?=.*[0-9])+(?=.*[$#@])+.*"
    )
    passwords = []  # List to store only valid password

    for password in password_list:
        matches = pattern.finditer(
            password
        )  # Check againt every given password
        for match in matches:
            passwords.append(match.group())

    print(", ".join(passwords))


if __name__ == "__main__":
    main()

import re

# Test Function
def main():
    # This program will filter out all urls given a string

    string = """My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles
     in the portal of http://www.geeksforgeeks.org as the https://www.facebook.com"""

    patterns = re.compile(r"https?://(\w+\.)?[(\w+)(\.w+)]+[/|%\w+]+")
    matches = patterns.finditer(string)
    for match in matches:
        print(match.group())


if __name__ == "__main__":
    main()

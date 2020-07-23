import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.nytimes.com/")

if req.status_code == 200:  # successfully hit
    soup = BeautifulSoup(req.text, "html.parser")

    # Following class points to the articles
    article_raw = soup.find_all("h2", {"class": "css-z9cw67 e1voiwgp0"})
    article_titles = []
    count = 1

    print("Following are the titles: \n")
    for article in article_raw:
        article_titles.append(article.text)
        print(f"Article No. {count}: '{article.text}'")
        count += 1
    
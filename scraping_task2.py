import requests
from bs4 import BeautifulSoup


def extract_image_links(raw_img_links):
    """ This function will extract all image links

        from a given raw image link which is authentic 
    
        and has 200 status code """

    extracted_image_links = []
    for im in raw_img_links:
        extracted_image_links.append(im.get("src"))
    return extracted_image_links


def main():
    req = requests.get("http://recurship.com/")
    if req.status_code == 200:  # successfully hit
        soup = BeautifulSoup(req.text, "html.parser")
        links = []
        for link in soup.find_all("a"):
            count += 1
            links.append(link.get("href"))  # Extract all links

        links = list(set(links))  # Removing duplicate links
        my_dict = {}
        for link in links:
            try:
                req = requests.get(link)
                if req.status_code == 200:

                    soup = BeautifulSoup(req.text, "html.parser")
                    title = soup.title.string

                    img_links = soup.find_all("img")
                    updated_img_links = extract_image_links(img_links)
                    my_dict[title] = updated_img_links
            except:
                print("The link ''{}'' coudln't be opened".format(link))

        print(str(my_dict).replace(",", ",\n "))  # To Make output clear


if __name__ == "__main__":
    main()

import requests
from bs4 import BeautifulSoup

def extract_text(url):
    headers = {"User-Agent": "Mozilla/5.0"} # This was super helpful in avoiding basic anti-bot measures
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "Failed to retrieve page."

    soup = BeautifulSoup(response.text, "html.parser")

    # Removed unnecessary elements which are irrelevant to the voice feature
    for tag in ["script", "style", "header", "footer", "nav"]:
        for element in soup.find_all(tag):
            element.decompose()

    # Extract readable text
    text = " ".join([p.text for p in soup.find_all("p")])
    return text[:5000]  # Limited to 5000 characters for efficiency

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    print(extract_text(url))

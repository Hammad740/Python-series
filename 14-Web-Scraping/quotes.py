import bs4
import requests
import lxml

res = requests.get("https://quotes.toscrape.com/")

soup = bs4.BeautifulSoup(res.text, "lxml")

authors = soup.select('.author')
print(authors)

authors = set()
for name in soup.select(".author"):
    authors.add(name.text)
print(authors)

print("\n")

quotes = soup.select(".text")
print(quotes)

for quote in soup.select(".text"):
    print(quote.text)


for item in soup.select(".tag-item"):
    print(item.text)

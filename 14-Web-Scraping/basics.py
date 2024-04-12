import requests
import bs4


result = requests.get("http://www.example.com")

print(result.text)

soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup)

print(soup.select('title'))
print(soup.select('p'))

print(soup.select('h1')[0].getText())


res = requests.get(
    "https://en.wikipedia.org/wiki/Grace_Hopper")

soup = bs4.BeautifulSoup(res.text, 'lxml')

# print(soup.prettify())

m = soup.select(".mw-headline")
print(m)
print(m[0])
print(type(m[0]))
print("#########")
print(m[0].text)

for item in soup.select(".mw-headline"):
    print(item.text)

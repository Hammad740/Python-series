import requests
import lxml
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# print(base_url.format('30'))

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
soup.prettify()
products = soup.select(".product_pod")
print(products)
example = products[0]
str(example)
answer = 'star-rating Three' in str(example)
print(answer)
x = example.select(".star-rating.Three")
print(x)
y = example.select("a")
print(y)
print(y[1]['title'])  # ? consider it as a dictionary
print("################")


two_star_titles = []
for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select("a")[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)

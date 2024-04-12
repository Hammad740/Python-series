import bs4
import requests
import lxml

response = requests.get(
    'https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')


soup = bs4.BeautifulSoup(response.text, 'lxml')

img = soup.select('.mw-file-element')[0]
print(img)
print("#############")
img_link = img['src']
f = open('my_img.jgp', 'w')
f.write(img_link)
f.close()

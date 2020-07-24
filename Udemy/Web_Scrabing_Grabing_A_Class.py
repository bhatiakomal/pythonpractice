'''import requests
import bs4
res=requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup=bs4.BeautifulSoup(res.text, 'lxml')
#print(soup)
print(soup.select('.toctext'))
print(soup.select('.toctext')[0])
print(type(soup.select('.toctext')[0]))
for item in soup.select('.toctext'):
    print(item.text)'''

import requests
import bs4
res=requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup=bs4.BeautifulSoup(res.text, 'lxml')
print(soup)

print(soup.select('img'))
print(soup.select('.thumbimage')[0])
computer=(soup.select('.thumbimage')[0])
print(computer('src'))

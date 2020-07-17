import requests
import bs4
result=requests.get('https://example.com/')
print(type(result))
print(result.text)

soup=bs4.BeautifulSoup(result.text, 'lxml')
print(soup)

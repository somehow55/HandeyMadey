import requests
from bs4 import BeautifulSoup

url = 'https://www.pinterest.com/pin/395472411035058771/'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# print(soup);

# title = soup.select_one('meta[property="og:title"]')['content'];
img = soup.select_one('meta[property="og:image"]')['content'];
url = soup.select_one('meta[property="og:url"]')['content'];
# desc = soup.select_one('meta[property="og:description"]')['content'];
print(img, url);
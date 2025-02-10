import requests
import bs4
#import json
from fake_headers import Headers, windows

headers = Headers(browser= "yandex", os= 'windows').generate()
response = requests.get('https://habr.com/ru/articles/', headers=headers)
# with open('xabr.xml', encoding="utf-8") as f:
#     reader = f.read()
# xabr_text = reader

# with open('xabr.xml', 'w', encoding='utf-8') as file:
#      file.write(soup.prettify())

soup = bs4.BeautifulSoup(response.text, 'lxml')
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
articles = []
for article in soup.select('article'):
    title_tag = article.select_one('h2 a')
    date_tag = article.select_one('time')
    description_tag = article.select_one('div.article-formatted-body')

    if title_tag and date_tag and description_tag:
        title = title_tag.get_text(strip=True)
        link = "https://habr.com" + title_tag['href']
        date = date_tag['datetime']
        description = description_tag.get_text(strip=True).lower()

        if any(keyword in description for keyword in KEYWORDS):
            articles.append({"title": title, "link": link, "date": date})

for article in articles:
    print(f"{article['date']} - {article['title']} ({article['link']})")
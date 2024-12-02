from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_news = response.text

soup = BeautifulSoup(yc_news, "html.parser")

articles = soup.select(selector=".title .titleline a")

texts = []
links = []
for article in articles:
    texts.append(article.getText())
    links.append(article.get(key="href"))

article_voute = [int(item.getText().split()[0]) for item in soup.find_all(name="span", class_="score")]
max_point = max(article_voute)
max_index = article_voute.index(max_point)

print(texts[max_index])
print(links[max_index])
print(max_point)

# with open("website.html") as html_file:
#     content = html_file.read()

# soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())
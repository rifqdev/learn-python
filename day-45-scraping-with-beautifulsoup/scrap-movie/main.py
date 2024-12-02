import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
movie_titles = [item.getText() for item in soup.find_all(name="h3", class_="title")]
movie_titles.reverse()
with open("movie_list.txt", mode="w") as data:
    for title in movie_titles:
        data.write(f"{title}\n")




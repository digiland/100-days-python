import requests
from bs4 import BeautifulSoup

r = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2//")
soup = BeautifulSoup(r.text, "html.parser")
titles = soup.find_all(name="h3", class_="title")
movies = [title.getText() for title in titles]
to_watch = movies[::-1]

with open("movies.txt", "w") as f:
    for movie in to_watch:
        f.write(movie + "\n")

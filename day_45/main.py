from urllib import response
from bs4 import BeautifulSoup


import requests

r = requests.get("https://news.ycombinator.com/news")

webpage = r.text

soup = BeautifulSoup(webpage, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]

# print(article_texts)
# print(article_links)

article_upvotes = [int(score.getText().split()[0])
                   for score in soup.find_all(name="span", class_="score")]
# print(article_upvotes)

max_upvotes = max(article_upvotes)
pos = article_upvotes.index(max_upvotes)

print(
    f"The article with the most upvotes is '{article_texts[pos]}', link: {article_links[pos]}: {max_upvotes} upvotes")


# with open('website.html') as f:
#     input = f.read()

# soup = BeautifulSoup(input, 'html.parser')

# links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))
#     print(link.getText())

# heading = soup.find('h1')

# company_url = soup.select_one(selector='a')

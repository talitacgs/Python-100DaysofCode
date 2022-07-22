from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

scores = soup.find_all(name="span", class_="score")
article_upvotes = [int(article_scores.getText().split()[0]) for article_scores in soup.find_all(name="span", class_="score")]

#Look for the article with largest number os votes

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

#print(article_texts)
#print(article_links)
#print(article_upvotes)


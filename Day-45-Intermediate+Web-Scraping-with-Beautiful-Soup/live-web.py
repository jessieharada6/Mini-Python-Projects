from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
# same as "view page source" in chrome
yc_web_page = response.text

# create coup
soup = BeautifulSoup(yc_web_page, "html.parser")
article_texts = []
article_links = []
article_upvotes = []

stories = soup.find_all(name="a", class_="storylink")
for story in stories:
    article_texts.append(story.getText())
    article_links.append(story.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts, article_links, article_upvotes)

largest_vote = max(article_upvotes)
largest_index = article_upvotes.index(largest_vote)
print(largest_vote, largest_index)

most_popular_article = article_texts[largest_index]
most_popular_link = article_links[largest_index]
print(most_popular_article, most_popular_link)
# max_index = 0
# max_vote = 0
# for i in range(len(article_upvotes)):
#     max_vote = max(max_vote, article_upvotes[i])
#     max_index = i


# https://news.ycombinator.com/robots.txt
# use <rootBaseUrl>/robots.txt to check for disallow on the ones they don't want you to scrape
# and crawl-delay is suggested delay per scrape

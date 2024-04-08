from bs4 import BeautifulSoup
from textblob import TextBlob
from newspaper import Article
import requests, nltk
from nltk import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

response = requests.get("https://timesofindia.indiatimes.com/india")
india_web_page = response.text
soup = BeautifulSoup(india_web_page, 'html.parser')

article_links = []
for article_tag in soup.find_all('a', href=True):
    link = article_tag['href']
    # Check if the link starts with "https://timesofindia.indiatimes.com/" and contains "articleshow"
    if link.startswith("https://timesofindia.indiatimes.com/") and "articleshow" in link:
        article_links.append(link)

print("Article links with format 'https://timesofindia.indiatimes.com/.......articleshow.....':")
for link in article_links:
    print(link)

article=Article(article_links[1])
article.download()
article.parse()
article.nlp()
text=article.text
summary=article.summary
print(type(text))
words = word_tokenize(text)
pos_tags=pos_tag(words)
named_entities=ne_chunk(pos_tags)
for entity in named_entities:
    if hasattr(entity, 'label'):
        print(entity.label(), ' '.join(c[0] for c in entity.leaves()))
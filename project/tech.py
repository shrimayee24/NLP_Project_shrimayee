from bs4 import BeautifulSoup
from textblob import TextBlob
from newspaper import Config, Article, Source
import requests, nltk
from nltk import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk


config = Config()
config.MAX_SUMMARY=400
config.memoize_articles = False

response = requests.get("https://timesofindia.indiatimes.com/technology")
india_web_page = response.text
soup = BeautifulSoup(india_web_page, 'html.parser')
article_links = []
article_text=[]
article_summary=[]
article_titles=[]

for article_tag in soup.find_all('a', href=True):
    link = article_tag['href']
    # Check if the link starts with "https://timesofindia.indiatimes.com/" and contains "articleshow"
    if link.startswith("https://timesofindia.indiatimes.com/") and "articleshow" in link:
        article_links.append(link)
        article=Article(link)
        article.download()
        article.parse()
        article.nlp()
        text=article.text
        article_text.append(text)
        article_titles.append(article.title)
        article_summary.append(article.summary)



print("Title: \n",article_titles[10],"\n")

print("Link: \n",article_links[10],"\n")

print("Text:\n",article_text[10],"\n")

print("Summary: \n",article_summary[10],"\n")


print("\n total articles: ", len(article_summary))
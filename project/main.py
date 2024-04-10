from bs4 import BeautifulSoup
from textblob import TextBlob
from newspaper import Config, Article, Source
import requests, nltk
from nltk import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from gensum import text_summarizer
import os.path
import csv

config = Config()
config.MAX_SUMMARY=400
config.memoize_articles = False

response = requests.get("https://timesofindia.indiatimes.com/india")
india_web_page = response.text
soup = BeautifulSoup(india_web_page, 'html.parser')
article_links = []
article_text=[]
article_summary=[]
article_titles=[]
article_img=[]
total=0
for article_tag in soup.find_all('a', href=True):
    link = article_tag['href']
    # Check if the link starts with "https://timesofindia.indiatimes.com/" and contains "articleshow"
    if link.startswith("https://timesofindia.indiatimes.com/") and "articleshow" in link:
        
        article = Article(link)
        article.download()
        article.parse()
        article.nlp()
        text = article.text
        summary=text_summarizer(text)

        
        # Find all img tags in the article content
        img_tags = BeautifulSoup(article.html, 'html.parser').find_all('img')
        img_src = None
        for img_tag in img_tags:
            src = img_tag.get('src', '')
            alt = img_tag.get('alt', '')
            fetchpriority = img_tag.get('fetchpriority', '')
            # Check if the img src contains "static.toiimg.", alt attribute is not "TOI logo", and fetchpriority is "high"
            if "static.toiimg." in src and alt != "TOI logo" and fetchpriority == "high":
                img_src = src
                break  # Stop searching after finding the first matching img src


        # Check if all fields are valid and not null
        if all(field is not None and isinstance(field, str) and field.strip() for field in [article.title, link, text, summary, img_src]):
            article_img.append(img_src)
            article_links.append(link)
            article_text.append(text)
            article_titles.append(article.title)
            article_summary.append(summary)
            total += 1
            print(total)


    if(total>=50):
        break;        

print("Title: \n", article_titles[1], "\n")
print("Link: \n", article_links[1], "\n")
print("Text:\n", article_text[1], "\n")
print("Summary: \n", article_summary[1], "\n")
print("Image: \n", article_img[1], "\n")
print("\nTotal articles: ", len(article_summary))

#define csv file path
csv_file = "C:\\Users\\AKANKSHA KALE\\Desktop\\NLP_Project\\project\\india.csv"
file_path = "C:\\Users\\AKANKSHA KALE\\Desktop\\NLP_Project\\project\\india.csv"

# Check if the file exists
if os.path.exists(file_path):
    # Get the size of the file
    file_size = os.path.getsize(file_path)
    
    # Check if the file is empty (size is 0)
    if file_size == 0:
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Article Title', 'Article Link', 'Article Text', 'Article Summary', 'Article Image'])
            for i in range(len(article_titles)):
                writer.writerow([article_titles[i], article_links[i], article_text[i], article_summary[i], article_img[i]])
            print("Data has been saved to:", csv_file)


  


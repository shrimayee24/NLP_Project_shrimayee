
from bs4 import BeautifulSoup
import requests

response = requests.get("https://timesofindia.indiatimes.com/india")
india_web_page = response.text
soup = BeautifulSoup(india_web_page, 'html.parser')


article_links = []
for article_tag in soup.find_all('a'):
    article_links.append(article_tag)

print("Article links")
print(article_links)   
for link in article_links:
    print(link)   





# indiapage=requests.get("https://timesofindia.indiatimes.com/india")
# worldpage=requests.get("https://timesofindia.indiatimes.com/world")
# businesspage=requests.get("https://timesofindia.indiatimes.com/business")
# technologypage=requests.get("https://timesofindia.indiatimes.com/technology")
# cricketpage=requests.get("https://timesofindia.indiatimes.com/sports/cricket")
# sportspage=requests.get("https://timesofindia.indiatimes.com/sports")
# dntertainmentpage=requests.get("https://timesofindia.indiatimes.com/etimes")
# autopage=requests.get("https://timesofindia.indiatimes.com/auto")
# tvpage=requests.get("https://timesofindia.indiatimes.com/tv/hindi")
# webseriespage=requests.get("https://timesofindia.indiatimes.com/tv/hindi")
# liftstylepage=requests.get("https://timesofindia.indiatimes.com/life-style")
# educationpage=requests.get("https://timesofindia.indiatimes.com/education")

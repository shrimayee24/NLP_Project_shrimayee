import pandas as pd
from bs4 import BeautifulSoup
from newspaper import Article
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

# Load existing BoW CSV files
india_bow_df = pd.read_csv("india_bow.csv")
world_bow_df = pd.read_csv("world_bow.csv")
business_bow_df = pd.read_csv("business_bow.csv")
tech_bow_df = pd.read_csv("tech_bow.csv")
sports_bow_df = pd.read_csv("sports_bow.csv")

# Function to preprocess text
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

# Function to update BoW dictionary from text
def update_bow(text, bow_df):
    preprocessed_text = preprocess_text(text)
    vectorizer = CountVectorizer(vocabulary=bow_df['Word'])
    bag_of_words = vectorizer.fit_transform([preprocessed_text])
    feature_names = vectorizer.get_feature_names_out()
    for i, word in enumerate(feature_names):
        index = bow_df.index[bow_df['Word'] == word].tolist()[0]
        bow_df.at[index, 'Frequency'] += bag_of_words[:, i].sum()

# Scrape new articles and update BoW CSV files
def update_bow_csv_from_articles(url, domain_name, bow_df):
    response = requests.get(url)
    india_web_page = response.text
    soup = BeautifulSoup(india_web_page, 'html.parser')

    for article_tag in soup.find_all('a', href=True):
        link = article_tag['href']
        try:
            if (link.startswith("https://timesofindia.indiatimes.com/") and "articleshow" in link and domain_name in link and "etimes" not in link and "auto" not in link and "tv" not in link and "tv/hindi" not in link and "web-series" not in link and "life-style" not in link and "/education" not in link):
                article = Article(link)
                article.download()
                article.parse()
                article.nlp()
                text = article.text
                update_bow(text, bow_df)
                print(f"Updated BoW with words from {link}")
        except Exception as e:
            print(f"Error downloading article from {link}: {e}")
            continue

# Update BoW for each domain
update_bow_csv_from_articles("https://timesofindia.indiatimes.com/india", "india", india_bow_df)
update_bow_csv_from_articles("https://timesofindia.indiatimes.com/world", "world", world_bow_df)
update_bow_csv_from_articles("https://timesofindia.indiatimes.com/business", "business", business_bow_df)
update_bow_csv_from_articles("https://timesofindia.indiatimes.com/technology", "technology", tech_bow_df)
update_bow_csv_from_articles("https://timesofindia.indiatimes.com/sports", "sports", sports_bow_df)

# Save updated BoW CSV files
india_bow_df.to_csv("india_bow.csv", index=False)
world_bow_df.to_csv("world_bow.csv", index=False)
business_bow_df.to_csv("business_bow.csv", index=False)
tech_bow_df.to_csv("tech_bow.csv", index=False)
sports_bow_df.to_csv("sports_bow.csv", index=False)

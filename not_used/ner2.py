import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import defaultdict

# Sample news articles
news_articles = [
    "The government announced new policies aimed at reducing carbon emissions.",
    "The football team secured a victory in the championship, thrilling fans nationwide.",
    "A new breakthrough in computer technology revolutionizes the industry.",
]

# Define categories and corresponding keywords
categories = {
    "Politics": ["government", "policies"],
    "Sports": ["football", "victory"],
    "Technology": ["technology", "computer"],
    # Add more categories and keywords as needed
}

# Function to perform NER and categorize articles
def categorize_article(article):
    # Tokenize the article
    words = word_tokenize(article)
    
    # Perform part-of-speech tagging
    tagged_words = pos_tag(words)
    
    # Initialize category scores
    category_scores = defaultdict(int)
    
    # Iterate through tagged words to find named entities and match with categories
    for word, tag in tagged_words:
        if tag == 'NNP':  # Proper noun (potential named entity)
            for category, keywords in categories.items():
                if any(keyword in word.lower() for keyword in keywords):
                    category_scores[category] += 1
    
    # Determine the category with the highest score
    max_category = max(category_scores, key=category_scores.get)
    
    return max_category

# Categorize each news article
for idx, article in enumerate(news_articles, start=1):
    category = categorize_article(article)
    print(f"Article {idx} Category:", category)
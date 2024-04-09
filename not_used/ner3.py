import spacy

# Load a pre-trained English model for named entity recognition
nlp = spacy.load("en_core_web_sm")

def categorize_article(text):
    doc = nlp(text)
    entities = set([ent.text.lower() for ent in doc.ents if ent.label_ in ["PERSON", "ORG"]])

    if not entities:
        return "Other"  # If no entities are found, categorize as "Other"

    return ", ".join(entities)  # Concatenate identified entities as category

def display_topics(categories):
    print("Select topics of interest:")
    for category in categories:
        print(category)

# Example news articles
news_articles = [
    "Virat Kohli breaks new record in cricket, leading the team to victory.",
    "Apple unveils new iPhone with advanced technology features.",
    "Jennifer Lawrence stars in the upcoming movie 'Red Sparrow'."
]

# Categorize each article
categories = set()
for article in news_articles:
    category = categorize_article(article)
    categories.add(category)

# Display identified categories
display_topics(categories)
selected_topics = input("Enter topics of interest (comma-separated): ").split(",")
print("Selected Topics:", selected_topics)
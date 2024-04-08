import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

# Sample news article
article = """
NEW DELHI: Actor-turned-politician Kangana Ranaut dismissed rumors that ‘she eats beef’, asserting her adherence to a vegetarian lifestyle, rooted in her identity as a ‘proud Hindu’.
Refuting claims suggesting her consumption of beef, Ranaut said in a post on X, "I don't consume beef or any other kind of red meat, it is shameful that completely baseless rumours are being spread about me, I have been advocating and promoting yogic and Ayurvedic way of life for decades now such tactics won't work to tarnish my image.The clarification from her follows online speculation allegi ..
"""

# Tokenize the article into words
words = word_tokenize(article)

# Perform part-of-speech tagging
pos_tags = pos_tag(words)

# Perform named entity recognition
named_entities = ne_chunk(pos_tags)

# Print the named entities found in the article
for entity in named_entities:
    if hasattr(entity, 'label'):
        print(entity.label(), ' '.join(c[0] for c in entity.leaves()))
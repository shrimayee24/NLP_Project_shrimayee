import streamlit as st
import pandas as pd
from gtts import gTTS
import os

st.set_page_config(layout="wide")
# Read the CSV file
csv_file = "C:\\Users\\AKANKSHA KALE\\Desktop\\NLP_Project\\project\\india.csv"
df = pd.read_csv(csv_file)

# Dropdown menu for category selection
selected_category = st.selectbox('Select Category', ['India', 'Politics', 'Business', 'Technology', 'Sports'])

# Display containers for each news article
st.write("## News Articles:")
for i in range(min(50, len(df))):
    article_title = df.iloc[i]['Article Title']
    article_summary = df.iloc[i]['Article Summary']
    article_link = df.iloc[i]['Article Link']
    article_image = df.iloc[i]['Article Image']
    
    # Check if all required fields are not empty and valid
    if all(isinstance(field, str) and field.strip() for field in [article_title, article_summary, article_link, article_image]):
        # Display article container
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write("")
            st.write("")
            st.image(article_image, width=250)  # Display article image on the left side with specified height and width
            # Display "Read Full Article" button
            st.write(f"[Read Full Article]({article_link})")
        with col2:
            st.write(f"### {article_title}")
            st.write(article_summary)
            
            # Display "Convert to Audio" button
            convert_button_key = f"convert_button_{i}"
            if st.button("Convert to Audio", key=convert_button_key):
                # Convert summarized text to audio
                audio_filename = f"{article_title}_summary_audio.mp3"
                tts = gTTS(article_summary, lang='en-uk')
                tts.save(audio_filename)
                st.audio(audio_filename, format='audio/mp3')

                # Remove audio file after playing
                if os.path.exists(audio_filename):
                    os.remove(audio_filename)
                    print("Audio file deleted")
            st.write("")
            st.write("")        
    else:
        print("One or more required fields are empty or invalid. Skipping article display.")

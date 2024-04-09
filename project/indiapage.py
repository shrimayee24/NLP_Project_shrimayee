import streamlit as st
import pandas as pd
from gtts import gTTS
import os

# Read the CSV file
csv_file = "C:\\Users\\AKANKSHA KALE\\Desktop\\NLP_Project\\project\\india.csv"
df = pd.read_csv(csv_file)

# Display containers for each news article
st.write("## News Articles:")
for i in range(min(50, len(df))):
    article_title = df.iloc[i]['Article Title']
    article_summary = df.iloc[i]['Article Summary']
    article_link = df.iloc[i]['Article Link']
    
    # Display article container
    st.write(f"### {article_title}")
    st.write(article_summary)
    
    # Display "Read the entire article" button at bottom right corner
    st.write(f"Read the full article [here]({article_link})")
    
    # Display "Convert to Audio" button at bottom right corner
    convert_button_key = f"convert_button_{i}"
    if st.button(f"Convert to Audio", key=convert_button_key):
        # Convert summarized text to audio
        audio_filename = f"{article_title}_summary_audio.mp3"
        tts = gTTS(article_summary, lang='en')
        tts.save(audio_filename)
        st.audio(audio_filename, format='audio/mp3')

        # Remove audio file after playing
        if os.path.exists(audio_filename):
            os.remove(audio_filename)
            print("Audio file deleted")

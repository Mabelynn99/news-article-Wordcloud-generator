import streamlit as st
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string

# Set up the Streamlit interface
st.title("Wordcloud Generator")
url_input = st.text_input("Enter a URL:")
news_article_input = st.number_input("Enter the number of news articles:", 1, 10, 5)

# Create a button to generate the wordcloud
if st.button("Generate Wordcloud"):
    # Download stopwords corpus
    nltk.download('stopwords')

    # Send HTTP request and parse HTML content
    page = requests.get(url_input)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract article links
    links = []
    articles_containers = soup.find_all('div', class_='card-object__content')
    for article in articles_containers[:news_article_input]:
        a_tag = article.find('a', class_='h6__link list-object__heading-link')
        link = a_tag['href']
        if not link.startswith('http'):  # Check if link is relative
            link = "https://www.channelnewsasia.com/" + link  # Make it absolute
        links.append(link)

    # Extract text from each link
    article_texts = []
    for link in links:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        text_containers = soup.find_all('div', class_='content-wrapper')
        for text_container in text_containers:
            paragraphs = text_container.find('div', class_='text-long')
            if paragraphs is not None:  # Check if 'paragraphs' variable is not None before entering inner loop
                for paragraph in paragraphs:
                    article_texts.append(paragraph.text)

    # Preprocess the text
    all_text = []
    for text in article_texts:
        text = text.lower()
        text = "".join(cha for cha in text if cha not in string.punctuation)
        words = word_tokenize(text)
        stopwords_set = set(nltk.corpus.stopwords.words('english'))
        text = " ".join(word for word in words if word not in stopwords_set)
        all_text.append(text)

    # Concatenate the preprocessed text
    all_text = " ".join(all_text)

    # Create a wordcloud object
    wordcloud = WordCloud(width=800, height=800, stopwords=stopwords_set, background_color='white', min_font_size=10).generate(all_text)

    # Display the wordcloud
    plt.figure(figsize=(8, 8))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    st.pyplot(plt)
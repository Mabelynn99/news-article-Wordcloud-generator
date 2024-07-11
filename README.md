# News Article Wordcloud Generator

**Project Description**
This is a web-based application that scrapes news articles and uses natural language processing to generate a word cloud of the most frequent words.

**Getting Started**
To get started, follow these steps:

1. Create a new Conda environment and activate it:

conda create -n streamlit_env
conda activate streamlit_env

2. Install the required libraries:

pip install -r requirements.txt

3. Create a new Python file, e.g., app.py, and copy the code into it.

4. Run the app by executing streamlit run app.py in your terminal.

5. Open a web browser and navigate to http://localhost:8501 to view your app.

**Usage**
To use this app, follow these steps:
1. Enter the URL of a news article in the input box.
2. Click the "Generate Word Cloud" button.
3. The word cloud for the article will be displayed.

**Requirements**
To run the app, you need to have the following libraries installed:

- Streamlit
- requests
- wordcloud
- nltk
- matplotlib
You can install all the required libraries by running pip install -r requirements.txt.

**Features**
- Generates word clouds from news articles
- Allows user to input URL to view generated word cloud

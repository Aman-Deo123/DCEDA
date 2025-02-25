import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import re

# Streamlit App Title
st.title("📊 Smartify: Data Cleaning + EDA Chatbot with AI Assistance")

# File uploader widget (fix emoji issue)
uploaded_file = st.file_uploader("📂 Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📋 Raw Data Preview:")
    st.dataframe(df.head())

    # Data Cleaning
    st.subheader("🛠 Data Cleaning")

    # Fill missing values
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns

    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])

    # Remove duplicates
    df.drop_duplicates(inplace=True)
    st.write("✔ Missing values handled and duplicates removed.")

    # Exploratory Data Analysis (EDA)
    st.subheader("📊 Exploratory Data Analysis")

    # Summary Statistics
    st.write("### 📉 Summary Statistics")
    st.write(df.describe())

    # Correlation Matrix
    numeric_df = df.select_dtypes(include=[np.number])
    if not numeric_df.empty:
        st.write("### 🔗 Correlation Matrix")
        plt.figure(figsize=(8, 6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
        st.pyplot(plt)

# Chatbot Section
st.subheader("🤖 AI Chatbot")
user_input = st.text_input("Ask me anything:")

# Google Custom Search API Key & Search Engine ID
import streamlit as st
import requests

# Fetch API keys from Streamlit Secrets
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
SEARCH_ENGINE_ID = st.secrets["SEARCH_ENGINE_ID"]
 

def google_search(query):
    """Search Google using Custom Search API and return the first Wikipedia link or top result."""
    try:
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}"
        response = requests.get(url)
        data = response.json()

        if "items" not in data:
            return "❌ No results found."

        for item in data["items"]:
            if "wikipedia.org" in item["link"]:
                return item["link"]  # ✅ Return the first Wikipedia link

        return data["items"][0]["link"]  # Return first result if no Wikipedia link

    except Exception as e:
        return f"❌ Error: {str(e)}"

def get_wikipedia_summary(wiki_url):
    """Fetch summary from Wikipedia page."""
    try:
        page_title = wiki_url.split("/")[-1].replace("_", " ")
        api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{page_title}"
        response = requests.get(api_url)
        data = response.json()

        if "extract" in data:
            return data["extract"]
        else:
            return "No summary available."

    except Exception as e:
        return f"❌ Error fetching Wikipedia summary: {str(e)}"

if user_input:
    search_result = google_search(user_input)
    
    if "wikipedia.org" in search_result:
        wiki_summary = get_wikipedia_summary(search_result)
        st.write(f"🔗 **Wikipedia Page:** [{search_result}]({search_result})")
        st.write(wiki_summary)
    else:
        st.write(f"🔎 **Google top result:** [{search_result}]({search_result})")

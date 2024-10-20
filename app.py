import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Title of the app
st.title("Data Cleaning and EDA Chatbot")

# File uploader widget
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Load the DataFrame from the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Print the available column names for debugging
    st.write("Available columns:", df.columns.tolist())

    # Data Cleaning
    st.header("Data Cleaning")
    st.write("### Handling Missing Values")
    missing_values = df.isnull().sum()
    st.write(missing_values)

    # Replace missing values with mean or median
    for col in df.columns:
        if df[col].dtype == np.number:
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

    # Remove duplicates
    st.write("### Removing Duplicates")
    duplicates = df.duplicated().sum()
    st.write(duplicates)
    df = df.drop_duplicates()

    # EDA
    st.header("Exploratory Data Analysis")
    st.write("### Summary Statistics")
    st.write(df.describe())

    # Histograms
    st.write("### Histograms")
    for col in df.columns:
        if df[col].dtype == np.number:
            plt.hist(df[col])
            plt.title(f'Histogram of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            st.pyplot(plt)

    # Correlation Matrix
    # Display data types for debugging
    st.write("Data Types:", df.dtypes)

    # Correlation Matrix
    st.write("### Correlation Matrix")
    try:
        # Convert all columns to numeric where possible
        df_numeric = df.apply(pd.to_numeric, errors='coerce')
    
        # Filter for numeric columns only
        numeric_df = df_numeric.select_dtypes(include=[np.number])
    
        if numeric_df.empty:
            st.write("No numeric columns available for correlation analysis.")
        else:
            corr_matrix = numeric_df.corr()
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
            st.pyplot(plt)
            plt.clf()  # Clear the figure for the next plot
    except Exception as e:
        st.write("An error occurred while calculating the correlation matrix:", e)

    # Box Plots
    st.write("### Box Plots")
    for col in df.columns:
        if df[col].dtype == np.number:
            plt.boxplot(df[col])
            plt.title(f'Box Plot of {col}')
            plt.xlabel(col)
            plt.ylabel('Value')
            st.pyplot(plt)

# Chatbot Section
st.header("Chatbot")
user_input = st.text_input("Type your message here:")
import random

if user_input:
    # Simple response logic with funky replies
    if "hello" in user_input.lower():
        responses = [
            "Hi pookie! 🌟", 
            "Hello there, superstar! ✨", 
            "Hey, you fabulous human! 😄"
        ]
        st.write(random.choice(responses))

    elif "help" in user_input.lower():
        responses = [
            "Help? I'm here to save the day! 🦸‍♂️", 
            "Need help? I'm your trusty sidekick! 🤖",
            "Just ask away, and I'll do my best to assist you! 💪"
        ]
        st.write(random.choice(responses))
    elif "data cleaning" in user_input.lower():
        responses = [
            "Data cleaning involves removing or correcting inaccurate records from a dataset. Need more info? 📊",
            "It's all about ensuring your data is accurate and usable! What else would you like to know? 🧹"
        ]
        st.write(random.choice(responses))
    elif "eda" in user_input.lower() or "exploratory data analysis" in user_input.lower():
        responses = [
            "EDA is the process of analyzing data sets to summarize their main characteristics, often using visual methods. 📈",
            "It's a crucial step in data analysis to understand patterns and anomalies! Want to learn more? 🔍"
        ]
        st.write(random.choice(responses))
    elif "Who are you" in user_input.lower():
        responses = [
            "I am a bot created by Aman, here to assist you! 🤖",
            "Just your friendly neighborhood data assistant created by Aman! How can I help? 🌐"
        ]
        st.write(random.choice(responses))
    elif "who is Satyam" in user_input.lower() or "who is Anshuman" in user_input.lower():
        responses = [
            "He is the owner's very good friend! They both play games together. 🎮",
            "He is great pal of my owner! They enjoy gaming together! 🕹️"
        ]
        st.write(random.choice(responses))
    else:
        responses = [
            "I'm not sure what you mean, but I'm all ears! 👂", 
            "Can you rephrase that? My circuits are a bit tangled! 🤔"
        ]
        st.write(random.choice(responses))
else:
    st.write("Feel free to ask me anything about data cleaning or EDA! I'm here to help! 🎉")

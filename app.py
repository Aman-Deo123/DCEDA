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

if user_input:
    # Simple response logic with funky replies
    if "hello" in user_input.lower():
        responses = ["Hi pookie! 🌟", "Hello there, superstar! ✨", "Hey, you fabulous human! 😄"]
        st.write(random.choice(responses))
    elif "data" in user_input.lower():
        responses = ["Data? Oh, I love data! Let's dive in! 🏊‍♂️", "Data is my jam! What do you need? 🎶"]
        st.write(random.choice(responses))
    elif "help" in user_input.lower():
        responses = ["Help? I'm here to save the day! 🦸‍♂️", "Need help? I'm your trusty sidekick! 🤖"]
        st.write(random.choice(responses))
    else:
        responses = ["I'm not sure what you mean, but I'm all ears! 👂", "Can you rephrase that? My circuits are a bit tangled! 🤔"]
        st.write(random.choice(responses))
else:
    st.write("Feel free to ask me anything about data cleaning or EDA! I'm here to help! 🎉")

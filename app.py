import pandas as pd#type:ignore
import numpy as np#type:ignore
import streamlit as st#type:ignore
import matplotlib.pyplot as plt#type:ignore
import seaborn as sns#type:ignore

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
    st.write("### Correlation Matrix")
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
    st.pyplot(plt)

    # Box Plots
    st.write("### Box Plots")
    for col in df.columns:
        if df[col].dtype == np.number:
            plt.boxplot(df[col])
            plt.title(f'Box Plot of {col}')
            plt.xlabel(col)
            plt.ylabel('Value')
            st.pyplot(plt)

else:
    st.info("Please upload a CSV file to get started.")

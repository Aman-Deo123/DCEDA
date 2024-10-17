# Data Cleaning and EDA Chatbot


This project is a web application built using Streamlit to perform data cleaning and exploratory data analysis (EDA) on a CSV file. It provides a user-friendly interface to handle missing values, visualize data, and gain insights through statistical summaries and plots.


## Features
 - **File Upload**: Upload a CSV file to get started.
 - **Data Cleaning**:
     Handling missing values (replacing with mean/median for numeric columns and mode for categorical columns).
     Removing duplicate rows.
 - **Exploratory Data Analysis (EDA)**:
     Summary statistics for numerical columns.
     Histograms for visualizing the distribution of each numeric column.
     Correlation matrix with a heatmap for understanding relationships between variables.
     Box plots for each numeric column to identify outliers.


   
## Tech Stack
        Python: Core programming language used.
        Streamlit: For building the interactive web interface.
        pandas: For data manipulation and cleaning.
        NumPy: For numerical computations.
        Matplotlib & Seaborn: For data visualization.
## How to Run the App
   Clone the repository:

   bash
   Copy code
   git clone https://github.com/Aman-Deo123/DCEDA
   cd data-cleaning-eda-chatbot
   Install the required dependencies:

   bash
   Copy code
   pip install -r requirements.txt
   Run the Streamlit app:

   bash
   Copy code
   streamlit run app.py
   Open your browser and go to https://edadc-07.streamlit.app to interact with the app.

## Usage
   1. Upload a CSV file using the file uploader widget.
   2. The app will display available columns, handle missing values, and clean the data.
   3. Explore the data with statistical summaries, histograms, correlation heatmaps, and box plots.
## Sample Output
   The app will show:

   Available columns: List of columns in the uploaded CSV.
   Missing values: Number of missing values in each column.
   Summary statistics: Descriptive stats (mean, median, etc.).
   Visualizations: Histograms, box plots, and a correlation heatmap.

 ## Future Improvements
    Adding more advanced data cleaning techniques.
    Enhancing EDA features with more visualization types.
    Allowing more flexible options for missing value handling and duplicate removal.


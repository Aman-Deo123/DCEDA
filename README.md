# Data Cleaning and EDA Chatbot

## Overview
This Streamlit application allows users to upload a CSV file for data cleaning and exploratory data analysis (EDA). The app provides an interactive interface for handling missing values, removing duplicates, and visualizing data through histograms, correlation matrices, and box plots. Additionally, it features a simple chatbot that responds to user queries.

## Features
- **File Upload**: Users can upload CSV files for analysis.
- **Data Cleaning**:
  - Identifies and displays missing values.
  - Fills missing numerical values with the mean and categorical values with the mode.
  - Removes duplicate entries from the dataset.
- **Exploratory Data Analysis**:
  - Displays summary statistics of the dataset.
  - Generates histograms for numerical columns.
  - Creates a correlation matrix heatmap.
  - Produces box plots for numerical columns.
- **Chatbot Interaction**: Users can interact with a chatbot that provides responses based on user input.

## Requirements
To run this application, you need to have the following Python packages installed:
- `pandas`
- `numpy`
- `streamlit`
- `matplotlib`
- `seaborn`

You can install the required packages using pip:
```bash
pip install pandas numpy streamlit matplotlib seaborn
```

## How to Run
   Clone this repository or download the code.
   Navigate to the directory containing the script.
   Run the application using Streamlit:
   Edit
   Copy code
   streamlit run app.py
Open the provided URL in your web browser to access the application.


## Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, please feel free to submit a pull request.


### Explanation of the Sections:
- **Overview**: Provides a brief description of the application and its purpose.
- **Features**: Lists the functionalities offered by the app.
- **Requirements**: Specifies the necessary Python packages for running the app.
- **How to Run**: Offers step-by-step instructions for executing the application.
- **Contributing**: Encourages others to contribute to the project.

Feel free to adjust any part of this template to better fit your project's specifics! If you need further assistance, just let me know.

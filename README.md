# Data Analysis - ImmoEliza

- **Repository**: `challenge-data-analysis`
- **Type of Challenge**: `Consolidation`
- **Duration**: `3 days`
- **Deadline**: `22/11/2024 12:30`
- **Team Size**: 3

## Description

This project aims to analyze real estate data for "ImmoEliza," a company looking to dominate the real estate market in Belgium. By cleaning, exploring, and interpreting the dataset, we intend to extract valuable insights that will guide the development of a predictive pricing model for properties.

## Installation

To set up the environment for this project:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   ```
2. **Navigate to the Directory**:
   ```bash
   cd challenge-data-analysis
   ```
3. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```
4. **Install Required Packages**:
   ```bash
   pip install pandas numpy matplotlib seaborn folium scikit-learn
   ```

## Usage

To run the data analysis:

1. **Activate the Virtual Environment**:
   ```bash
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```
2. **View Analysis Process**:
   ```bash
   Data_Analysis.ipynb
   ```
   This file outlines the steps we took to clean, analyze and visualize the data.

## Visuals

View "ImmoEliza - Data Analysis Presentation.pdf" for insights and interpretations.

![Screenshot from 2024-11-20 15-39-12](https://github.com/user-attachments/assets/05eb2d18-6eda-49c1-9d7a-d9b2fe2517e0)
                                    Example for Graphs we created 

## Contributors

- **Hussain**: https://github.com/Mohammedhussingh
Responsible for data cleaning, organization, encoding, and feature engineering.

- **Vera**: https://github.com/IVera96
Contributed to data encoding, data analysis, and answering the required questions.

- **Nicole**: https://github.com/npret
Focused on data exploration, feature prioritization, and preparing presentation.

## Timeline

1. **Day 1**: Data Cleaning and Preparation.
2. **Day 2**: Exploratory Data Analysis and Visualization.
3. **Day 3**: Interpretation, Insights, and Presentation.


## Mission Objectives

- Utilize `pandas` for effective data handling.
- Apply data visualization tools such as `matplotlib` or `seaborn`.
- Clean datasets to prepare them for analysis.
- Utilize colors effectively in visualizations.
- Draw conclusions and interpret data insights.
- Develop and answer creative questions about the dataset.

## Steps to Complete the Analysis

### Step 1: Data Cleaning

To ensure meaningful analysis, the dataset needs to be cleaned:

- Remove duplicates.
- Trim any blank spaces in strings.
- Correct errors and fill or remove empty values.

### Step 2: Data Analysis

Once cleaned, perform exploratory analysis:

- **Basic Analysis**: Determine the number of rows and columns, and analyze correlations between variables and price.
- **Correlation Analysis**: Use visualizations to explore relationships between variables.
- **Key Metrics**: Identify which variables have the greatest influence on price and which have the least. Calculate the percentage of missing values per column.

### Step 3: Data Interpretation

Communicate the insights gained from your analysis using visual tools and summaries. Example questions to address include:

- Identify and plot outliers.
- Which variables are redundant and should be removed?
- Create a histogram of property surfaces.
- Identify the top 5 most important variables.
- Determine the most and least expensive municipalities in Belgium, Wallonia, and Flanders based on average and median prices.

## Plots Must-Have

- A descriptive title.
- Legends where appropriate.
- Properly labeled axes, including units.
- Thoughtful use of colors.
- Comparable scales when comparing data.
- Avoid overlapping text to improve readability.

## Evaluation Criteria

| Criteria       | Indicator                                   | Yes/No |
| -------------- | ------------------------------------------ | ------ |
| Completeness   | Answered all outlined questions             |        |
|                | Used `pandas`, `matplotlib`, or `seaborn`   |        |
|                | Presented analysis results effectively      |        |
|                | Clean, well-structured code                 |        |
|                | Comprehensive README                        |        |
| Excellence     | Answered additional creative questions      |        |
|                | Addressed bonus questions                   |        |
|                | Used effective colors in visualizations     |        |






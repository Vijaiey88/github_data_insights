# GitHub Data Dive

## Introduction
GitHub Data Dive is an interactive web application designed to extract, analyze, and visualize data from GitHub repositories. It leverages the GitHub API to provide insights into repository dynamics such as programming language popularity, repository activity levels, and license types. The application helps developers, organizations, and educators explore trending open-source projects, make informed decisions about collaboration opportunities, and identify educational resources effectively.

## Skills and Technologies Used
- **Languages & Libraries:** Python, Pandas, Streamlit, SQL, Plotly
- **APIs:** GitHub API
- **Technologies:** Data Extraction, Data Cleaning, Data Analysis, Data Visualization


## Approach
1. **Data Extraction:** Using the GitHub API to extract data from repositories based on 10 trending topics in the data world. The data includes:
   - Repository Name
   - Owner
   - Description
   - URL
   - Primary Programming Language
   - Creation Date
   - Last Updated Date
   - Stars, Forks, and Open Issues count
   - License Type

2. **Data Cleaning:** Handle missing values and ensure data consistency by standardizing formats.

3. **Data Storage:** Store cleaned data in a SQL database for efficient access and manipulation.

4. **Data Analysis:** Analyze trends such as popular programming languages and repository activity.

5. **Visualization:** Build an interactive Streamlit application to visualize insights and allow user interaction.

6. **Deployment:** Deploy the Streamlit app using Render for public access and scalability.

## Installation
To set up the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/github-data-dive.git
   cd github-data-dive
   
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Configure your SQL database connection in the script using the connection string:
   ```bash
   connection_string = 'mysql+pymysql://username:password@localhost/github_data'

4. Run the application:
   ```bash
   streamlit run app.py

## Demo

![Github Data Insights](https://github.com/user-attachments/assets/4d65d95b-93cc-4bdb-9c5d-4aa2cc919610)

## Usage
The application provides the following functionalities:
- **Displaying Raw Data:** View repository data directly from the database in a table format.
- **Popular Programming Languages Visualization:** Analyze the most popular programming languages used in repositories.
- **Repository Activity Analysis:** Visualize repository activity through a scatter plot of stars vs. forks.
- **Tracking Repository Growth:** Track the number of repositories created over the years using a line chart.
- **License Type Exploration:** Examine the most common license types used across repositories.
- **Data Filtering:** Filter repositories based on programming languages, stars, and forks through an interactive sidebar for tailored insights.

## Features
- **Data Filtering:** Easily filter repositories by programming language, minimum stars, and forks.
- **Interactive Visualizations:** Leverage Plotly for dynamic charts, including bar charts, scatter plots, and line graphs, providing an engaging user experience.
- **Dynamic Data Exploration:** Explore repository details interactively with a user-friendly interface, enabling deeper insights and analysis.

## Results
- **Cleaned and Structured Dataset:** A dataset detailing repositories related to 10 trending topics in the data world, including metrics such as stars, forks, programming languages, and creation dates.
- **Streamlit Web Application:** A fully functional and interactive application allowing users to explore and visualize repository data dynamically.
- **Comprehensive Documentation:** Detailed documentation outlining the project methodology and instructions for using the application, ensuring easy setup and usage.

## References
   - **GitHub API Documentation:** [GitHub REST API v3](https://docs.github.com/en/rest) - Official documentation on accessing GitHub repository data.
   - **Streamlit Documentation:** [Streamlit Docs](https://docs.streamlit.io/) - Comprehensive guide for building web apps with Streamlit.
   - **Plotly Documentation:** [Plotly Python Graphing Library](https://plotly.com/python/) - Reference for creating interactive visualizations with Plotly.
   - **Pandas Documentation:** [Pandas Docs](https://pandas.pydata.org/pandas-docs/stable/) - Useful for data manipulation and analysis.
   - **SQLAlchemy Documentation:** [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) - Guide for setting up and using the SQL database interface.

## Feedback
If you have any feedback, please reach out to me at vijaiey88@gmail.com

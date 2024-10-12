import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Create the connection string
connection_string = 'mysql+pymysql://root:inba568.@localhost/github_data'

# Create the engine
engine = create_engine(connection_string)

# Set Streamlit page configuration for wide layout
st.set_page_config(page_title="GitHub Data Dive", layout="wide")

# Streamlit app title
st.title("GitHub Data Dive: Repository Insights")

# Load data from the database
@st.cache_data
def load_data():
    connection = engine.connect()
    df = pd.read_sql('SELECT * FROM repo_data', connection)
    connection.close()
    return df

# Load and display the dataset
df = load_data()

# Display raw data option
if st.checkbox("Show Raw Data"):
    st.subheader("GitHub Repositories Data")
    st.write(df)

# Popular programming languages visualization
st.subheader("Top 10 Programming Languages")
language_counts = df['Programming Language'].value_counts().head(10).reset_index()
language_counts.columns = ['Programming Language', 'Count']
fig = px.bar(language_counts, x='Programming Language', y='Count', color='Programming Language',
             title='Top 10 Programming Languages Used in Repositories')
st.plotly_chart(fig)

# Repository activity analysis (stars and forks) with Plotly
st.subheader("Repository Activity: Stars vs. Forks")
fig = px.scatter(df, x='Number of Stars', y='Number of Forks', hover_name='Repository Name',
                 title='Stars vs. Forks', opacity=0.5)
st.plotly_chart(fig)

# Repository growth analysis over time with Plotly
st.subheader("Repositories Created Over the Years")
df['Creation Date'] = pd.to_datetime(df['Creation Date'])
df['Creation Year'] = df['Creation Date'].dt.year
repos_per_year = df.groupby('Creation Year').size().reset_index(name='Count')
fig = px.line(repos_per_year, x='Creation Year', y='Count', markers=True, title='Repositories Created Over the Years')
st.plotly_chart(fig)

# License type analysis with Plotly
st.subheader("Top 10 License Types")
license_counts = df['License Type'].value_counts().head(10).reset_index()
license_counts.columns = ['License Type', 'Count']
fig = px.bar(license_counts, x='License Type', y='Count', color='License Type', title='Top 10 License Types Used in Repositories')
st.plotly_chart(fig)

# Filter data by programming language
selected_language = st.selectbox("Select a Programming Language", ['All'] + list(df['Programming Language'].dropna().unique()))

if selected_language != 'All':
    filtered_df = df[df['Programming Language'] == selected_language]
else:
    filtered_df = df


# Additional filtering: Stars and Forks
st.sidebar.header("Additional Filters")
min_stars = st.sidebar.slider("Minimum Stars", 0, int(df['Number of Stars'].max()), 0)
min_forks = st.sidebar.slider("Minimum Forks", 0, int(df['Number of Forks'].max()), 0)

# Apply additional filters based on stars and forks
filtered_df = filtered_df[(filtered_df['Number of Stars'] >= min_stars) & (filtered_df['Number of Forks'] >= min_forks)]

# Display data after applying filters
st.subheader(f"Filtered Repositories for {selected_language}")
st.write(filtered_df[['Repository Name', 'Owner', 'Number of Stars', 'Number of Forks', 'License Type']])

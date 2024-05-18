# Movie Recommendation System

This project is a simple movie recommendation system that suggests 5 related movies based on a given movie title. The recommendation is made using cosine similarity between the movie descriptions and other features.

## Data Sources

The system utilizes two datasets:
- **tmdb_5000_movies.csv**: Contains information about movies including titles, overviews, genres, and keywords.
- **tmdb_5000_credits.csv**: Contains data about movie credits including cast and crew details.

## Setup

1. **Dependencies**: Make sure you have the following Python libraries installed:
   - pandas
   - numpy
   - ast
   - scikit-learn
   - nltk
   - streamlit

2. **Data Loading**: Load the movie datasets `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`.

3. **Data Processing**: Perform data cleaning and transformation steps including handling missing values, converting JSON strings to lists, extracting relevant information such as genres, keywords, cast, and crew, and generating movie tags.

4. **Vectorization**: Use CountVectorizer from scikit-learn to convert text data into numerical vectors.

5. **Similarity Calculation**: Compute cosine similarity between movie vectors to find related movies.

6. **Recommendation**: Implement the `recommend` function which takes a movie title as input and recommends 5 related movies based on similarity scores.


## Streamlit App

There is also a Streamlit app deployed for this movie recommendation system. You can try it out [here](https://movie-recommendation-9xvo.onrender.com/).

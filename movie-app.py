import streamlit as st
import pickle
import pandas as pd
import requests
import time
from requests.exceptions import RequestException

st.set_page_config(layout="wide")

def fetch_poster(movie_id):
    max_retries = 3
    retry_delay = 1  # in seconds
    for _ in range(max_retries):
        try:
            response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
            response.raise_for_status()
            data = response.json()
            return "http://image.tmdb.org/t/p/w500/" + data['poster_path']
        except RequestException:
            time.sleep(retry_delay)
    return None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_poster_urls = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        poster_url = fetch_poster(movie_id)
        recommended_poster_urls.append(poster_url)
    return recommended_movies, recommended_poster_urls

st.title('Movie Recommender')
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Load movie dictionary
movie_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

# Select box with a default non-selectable option
selected_movie_name = st.selectbox(
    "Find Movie",
    ["Select movie"] + list(movies['title'].values),
    index=0,
    format_func=lambda x: "Select a movie" if x == "Select movie" else x
)

# To check if the selected option is valid
if selected_movie_name != "Select movie":
    if st.button("Recommend"):
        names, posters = recommend(selected_movie_name)
        columns = st.columns(len(names))
        for name, poster_url, col in zip(names, posters, columns):
            col.header(name)
            if poster_url:
                col.image(poster_url)
            else:
                col.write("Poster not available")
else:
    st.write("Please select a movie from the dropdown.")

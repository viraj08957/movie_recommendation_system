import streamlit as st 
import pickle
import pandas as pd 

def recommend(movie):


    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommend_movies = [] 
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


    for i in movies_list:
        print(new_df.iloc[i[0]].title)


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Choose a movie')

select_movie_name= st.selectbox(
    "how would you liked to be connected?",
    movies['title'].values


)

if st.button("Recommend"):
    recommendations = recommend(select_movie_name)
    for i in recommendations:
        st.write(i)

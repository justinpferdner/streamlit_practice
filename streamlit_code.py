import streamlit as st
import pandas as pd
import numpy as np

st.title('Lab 9: Streamlit')

data = pd.read_csv('AppleStore.csv')

selected_price_range = st.sidebar.slider('Select Price Range', min_value=0.0, max_value=20.0, value=(0.0, 20.0))
all_genres = data['prime_genre'].unique()
genre = st.sidebar.multiselect('Select Genre', all_genres, default= all_genres)


filtered_data = data[(data['prime_genre'].isin(genre)) & (data['price'] >= selected_price_range[0]) & (data['price'] <= selected_price_range[1])]


# View the Raw Data
if st.checkbox('View Data'): 
    st.subheader('Raw Data')
    st.write(filtered_data)

# Chart: Apps with the most ratings
st.subheader('Apps with Most Ratings (Top 10)')
top_rated_apps = filtered_data.sort_values(by='rating_count_tot', ascending=False).head(10)
st.bar_chart(top_rated_apps.set_index('track_name')['rating_count_tot'], use_container_width=True)

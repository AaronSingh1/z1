import streamlit as st
import requests

CAT_API_URL = "https://api.thecatapi.com/v1/images/search"
BREEDS_API_URL = "https://api.thecatapi.com/v1/breeds"

def get_cats(breed_id=None):
    params = {'limit': 9, 'size': 'small'}
    if breed_id:
        params['breed_ids'] = breed_id
    response = requests.get(CAT_API_URL, params=params)
    return response.json()

def get_breeds():
    response = requests.get(BREEDS_API_URL).json()
    return {breed['id']: breed['name'] for breed in response}

st.title("🐱 Random Cat Gallery")
breeds = get_breeds()
selected_breed = st.selectbox("Filter by breed:", ["All"] + list(breeds.values()))

if selected_breed != "All":
    breed_id = [k for k, v in breeds.items() if v == selected_breed][0]
else:
    breed_id = None

if st.button("Load More Cats 🐈"):
    cats = get_cats(breed_id)
    for cat in cats:
        st.image(cat['url'], width=300)

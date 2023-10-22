import streamlit as st
import langchain_helper
st.title("Restaurant Name Generator")

cuisine=st.sidebar.selectbox("Pick a cuisine", ("Italian",
    "Japanese",
    "Chinese",
    "Mexican",
    "Indian",
    "French",
    "Thai",
    "Mediterranean",
    "Greek",
    "Spanish",
    "Korean",
    "Vietnamese",
    "Brazilian",
    "American",
    "Cajun",
    "Middle Eastern",
    "Caribbean",
    "African",
    "Turkish",
    "Peruvian"))


if cuisine:
 response=langchain_helper.gen_res_name_and_items(cuisine)
 st.header(response['restaurant_name'].strip())
 menu_items=response['menu_items'].strip().split(",")
 st.write("**Menu Items**")
for item in menu_items:
    st.write("-",item)
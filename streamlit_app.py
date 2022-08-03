import streamlit
streamlit.title("My Parents New Healthy Dinner")
streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oat meal')
streamlit.text("Kale, Spinach & Rocket Smoothie")
streamlit.text("Hard Boiled Free Range Egg")
streamlit.header("Build your own smoothie")


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

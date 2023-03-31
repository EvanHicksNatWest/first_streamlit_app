import streamlit
import pandas
import requests

streamlit.title('Hello World')
streamlit.header('Header')
streamlit.text('Text')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
streamlit.header("Fruityvice Fruit Advice!")

streamlit.text(fruityvice_response.json())
# Normalises JSON data on watermelon
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Above tabulated
streamlit.dataframe(fruityvice_normalized)

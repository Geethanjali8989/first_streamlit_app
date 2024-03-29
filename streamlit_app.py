import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title ("My parents new healthy diner")

streamlit.header ("😍Breakfast menu😍")
streamlit.text('IDLY😎')
streamlit.text('DOSA😉')
streamlit.text('UPMA🍒🍊')


streamlit.header('Breakfast Menu')
streamlit.text('🐟Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard-Boiled 🍳Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Peach'])

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)


fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Peach'])
fruit_to_show=my_fruit_list.loc[fruit_selected]

streamlit.dataframe(fruit_to_show)




#challenge lab
def insert_row_snowflake(new_fruit):
     with  my_cnx.cursor() as my_cur:
           my_cur.execute("insert into FRUIT_LOAD_LIST values('"+ add_my_fruit +"')")
           return "Thanks for adding new fruit " + new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
# add a button to load the fruit
if streamlit.button('Add new fruit'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = insert_row_snowflake(add_my_fruit)
   streamlit.text(my_data_rows) 





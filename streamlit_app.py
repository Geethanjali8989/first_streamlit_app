import streamlit
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

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Peach'])

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)


fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Peach'])
fruit_to_show=my_fruit_list.loc[fruit_selected]

streamlit.dataframe(fruit_to_show)


#new section to display fruity wise api resdponse
streamlit.header("Fruityvice Fruit Advice!")
import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")
streamlit.text(fruityvice_response.json())#just writes data to the screen


# take the json version of data and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output at the table as table
streamlit.dataframe(fruityvice_normalized)






#new section to display fruity wise api resdponse
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Apple')
streamlit.write('The user entered ', fruit_choice)
import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)

# take the json version of data and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output at the table as table
streamlit.dataframe(fruityvice_normalized)



import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute(SELECT * FROM FRUIT_LOAD_LIST)
my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
streamlit.text("THE FRUIT LOAD LIST CONTAINS")
streamlit.text(my_data_row)




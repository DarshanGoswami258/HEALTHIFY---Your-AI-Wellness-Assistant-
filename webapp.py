import streamlit as st
import google.generativeai as genai
import pandas as pd 
import os

api = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# Let's create the UI
st.title(':orange[Healthify] : :blue[AI Powered Personal Health Assistant]')
st.markdown('''#### This application will assist you to have a better and healthy life. your health realted questions and get Personalised guidence.''')
tips = ''' Follow the Steps
* Enter your details in the side bar.
* Enter your gender, age, height (cms), weight (kgs).
* Select the number on the fitness scale (0-5). 5-Fittest and 0-Not fittness at all.'''
st.write(tips)


st.sidebar.header(':red[Enter Your Details]')
Name = st.sidebar.text_input('Enter Your Name')
gender = st.sidebar.selectbox('Select Your gender', ['Male','Female','Other'])
age = st.sidebar.text_input('Enter Your Age in Yrs')
height = st.sidebar.text_input('Enter Your Height in Cms')
weight = st.sidebar.text_input('Enter Your Weight in Kgs')
fitness = st.sidebar.slider('Rate Your Fittness (0-5)', 0, 5, 3)
bmi = pd.to_numeric(weight) / ((pd.to_numeric(height)/100) ** 2)
st.sidebar.write(f'{Name} Your BMI: {round(bmi,2)} kg/m^2')

# Let's Use GenAI Model to get the Output
user_query = st.text_input('Enter Your Question Here')
prompt = f'''Assume you are a Health Expert. You are Required to answer the question asked
by the user. Use the Following Details provided by the user.
name of user is {Name},
gender is {gender},
age is {age},
height is {height} cms,
weight is {weight} kgs,
bmi is {bmi} kg/m^2,
and user rates his/her fitness as {fitness} out of 5

Your output should be in the following format
* It start by giving one two line comment on the details that have been provided.
* It should explain what the real problem is based on the query asked by the user.
* What could be the possible reason for the problem.
* What are the possible solutions for the problem.
* You can also mention what doctor to see (Specialization) if required.
* Strickly do not recommend any medicine Even if asked.
* output should be in bullet points and usetables wherever required
* In the End Give me a 5 to 7 line of summary.

here is the query from the users {user_query}'''


if user_query:
    response = model.generate_content(prompt)
    st.write(response.text)
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import time,datetime
import sqlite3


def main():
    st.header("Demo app to learn and share")
    conn = sqlite3.connect("data/WSDA_Music.db")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM artist;""")
    dfa =pd.DataFrame(cur)
    st.write(dfa)

    #Example 1
    st.write('Hello, * worlld!* :sunglasses: :wolf:')

    #example 2
    st.write(1234)

    #Example panda frame
    df = pd.DataFrame(
        {
            'first column':[1,2,3,4],
            'second column':[10,20,30,40]        }
    )
    st.write(df)

    #example 3
    st.write('below is  a data frame:',df,'Above is a data frame :womens:')

    #example 4
    df2  = pd.DataFrame(
        np.random.randn(200,3),
        columns =['a','b','c'])
    c =alt.Chart(df2).mark_circle().encode(x='a',y='b',size='c',tooltip=['a','b','c'])
    st.write(c)

    #example 5

    st.subheader('Range Slider Demo')

    values = st.slider(
        'Select a range of value',
        0.0,100.0,(25.0,75.0))
    st.write('values:', values)

    #example 6

    st.subheader('Range time Slider')
    appointment = st.slider(
        'Select your appointment:',
        value =(time(11,30),time(12,45)))
    st.write("You're scheduled for :",appointment)


    #example 7
    st.subheader("Datetime Slider")
    start_time =st.slider(
        "when do you start",
        value =datetime(2020,1,1,9,30),
        format=("MM/DD/YY -hh:mm")
    )
    st.write("Start Time:",start_time)

    #Example 8
    st.header("Line Chart")
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c'])
    st.line_chart(chart_data)

    #example 9
    st.header ('st.selectbox')
    option = st.selectbox(
        'what is your fovorite color?',
        ('Blue','Red','Green'))
    st.write('Your favorite Color is:',option)

    #example 10
    st.header('st.multiselect')
    st.subheader("Multiselect")

    options = st.multiselect(
        'What are your faovrite colors',
        ['Green','Yellow','Red','Blue'],
        ['Yellow','Red'])
    st.write('You selected:',options)

    # example 10

    st.header('Day 12::st.Checkbox')
    st.subheader("st.Checkbox")

    st.write('What would you like to order?')

    icecream = st.checkbox('Ice cream')
    coffee = st.checkbox('Coffee')
    cola = st.checkbox('Cola')

    if icecream:
        st.write("Great! Here's some more 🍦")

    if coffee:
        st.write("Okay, here's some coffee ☕")

    if cola:
        st.write("Here you go 🥤")





if __name__ == "__main__":
    main()
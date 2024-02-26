import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write('Hello world!')

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

import streamlit as st
import numpy as np
import pandas as pd
from pycoingecko import CoinGeckoAPI
import datetime
cg = CoinGeckoAPI()


st.title('Mercado de Criptomonedas')

dataframe = pd.DataFrame(
  np.random.randn(10, 20),
  columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

chart_data = pd.DataFrame(
  np.random.randn(20, 3),
  columns=['a', 'b', 'c'])

st.line_chart(chart_data)

dataframe = pd.DataFrame(
  np.random.randn(20, 3),
  columns=['a', 'b', 'c'])

st.dataframe(dataframe.style.highlight_max(axis=0))

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

if st.checkbox('Show dataframe'):
	chart_data = pd.DataFrame(
		np.random.randn(20, 3),
		columns=['a', 'b', 'c'])

	chart_data

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

df = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])

st.vega_lite_chart(df, {
  'mark': 'circle',
  'encoding': {
  'x': {'field': 'a', 'type': 'quantitative'},
  'y': {'field': 'b', 'type': 'quantitative'},
  'size': {'field': 'c', 'type': 'quantitative'},
  'color': {'field': 'c', 'type': 'quantitative'},
  },
})


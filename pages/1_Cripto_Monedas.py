import pandas as pd
import utils.utils as utl 

import streamlit as st
import numpy as np
import pandas as pd
from pycoingecko import CoinGeckoAPI
import datetime
from datetime import time
from datetime import datetime

cg = CoinGeckoAPI()

today = utl.get_today()

start_time = st.slider(
  "Schedule your appointment:",
  min_value=(datetime(2018, 1, 1)),
  value=(datetime(2020, 1, 1), today))
st.write("You're scheduled for:", start_time[0])


dates = pd.date_range(end=pd.Timestamp.today(), periods=2000, freq='D')

st.write("Start time:", start_time[0])

chart_data = utl.get_data_historical_kpi('bitcoin', 'usd', 1999, 'prices')

chart_data['date'] = dates


filtered_value = chart_data[(chart_data['date'].dt.date > start_time[0].date()) & (chart_data['date'].dt.date < start_time[1].date())] 

st.line_chart(filtered_value, x='date')

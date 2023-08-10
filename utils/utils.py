import pandas as pd 

import streamlit as st
import numpy as np
import pandas as pd
from pycoingecko import CoinGeckoAPI
from datetime import time
from datetime import datetime

cg = CoinGeckoAPI()

@st.cache_data
def get_today(): 
  return datetime.today()

@st.cache_data
def get_data_historical_kpi(id: str, vs_currency: str, days: int, kpi: str):
  coin_data = cg.get_coin_market_chart_by_id(id=id,vs_currency=vs_currency, days=days, interval='daily')
  kpi_data = []
  for data in coin_data[kpi]:
    kpi_data.append(data[1])
  coin_data_df = pd.DataFrame(data={id: kpi_data})
  return coin_data_df

import pandas as pd
import utils.utils as utl 
from streamlit_extras.metric_cards import style_metric_cards
import streamlit as st
import numpy as np
import pandas as pd
from pycoingecko import CoinGeckoAPI
from datetime import datetime
import altair as alt
from streamlit_echarts import st_echarts

cg = CoinGeckoAPI()

st.markdown("""
  <style>
    div.css-26zv68.e1f1d6gn0{
      gap: 0;
      flex-direction: column-reverse;
    }
    
    div.css-1tvsewn.e1f1d6gn0{
   
    }
    
    div.css-1629p8f.e1nzilvr1>h2{
      text-align: center;
      padding: 1rem;
      /* border: 1px solid black; */
      font-size: 1.5rem;
      box-shadow: 0px 0px 5px #00000033;
      border-radius: 0.5rem;
      background-color: #a9a9ef;
      margin-bottom: 0.5rem;
    }
    
    div.element-container>div[data-testid="metric-container"]{
      text-align: center;
    }
    
    div[data-testid="stVerticalBlock"]{
     
    }
    
    div[data-testid="metric-container"]{
      border-right: 0.5rem solid #d3d3ff !important;
    }
    
  </style>
""", unsafe_allow_html=True)

# utl.set_default_keys()

with st.sidebar:
  option = st.selectbox(
    'Moneda de Referencia:',
    ['bitcoin', 'ethereum', 'solana'])
  
style_metric_cards(
  background_color="#d3d3ff",
  border_size_px=0,
  border_radius_px=8,
  border_left_color="#d3d3ff"
)
  
# Data Fetching

# Page Structure  time_value'
    
datos = cg.get_coin_by_id(option, ticket='false', community_data='false', developer_data='false')  
col111, col211 = st.columns([8, 3])
  
with col111:
  st.title('Criptomoneda: ' + option[0].upper() + option[1:])
  
with col211:
   
  st.header('Precio Actual')
  st.metric("czxc", datos['market_data']['current_price']['usd'], label_visibility='collapsed')  
  
  st.header('Datos del Mercado')
  st.metric("Ranking por Capitalización de Mercado", datos['market_cap_rank']) 
   
  col11, col21 = st.columns([1, 1])
  
  with col11:
    st.metric("Total Disponibles", datos['market_data']['total_supply'])
    
  with col21:
     st.metric("Total Circulando", datos['market_data']['circulating_supply']) 
 
  with st.container():
    st.header('Sentimiento del Mercado')
    st.metric("Usuario que la tiene en Porfolio", datos['watchlist_portfolio_users'])  

    col13, col23 = st.columns([1, 1])

    with col13:
      st.metric("Positivo", datos['sentiment_votes_up_percentage'])
      
    with col23:
        st.metric("Negativo", datos['sentiment_votes_down_percentage']) 
 

charts_data = {
  "price" : utl.get_data_historical_kpi(option, 'usd', 'max', 'prices'),
  "market_cap": utl.get_data_historical_kpi(option, 'usd', 'max', 'market_caps'),
  "volumen": utl.get_data_historical_kpi(option, 'usd', 'max', 'total_volumes')
}

total_dates = charts_data['price'].shape[0]

@st.cache_data
def get_dates(periods: int):
  return pd.date_range(end=pd.Timestamp.today(), periods=periods, freq='D') 

dates = get_dates(total_dates )

for key in charts_data:
  charts_data[key] = pd.DataFrame(charts_data[key])
  charts_data[key]['date'] = dates

def filter_by_dates(df_chart, min_date, max_date):
  return df_chart[(df_chart['date'].dt.date > min_date) & (df_chart['date'].dt.date < max_date)] 

col1, col2 = st.columns([3, 1])

with col111:
  
  with st.container():
  
    start_time = st.slider('',
      value=(st.session_state['min_time'] , st.session_state['max_time']), 
      min_value=charts_data['price'].iloc[1,-1].to_pydatetime(),
      max_value=st.session_state['today']
    )

    with st.container():
      price_tab, tab2, tab3 = st.tabs(["Precios", "Capitalización del Mercado", "Volumen de Comercialziación"])
      
      with price_tab:
        
        c = alt.Chart(
          filter_by_dates(charts_data['price'], start_time[0].date(),   start_time[1].date()), 
          padding={"left": 20, "top": 20, "right": 20, "bottom": 20},
          height=450
          ).mark_line().encode(
            x='date', y=option
            )

        st.subheader("Precio Histórico del " + option[0].upper() + option[1:])
        st.altair_chart(c, use_container_width=True)
         
      with tab2:
        
        c = alt.Chart(
          filter_by_dates(charts_data['market_cap'], start_time[0].date(),   start_time[1].date()), 
          padding={"left": 20, "top": 20, "right": 20, "bottom": 20},
          height=450
        ).mark_line().encode(
            x='date', y=option)

        st.subheader("Capitalización histórica del " + option[0].upper() + option[1:]) 
        st.altair_chart(c, use_container_width=True)

      with tab3:
        
        c = alt.Chart(
          filter_by_dates(charts_data['volumen'], start_time[0].date(),   start_time[1].date()), 
          padding={"left": 20, "top": 20, "right": 20, "bottom": 20},
          height=450  
        ).mark_line().encode(
            x='date', y=option
          )

        st.subheader("Volumen de Comercialización del " + option[0].upper() + option[1:]) 
        st.altair_chart(c, use_container_width=True)
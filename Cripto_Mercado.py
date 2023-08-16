import streamlit as st
import numpy as np
import pandas as pd
import utils.utils as utl
import utils.charts as chr
from pycoingecko import CoinGeckoAPI
import altair as alt
from streamlit_echarts import st_echarts

cg = CoinGeckoAPI()

## Configuración de la página
st.set_page_config(
  page_title="Critomercado by Ricardo Sánchez",
  page_icon="🪙",
  layout="wide",
  initial_sidebar_state="expanded",
)

st.markdown("""
  <style>
    div.css-26zv68.e1f1d6gn0{
      gap: 0;
      flex-direction: column-reverse;
    }
    
    div.css-z5fcl4{
      padding: 0rem
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
    
    div.css-1r6slb0.e1f1d6gn1{
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
    
    div[data-testid="stMetricValue"]{
     
    }
    
    div.element-container>div[data-testid="metric-container"]{
      display: flex;
      flex-direction: column;
      text-align: center;
      align-items: center;
    }
    
    div.css-1xarl3l{
      font-size: 3rem;
    }
    
  </style>
""", unsafe_allow_html=True)

utl.set_default_keys()
st.title('Panorama General del Criptomercado')

with st.sidebar:
  
  vs_currency = st.selectbox(
    'Moneda de Referencia:',
    utl.get_vs_currencies()
  )
  st.session_state['vs_currency'] = vs_currency

st.markdown('''El mercado de Criptomendas esta liderado por un grupo peque;o de moendas las cuales abarcan gran parte de la capitalizacion del mercado en general. Estas''')

global_data = utl.get_global_data(vs_currency)

col1, col2, col3 = st.columns(3)
col1.metric("Total de mercados", global_data['markets'])
col2.metric("Cripto monedas Activas", global_data['active_cryptocurrencies'])
col3.metric("Capitalización total del mercado", utl.human_format(global_data['total_market_cap']) + " usd")

col12, col22 = st.columns([1, 1])

with col12:
  
  market_categories = pd.DataFrame(cg.get_coins_categories())
  data = market_categories.iloc[0:10, :]
  
  options = {
    "yAxis": {
        "type": "category",
        "data": list(data['name']),
    },
    "title": {"text": "Porcentaje de Capitalizacion del Mercado", "left": "center"},
    "xAxis": {"type": "value"},
    "series": [{"data": list(data['market_cap']), "type": "bar"}],
  }
  
  c = alt.Chart(data, 
    height=400,
  
    ).mark_bar().encode(
      y='name', x="market_cap"
    )

  st.altair_chart(c, use_container_width=True)
  
with col22:
  
  market_categories = pd.DataFrame(cg.get_coins_categories())
  data = market_categories.iloc[0:10, :]
  
  exchanges_categories = pd.DataFrame(cg.get_exchanges_list())
  exchanges_categories_top_10_trust = exchanges_categories.sort_values(by='trust_score_rank', ascending=True).head(10)
  data = exchanges_categories.sort_values(by='trust_score_rank', ascending=True).head(11)
  
  options = {
    "yAxis": {
        "type": "category",
        "data": list(data['name']),
    },
    "title": {"text": "Porcente Capitalizacion del Mercado", "left": "center"},
    "xAxis": {"type": "value"},
    "series": [{"data": list(data['trade_volume_24h_btc']), "type": "bar"}],
  }
  
  
  
  c = alt.Chart(data, 
    height=400,
    ).mark_bar().encode(
      y='name', x="trade_volume_24h_btc"
      )

  st.altair_chart(c, use_container_width=True)
  

option = {
  "title": {"text": "Porcentaje de Capitalizacion del Mercado", "left": "center"},
  "tooltip": {"trigger": "item"},
  "series": [
    {
      "type": 'pie',
      "data": global_data['market_cap_percentage'],
      "radius": '70%',
      "emphasis": {
        "itemStyle": {
            "shadowBlur": 10,
            "shadowOffsetX": 0,
            "shadowColor": "rgba(0, 0, 0, 0.5)",
        }
      },
    }
  ]
}

col1, col2 = st.columns([2, 2])
data = np.random.randn(10, 1)

with col1:
  chr.plot_treemap()

with col2:  
  st_echarts(option, height="500px")
  
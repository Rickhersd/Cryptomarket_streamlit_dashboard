import pandas as pd 

import streamlit as st
import numpy as np
import pandas as pd
from pycoingecko import CoinGeckoAPI

from datetime import datetime

cg = CoinGeckoAPI()

@st.cache_data
def get_today(): 
  return datetime.today()

@st.cache_data
def get_data_historical_kpi(id: str, vs_currency: str, days, kpi: str) -> pd.DataFrame:
  """
  Función para obtener los datos historicos de una criptomoneda
  ...
  Parámetros
  ----------
  id : str
    identificador de la Criptomenda (ejemplo "bitcoin")
  vs_currency : str
    Moneda contra la que se compara el precio de la cripto solicitada
  days : str | int
    Cantidad de días para el rango del gráfico desde hoy (10, 20, 50). Si se indica "max" devuelve todo el historial
  kpi : int
    Métrica: prices, total-volumes o market-caps 

  """
  coin_data = cg.get_coin_market_chart_by_id(id=id,vs_currency=vs_currency, days=days, interval='daily')
  kpi_data = []
  for data in coin_data[kpi]:
    kpi_data.append(data[1])
  coin_data_df = pd.DataFrame(data={id: kpi_data})
  return coin_data_df

@st.cache_data
def get_global_data(vs_currency: str) -> dict:
  data = cg.get_global()
  return {
    'active_cryptocurrencies': data['active_cryptocurrencies'],
    'upcoming_icos': data['upcoming_icos'],
    'ongoing_icos': data['ongoing_icos'],
    'ended_icos': data['ended_icos'],
    'markets': data['markets'],
    'total_market_cap': data['total_market_cap'][vs_currency],
    'market_cap_percentage': [{'value':data['market_cap_percentage'][key], 'name':key } for key in data['market_cap_percentage']],
    'updated_at': data['updated_at']
  }

# @st.cache_data
# def get_global_data():

@st.cache_data
def get_vs_currencies():
  return cg.get_supported_vs_currencies()

def set_default_keys():
  """
  Establece todos los valores por defecto de las keys de las sesión para evitar errores de valores no encontrados. Se debe de ejecutar al comienzo de cada página de Streamlit.
  """
  
  default_keys={
    'today': get_today(),
    'vs_currency': 'usd',
    'min_time': datetime(2020, 1, 1),
    'max_time': get_today()
  }
  
  for key in default_keys:
    if key not in st.session_state:
      st.session_state[key] = default_keys[key]
    

def human_format(num):
  """
  Recibe una cantidad n y la devuelve a un formato x.xx maginud para mayor comprensión
  """
  
  magnitude = 0
  while abs(num) >= 1000:
    magnitude += 1
    num /= 1000.0
  return '%.2f %s' % (num, ['','Miles', 'Millones', 'Miles de Millones', 'Billones', 'Trillones'][magnitude])
import streamlit as st
import utils.utils as utl

## Configuración de la página
st.set_page_config(
  page_title="Criptomercado por Ricardo Sánchez",
  page_icon="🪙",
  layout="wide",
  initial_sidebar_state="expanded",
)

utl.set_default_keys()

_, center, _ = st.columns([1,3,1])

body = """
# Análisis del Criptomercado por Ricardo Sánchez

El análisis que se presenta a continuación consiste en una revisión de los datos proporcionados por la API de CoinGecko con el propósito de identificar tendencias o patrones que puedan orientar la selección de diez monedas para inversión. Inicialmente, el objetivo del análisis es proporcionar un contexto general del panorama del criptomercado, seguido por la visualización de los datos históricos de las criptomonedas, incluyendo tanto sus precios como los volúmenes de comercio.

Para lograr este propósito, se desarrollaron dos dashbords interactivos capaces de mostrar de forma clara los datos mas relevantes del criptomercado. Comenzando por una dashboard con el parnorame general del criptomercado seguido por un dashboard capaz de mostrar toda la informacion de una moneda en especico.

Tras la visualizcion de estos graficos, se obtuvieron una serie de conclusiones las cuaels se exponen en la pagina tres de este prouectos. Es importante destacar que el mercado de criptomonedas es conocido por ser uno de los más volátiles entre los diferentes mercados de inversión, si no el más volátil. Por lo tanto, antes de tomar cualquier decisión de inversión, se recomienda contar con un entendimiento sólido de lo que se está invirtiendo, utilizar solo dinero dispuesto a perder y, sobre todo, evitar ser influenciado por el miedo a perderse oportunidades (FOMO) cuando los mercados se encuentran en temporadas alcistas. Dicho esto, también se aclara que las conclusiones propuestas son del mercado en un sentido general y al largo plazo.
 
"""

with center:
  st.markdown(body)
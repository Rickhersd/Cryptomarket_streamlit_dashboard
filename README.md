<div align="center">
  <img src="./src/CoinGecko_Logo.png">
  <p align="center">
    <br>
    <strong>
      Este proyecto fue gracias a CoinGecko
    </strong>
  </p>
</div>

<br>


# **Análisis del Criptomercado con Streamlit**

El proyecto que se presenta a continuación es un analisis del criptomercado, en le que, apartir de los datos propuetost por la Api de CoinGecko con los datos historicos de las critpos se busca buscar patrones o tendencias para se visualizan los graficos. El trabajo se llevó a cabo en un notebook en formato ipynb y culminó en la creación de un dashboard utilizando la biblioteca Streamlit.

El proyecto fue encomendado por el Bootcamp SoyHenry y forma parte del segundo proyecto individual obligatorio para la graduación del bootcamp. De acuerdo con las directrices originales, se nos asignó el siguiente rol:

"En los últimos años, el mercado de criptomonedas ha experimentado un crecimiento exponencial y una adopción creciente a nivel mundial. La aparición del Bitcoin en 2009 marcó el inicio de una revolución financiera que ha llevado a la creación de miles de criptomonedas diferentes, con diversas funcionalidades y tecnologías subyacentes.

Con el aumento del interés en el mercado de criptomonedas, cada vez más inversores, empresas y entusiastas buscan comprender mejor el comportamiento y la evolución de estos activos digitales. Sin embargo, la naturaleza altamente volátil y compleja de las criptomonedas presenta desafíos significativos para aquellos que desean tomar decisiones informadas sobre inversiones o simplemente comprender mejor cómo funcionan estos mercados emergentes.

El análisis y la exploración de datos desempeñan un papel crucial en la obtención de información valiosa dentro del vasto conjunto de datos disponibles sobre criptomonedas. En este contexto, el uso de una fuente de datos actualizados es fundamental para proporcionar información sobre una amplia variedad de criptomonedas, incluyendo precios, volúmenes de negociación, capitalización de mercado, información histórica y más."

## **Desarrollo del Proyecto**

La ejecución del proyecto comenzó con un análisis exploratorio de los datos proporcionados por la API de CoinGecko. Después de visualizar los datos y los gráficos históricos de las criptomonedas, se procedió al desarrollo del dashboard utilizando Streamlit. Aunque esta librería no es la elección habitual para dashboards, se optó por ella debido a la intención de desarrollar el proyecto exclusivamente en Python o para tener un primer acercamiento a este reconocido framework. Es importante destacar que los gráficos proporcionados por Streamlit resultaron limitados en mi opinión, lo que llevó a la utilización de librerías como Echarts y Vegas Altair para generar gráficos de mayor calidad y flexibilidad.

Este proyecto fue completado en una semana, durante la cual se logró desarrollar la aplicación web con Streamlit y se realizó el análisis exploratorio de la API de CoinGecko.

### **Librerías utilizadas**

- **Streamlit:** Framework base para la creación del sitio web multipágina.
- **Echarts:** Biblioteca de JavaScript utilizada para la visualización de gráficos en el frontend, adaptada para funcionar en el entorno de Python.
- **Streamlit - Extras:** Biblioteca que permite la incorporación de nuevos widgets y elementos estéticos a la interfaz creada con Streamlit.
- **Pandas:** Biblioteca utilizada para la manipulación y análisis de datos tabulares.
- **Vegas-altair:** Biblioteca que proporciona herramientas de visualización de datos, integrada en Streamlit para mejorar las capacidades gráficas.
- **Matplotlib y Seaborn:** Bibliotecas utilizadas para la creación de gráficos y visualizaciones. Fueron empleadas durante el análisis exploratorio de datos (EDA).
- **CoinGeckoAPI:** Biblioteca diseñada para simplificar el acceso y la interacción con la API de CoinGecko, facilitando la obtención de datos relacionados con criptomonedas.

### **Estructura del Respositorio**

Al ser un proyecto hecho en streamlit, la estructura del repo esta acorde a la arquitecutra del framework de una aplicación Multipages. 

- El archivo Cripto_Mercados es la pagina principal del proyecto. 
- Dentro de la carpeta pages se ecnuentran todas las paginas de la aplicación web.
- Para tener un código refactorizado, los métodos de fetching de datos y los gráficos estan dentro de la carpeta utils.

### **Ejecutar en Local**

1. Clonar el repositorio desde GitHub:

```shell
git clone https://github.com/Rickhersd/Cryptomarket_streamlit_dashboard.git
```

2. Ingresar a la carpeta del repositorio y instalar las bibliotecas necesarias. Se recomienda crear un entorno virtual previamente, ya sea utilizando pyenv o virtualenv.

> *Nota: Es necesario tener instalado una versión de Python superior a la 3.7.X para correr la apliación*  

```shell
cd ./Cryptomarket_streamlit_dashboard 
pip install -r requirements.txt
```

3. Ejecutar el siguiente comando para iniciar la aplicación de Streamlit:

```shell
streamlit run Cripto_Mercado.py
```

4. Esperar a que se inicie el servidor local e ingresar. Por defecto es el http://localhost:8501

## **Dashboard**

El informe y la visualización de los datos se encuentran disponibles en el siguiente enlace: [CryptomercadoPorRicardoSanchez](https://criptomercadobyricardosanchez.streamlit.app/).

La página web consta de cuatro secciones organizadas de la siguiente manera:

1. **Criptomercado**: Un dashboard interactivo que presenta información general del criptomercado. En este apartado se analiza la capitalización total del mercado, la dominancia de las criptomonedas y los exchanges más importantes.

2. **Criptomonedas**: Un dashboard que muestra la información más relevante de las criptomonedas seleccionadas para invertir. Se incluyen los datos históricos de precios, capitalización y volumen total de comercio.

3. **Conclusiones**: En esta sección se resumen todas las conclusiones obtenidas a partir del análisis realizado. Las conclusiones detalladas se encuentran más abajo en la sección correspondiente.

4. **Contacto**: Información de contacto del autor del proyecto.

<details>
  <summary>
    <span><strong>Capturas de Pantalla</strong></span>
  </summary>

### Screenshots

<div align="center">
  <img src="./imgs/Apidocs_page.png">
  <p align="center">
    <strong>
      Página Inicial - Panorama General del Criptomercado
    </strong>
  </p>
</div>

<div align="center">
  <img src="./imgs/Apidocs_page.png">
  <p align="center">
    <strong>
      Página Dos - Dashboards de Criptomonedas
    </strong>
  </p>
</div>

</details>

## **Conclusiones**

Tras realizar una análisis de todas las graficas y sus tendencias, se pudieron obtener las siguientes conclusiones:

- **Histórico de Datos y Correlación con Bitcoin:** Se observa que Bitcoin tiene el conjunto de datos más extenso entre las diez criptomonedas analizadas, abarcando desde 2014. Además, todas las criptomonedas muestran una correlación con el gráfico de Bitcoin, que se ve influenciada por la dominancia de esta moneda. Este aspecto es crucial ya que eventos futuros que impacten positivamente el precio de Bitcoin podrían resultar en aumentos en otras inversiones.

- **Tendencia Alcista General:** En los gráficos de alta temporalidad, se aprecia una tendencia alcista en todas las criptomonedas debido a la correlación alcista con Bitcoin. Esto sugiere que el mercado en su conjunto está en una tendencia alcista a largo plazo. Independientemente de la moneda, todas las selectas parecen ser propuestas sólidas para inversión.

- **Patrón de Aumento y Caída en 2021:** Un patrón común en todas las criptomonedas es el fuerte aumento de precios a principios de 2021, con aumentos de hasta un 600% en la mayoría de los casos, seguido por una corrección en los meses posteriores. Este patrón se repite en todas las monedas y refleja la volatilidad inherente al mercado.

- **Repunte Alcista en 2018:** Un segundo patrón relevante se evidencia en 2018 para varias criptomonedas: Bitcoin, XRP, Cardano, Solana y Ethereum. En este año, se experimentó un repunte alcista que llevó a nuevos máximos históricos. En las otras criptomonedas, no hay suficientes datos históricos para analizar este comportamiento.

- **Exchange idóneo**: Binance es el exchange por excelencia en el criptomercado, tanto por su alto volumen de trading como por su nivel se confianza. Ademas, el BNB, la criptomoneda propia de la plataforma, se sitúa en el top 10 de criptos por capitalizacion del mercado.

- **Relación con las Recompensas de Minería de Bitcoin:** Se identificó que estos repuntes alcistas a finales de 2018 y 2022 coincidieron con eventos en los que las recompensas por la minería de Bitcoin se redujeron. Esta observación respalda la idea de que el mercado es cíclico y sugiere que podría esperarse un patrón similar en 2025 o 2026, cuando se produzca la próxima reducción de recompensas. Cabe resutlar que este mismo patrón ocurrió en el año 2014, en el caso del bitcoin.

- **Volumen de Comercialización y Precio de Bitcoin:** Aunque el volumen de comercio de Bitcoin muestra una tendencia bajista en los últimos meses, el precio de Bitcoin sigue una tendencia alcista. Esto indica un mayor interés en la compra de Bitcoin. Si se repitiera el volumen de comercio de anteriores máximos históricos, podríamos esperar patrones anteriores que conduzcan a nuevos máximos históricos.

- **Potencial de Nuevos Máximos Históricos:** Considerando la fuerte correlación entre las criptomonedas y el Bitcoin, si el mercado cripto en su conjunto experimenta una nueva ola de volumen de comercialización, podríamos anticipar nuevos máximos históricos en todas las criptos selectas.

- **Precio en Relación al Volumen de Comercialización:** A pesar de los volúmenes de comercialización actuales más bajos, los precios se encuentran en niveles más altos en comparación con años anteriores con niveles similares de comercio. Esto sugiere que un aumento en el volumen de comercio podría llevar a nuevos máximos en todas las criptomonedas.

- **Recomendación de Portafolio:** En última instancia, todas las criptomonedas analizadas tienen proyectos sólidos respaldándolas. Sin embargo, la recomendación más sólida sería construir un portafolio que tenga Bitcoin y Ethereum como componentes principales, representando entre un 50% y 70% del capital total, mientras que el resto podría ser distribuido en otras criptomonedas.

## **Contacto**

Me llamo Ricardo Sánchez y soy un Desarrollador Web enfocado al frontend y Analista de Datos de Venezuela. Comencé a los quince años en el mundo de la programación de forma autodidacta enfocando mi aprendizaje al desarrollo web, y tras comenzar la carrera de ingeniería en Informática, decidí orientar mi carrera profesional hacia el mundo del análisis de Datos. Actualmente busco combinar mis conocmientos en ambas áreas para ofrecer diferentes tipos de servicios y busco desarrolar proyectos que combinen tanto plataformas webs como conocimientos de Data.

<br>

<div align="center">
  <a https='https://www.linkedin.com/in/ricardosanchez-dev/'>
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"alt="Linkedin"/>
  </a>
  <a https='mailto:rickhersd2002@gmail.com'>
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/>
  </a>
  <a https="https://wa.me/584120260569?text=Hola,%20Ricardo">
    <img  src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="Whatsapp"/>
  </a>
  <a https='https://github.com/Rickhersd'>
    <img src="https://img.shields.io/badge/Github-151515?style=for-the-badge&logo=github&logoColor=white"alt="Linkedin"/>
  </a>
</div>
from streamlit_echarts import JsCode
import pandas as pd
import pandas as pd
from pycoingecko import CoinGeckoAPI
from streamlit_echarts import st_echarts

cg = CoinGeckoAPI()

def plot_treemap(): 
  market = cg.get_coins_markets('usd', per_page=250)
  market_df = pd.DataFrame(data=market)
  dict_tree = market_df.set_index('id').to_dict()['market_cap'] 
  tree_map_criptos = [{
    'value': dict_tree[key], 
    "name": key,
    "path": key} for key in dict_tree
  ]

  option = {
    "title": {"text": "Treemap del Criptomercado", "left": "center"},
    "tooltip": {
      "formatter": JsCode(
        "function(info){var value=info.value;var treePathInfo=info.treePathInfo;var treePath=[];for(var i=1;i<treePathInfo.length;i+=1){treePath.push(treePathInfo[i].name)}return['<div class=\"tooltip-title\">'+treePath.join('/')+'</div>','Valor: '+ value +' USB'].join('')};"
      ).js_code,
    },
    "series": [
      {
        "name": "Distribucion de Capitalizacion del Cripto Mercado",
        "type": "treemap",
        "visibleMin": 300,
        "label": {"show": True, "formatter": "{b}"},
        "itemStyle": {"borderColor": "#fff"},
        "levels": [
          {"itemStyle": {"borderWidth": 0, "gapWidth": 5}},
          {"itemStyle": {"gapWidth": 1}},
          {
            "colorSaturation": [0.35, 0.5],
            "itemStyle": {"gapWidth": 1, "borderColorSaturation": 0.6},
          },
        ],
        "data": tree_map_criptos
      }
    ],
  }
  st_echarts(option, height="500px")
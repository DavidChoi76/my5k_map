import folium
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
import numpy as np
import re

st.set_page_config(
    page_title="streamlit-folium documentation: Limit Data Return",
    page_icon="🤏",
    layout="wide",
)

"# 2023 함께걸어요 My5K 진행 현황"

m = folium.Map(location=[39.949610, 175.150282], tiles="OpenStreetMap", zoom_start=2.4)  # 39.949610, 175.150282

icons = folium.features.CustomIcon('5k_flag.png', icon_size=(20,20))

# add marker one by one on the map
data = pd.read_csv("data.csv", encoding='CP949')

# add marker one by one on the map

for i in range(0, len(data)):
   folium.Marker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lon']], 
      popup=data.iloc[i][['Countries','Cities','Date','Persons']], #, icon=icon, # ,'Cities','Date','Persons'
      icon=folium.features.CustomIcon('5k_flag.png',icon_size=(20,20)),
      tooltip=data.iloc[i]['Countries']
   ).add_to(m)

def color_code(value):
    match_b = re.search(r'영국', value)
    match_c = re.search(r'독일', value)
    
    if match_b:
        color = 'red'
    elif match_c:
        color = 'yellow'
    else:
        color='white'
    print (color)
    return f'background-color: {color}'

df = pd.read_csv("my5k_countries.csv", encoding='CP949')
df.replace(np.nan, value = "", inplace = True)

res=df.style.applymap(color_code, subset=[df.columns[1]])

st.dataframe(df)
st_data = st_folium(m, width=1500)
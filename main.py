import pandas as pd
import requests
import streamlit as st
import urllib
import folium

st.title('国土地理院APIを用いて住所から緯度経度に変換するアプリです')
st.subheader('foliumライブラリを用い地図に表示します')
"""国土地理院APIを用いて住所から緯度経度に変換する"""
st.text('環境')
# 国土地理院API
GeospatialUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="

# データフレーム作成
df = pd.read_csv('./sample_address.csv')
print(pd)
st.text('テキスト')

st.caption('キャプション')

# 国土地理院APIより住所→緯度経度に変換
lat_list = []
lng_list = []
for index, row in df.iterrows():
    s_quote = urllib.parse.quote(row.住所)
    response = requests.get(GeospatialUrl + s_quote)
    try:
        lat_list.append(response.json()[0]["geometry"]["coordinates"][1])
        lng_list.append(response.json()[0]["geometry"]["coordinates"][0])
    except Exception as e:
        print(e)

# inputデータに緯度経度を追加する
df_new = df.copy()
try:
    df_new['lat'] = lat_list
    df_new['lng'] = lng_list
except Exception as e:
    print(e)

# csvに結果を保存する
df_new.to_csv('./result_add2latlng.csv', encoding='UTF-8', index=False)


# 観光地をmapに描画する
m = folium.Map(location=[df_new[0:1].lat, df_new[0:1].lng], tiles='OpenStreetMap', zoom_start=10)
for i, marker in df_new.iterrows():
    name='Location:'+str(i)
    lat = marker.lat
    lon = marker.lng
    popup ="<strong>{0}</strong><br>Lat:{1:.3f}<br>Long:{2:.3f}".format(name, lat, lon)
    folium.Marker(location=[lat, lon], popup=popup, icon=folium.Icon(color='lightgreen')).add_to(m)

# HTML出力
m.save('./mapping' + '.html')

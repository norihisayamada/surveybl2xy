import  os
import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as stc
import urllib
import urllib.request
import folium
from io import StringIO

st.title('国土地理院APIを用いて住所から緯度経度に変換するアプリです')
st.header('住所の緯度経度を地図に表示します')

st.subheader('開発環境')
# st.text('テキスト')
# st.caption('キャプション')

# 国土地理院API
GeospatialUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="

# データフレーム作成/ファイルの読み込み
df = pd.read_csv('./sample_address.csv')
# upload_file = st.file_uploader('ファイルのアップロード', type=['csv'])
# df = pd.read_csv(upload_file)
# st.caption('キャプション')
st.text('元のデータ（UAV関係会社住所)')
"""国土地理院APIを用いて住所から緯度経度に変換する"""
st.write(df)


# 国土地理院APIより住所→緯度経度に変換
lat_list = []
lng_list = []
for index, row in df.iterrows():
    s_quote = urllib.parse.quote(row.住所)
    response = requests.get(GeospatialUrl + s_quote)
    # print(response.json()[0])
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

#パスの操作
st.text("パスの操作")
"""
https://www.sejuku.net/blog/63651
"""
print(os.getcwd())
path = "C:\\Users\sus44\PycharmProjects\surveybl2xy\mapping.html"
print(path)
ospath = os.path.basename(path)
print(ospath)



st.text("urllib.requestモジュールによるWebページの取得")
"""
https://atmarkit.itmedia.co.jp/ait/articles/1910/15/news018.html
"""
# res = requests.get('https://www.example.com/')
# print(res)
# response = urllib.request.urlopen('https://www.example.com/')
# print('url:', response.geturl())
# print('code:', response.getcode())
# print('Content-Type:', response.info()['Content-Type'])
# content = response.read()
# print(content)
# response.close()
#
# html = content.decode()
# print(html)
st.text("HTMLファイルからデータの取得(read)")
"""
https://www.teamxeppet.com/python-lxml-1/
"""
# import glob
from lxml import html
#
# for file in glob.glob(r"C:\Users\sus44\PycharmProjects\surveybl2xy\mapping.html"):
#     with open(file, mode='rb') as g:
#         t = html.fromstring(g.read())
#         text = t.text_content().strip()
#         print(text)

st.write('地図に表示しますか？')
if st.button('開始'):
    'mapping...'
    ospath

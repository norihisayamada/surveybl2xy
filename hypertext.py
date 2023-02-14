import  streamlit as st
import  streamlit.components.v1 as stc
import urllib

st.write('地図に表示しますか？')
#
# html_pd = pd.read_html('test.html')
# print(html_pd)

if st.button('開始'):
    'mapping...'
    # html_pd = stc.html('mapping.html')
    # print(html_pd)
    # html_pd =stc.html(html_pd)
    stc.iframe('mapping.html', width=None, height=None, scrolling=False)



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
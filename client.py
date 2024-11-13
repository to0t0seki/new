import requests

url = 'https://p9f4y2amctfjgzh4idrckr.streamlit.app/get_data'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"aaの値: {data['aa']}")
else:
    print(f"データの取得に失敗しました。ステータスコード: {response.status_code}")
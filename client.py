import requests

url = 'https://p9f4y2amctfjgzh4idrckr.streamlit.app/'
response = requests.get(url)

print(response.json)
from fastapi import FastAPI
from pydantic import BaseModel
import streamlit as st

app = FastAPI()

class Data(BaseModel):
    aa: int

@app.get("/get_data", response_model=Data)
def get_data():
    aa = 1
    print("Hello World")  # サーバーのコンソールに出力されます
    return Data(aa=aa)

st.write("Hello World")
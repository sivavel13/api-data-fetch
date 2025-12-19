import requests
import pandas as pd

url="https://fakestoreapi.com/products"
r=requests.get(url).json()
df=pd.json_normalize(r)
df=df.dropna()
df.to_csv("api_products_clean.csv", index=False)
print("Fetched and cleaned:", df.shape)

import pickle
import pandas as pd
from pprint import pprint
from collections import ChainMap

import meilisearch

import requests

from st_keyup import st_keyup

import streamlit as st


client = meilisearch.Client("http://meili:7700")

index = client.index("anime")


for i in range(1, 11):
    with open(f"data/result-{i}.pkl", "rb") as f:
        document = pickle.load(f)[0]

    for doc in document:
        doc["キャスト"] = [{key: value} for key, value in doc["キャスト"].items()]
    index.add_documents(document)


# MeiliSearchのエンドポイント
MEILI_SEARCH_URL = "http://meili:7700/indexes/anime/search"

st.title("Anime Search")

# 検索ボックス
search_query = st_keyup("Enter a search queey:")

# 検索クエリが入力されたら検索を実行
if search_query:
    response = requests.post(MEILI_SEARCH_URL, json={"q": search_query})
    results = response.json()

    pprint(results)

    st.write(len(results), "animes found")

    # 検索結果を表示
    for anime in results["hits"]:
        st.subheader(anime["タイトル"])
        casts = anime["キャスト"]
        _ = anime.pop("キャスト")
        st.write("アニメ:", anime)
        with st.expander("キャスト"):
            st.dataframe(pd.Series(dict(ChainMap(*casts[::-1])), name="声優"))

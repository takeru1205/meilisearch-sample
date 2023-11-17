import json
import pickle
import meilisearch

client = meilisearch.Client("http://meili:7700")

index = client.index("anime")


for i in range(1, 11):
    with open(f"data/result-{i}.pkl", "rb") as f:
        document = pickle.load(f)[0]

    for doc in document:
        doc["キャスト"] = [
            {"name": key, "role": value} for key, value in doc["キャスト"].items()
        ]

    index.add_documents(document)

print(index.search("WILD"))

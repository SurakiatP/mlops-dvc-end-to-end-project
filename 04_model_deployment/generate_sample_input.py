import pandas as pd
import json
import os

df = pd.read_csv("../data/features.csv")
if "target" in df.columns:
    df = df.drop(columns=["target"])

sample = df.iloc[0].tolist()
input_json = {"data": [sample]}

output_path = "sample_input.json"
with open(output_path, "w") as f:
    json.dump(input_json, f, indent=4)

print(f" Sample input saved to {output_path}")
print(json.dumps(input_json, indent=4))

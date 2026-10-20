import json

data={"name": "Sara", "skills": ["Python", "SQL"]}

with open("data.json","w", encoding="utf-8")as f:
    json.dump(data, f , ensure_ascii=False, indent=2)

with open("data.json" , "r", encoding="utf-8") as f:
    loaded= json.load(f)

print(loaded["skills"][0]) 
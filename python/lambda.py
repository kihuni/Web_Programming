people = [
    {"name": "stephen", "house":"num10"},
    {"name": "kamau", "house":"num11"}
]

people.sort(key=lambda people:people["name"]) 

print(people)
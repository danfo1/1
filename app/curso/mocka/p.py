import json

with open("C:/Users/dsforero/Desktop/app/curso/mocka/m.json") as json_file:
    data = json.load(json_file)

print(json.dumps(data, indent=2, sort_keys=True))

for x in data:
    if x["genero"] == 'Mystery|Thriller':
        print(x['titulo'])

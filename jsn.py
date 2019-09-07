import json

cat = {"age":"1", "color":"black"}


result = json.dumps(cat)

result2 = json.loads(result)

print(type(result2))
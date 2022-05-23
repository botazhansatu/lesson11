from pprint import pprint
act={"city": "Москва", "temperature": "20"}


pprint(act)
print(act.get("product", "Russia"))

act["country"]="Russia"
act["date"]="27.05.2019"
print(len(act))
users = {
    "id": 1,
    "name": "Leanne Graham",
    "user name": "Bret",
    "email": "Sincere@april.biz",
    "addres":{
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}
print(users)
print(users["id"])
print(users["name"])
print(users["user name"])
print(users["email"])
print(users["addres"]["geo"]["lat"])

print(users)
print(type(users))
print("\nubah dict ke json\n")

import json
result = json.dumps(users)
print(type(result))
print(result)

with open('result.jason', 'w') as file:
    json.dump(result,file)
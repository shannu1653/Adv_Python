import requests
import json

url="https://api.api-ninjas.com/v1/dogs?name=golden retriever"
head={
     'X-Api-Key':'/aqmL87zeFVweUbzfcFhMw==VXjY3Za8tdHVajwn'}

#1.how to get all data
# dog_data=requests.get(url,headers=head)
# print(dog_data.json())


#2.add data
new_product={
          "title": "Wireless Mouse",
        "price": 499,
        "description": "A smooth wireless mouse with long battery life",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
     }
response=requests.post(url,json=new_product)
print(response)

import requests
import json


BASE = "https://crudcrud.com/api/2162dd25bba1448f8fb499d089423153"
resource = "Std_data"
url = f"{BASE}/{resource}"



#crud operations get,post,put/patch,delete


#1.get data
# data=requests.get(url)
# print(data.json())
# print(type(data))
# print(type(data.json()))



#2.post data

movies={
    'baahubali' :'600'
}


# j_m=json.dumps(movies)
post=requests.post(url,json=movies)
print(post.json())
# print(type(j_m))  #json formated is nothing but string formatted
# print(type(movies))
# j_m=json.loads(j_m)  ##ut loads converts to string to dictionary
# print(type(j_m)) 

#.json() we convert response to programming launguge

#json.stringfy --> using dumps
#jsom=n.parese --> usinf=g loads



#api-->Application programmig interface
#request module-->to communicate with server
#url(unifom resource locatot)/end point/api
import requests
import json
#HTTP methods:hyper text transfer protocol/secure
#http methods--> 1.POST    2.GET         3.UPDATION(put/patch)    4.DELETE 
# CRUD-          CREATE    READ/RETRIVE   UPDATE        DELETE

#http response code
#5 types
#200





url="https://fakestoreapi.com"

#put--replaces entire dictionary
#patch--replace specific key value

# url='https://fakestoreapi.com/products'                      
# data=requests.get(url)
# print(data.json())
# for i in data.json():
#     print(i['title'])
# #api --only in json formated

# 🧾 2️ READ (GET) — Fetch Data
# 1.1 Get all products

def get_all_products():
    response=requests.get(f"{url}/products")
    if response.status_code==200:
        data=response.json()
        for i in data:
           print(i)
    else:
        print("Error:",response.status_code)
# get_all_products()


#1.2 Get product by ID
def get_product(product_id):
        response = requests.get(f"{url}/products/{product_id}")
        if response.status_code == 200:
                print(response.json())
        else:
            print(f'product not found')


# 3️ CREATE (POST) — Add New Product
def create_product():
    new_product={
          "title": "Wireless Mouse",
        "price": 499,
        "description": "A smooth wireless mouse with long battery life",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
     }
    response=requests.post(f"{url}/products",json=new_product)
    if response.status_code == 200 or response.status_code == 201:
        print("Product created successfully!")
        print(response)
    else:
        print("Error:", response.status_code)
# create_product()
# get_all_products()
# Example usage
# get_all_products()
# get_product("20")
# create_product()

#  4️ UPDATE (PUT) — Modify Existing Product
def update_product(product_id):
    updated_data={
          'title':'Updated Wireless Mouse',
          'price':100000
    }
    response=requests.patch(f"{url}/products/{product_id}",json=updated_data)
    if response.status_code==200:
         print("product updated successfully")
         print(response.json())
    else:
         print('Error:',response.status_code)

# 5️ DELETE (DELETE) — Remove a Product
def delete_product(product_id):
    response = requests.delete(f"{url}/products/{product_id}")
    if response.status_code == 200:
        print("Product deleted successfully!")
        return response.json()
    else:
        print("Error:", response.status_code)






# update_product(1)
# create_product()
# get_all_products()
# get_product(1)

def start():
        print("All Products:")
        print(get_all_products())

        print("\nSingle Product:")
        print(get_product(1))

        print("\nCreate Product:")
        print(create_product())

        print("\nUpdate Product:")
        print(update_product(1))

        print("\nDelete Product:")
        print(delete_product(1))
        print(get_all_products())
# start()
#authentication--who are you ,it checks the identity
#autherization--> what you can do ,it gives permision
# new_product={
#           "title": "Wireless Mouse",
#         "price": 499,
#         "description": "A smooth wireless mouse with long battery life",
#         "image": "https://i.pravatar.cc",
#         "category": "electronics"
#      }
    
url="https://api.api-ninjas.com/v1/dogs?name=golden retriever"
head={
     'X-Api-Key':'/aqmL87zeFVweUbzfcFhMw==VXjY3Za8tdHVajwn'}

#response=requests.post(url,json=new_product)
dog_data=requests.get(url,headers=head)
# print(dog_data.json())

#info datails--->data transefer to to request
#data=request body

# response=requests.post(f"{url}",json=new_product,headers=head)
# if response.status_code == 200 or response.status_code == 201:
#     print("Product created successfully!")
#     print(response.json())
# else:
#     print("Error:", response.status_code)
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
print(GREEN)
# print(RED)
# print(YELLOW)
# print(CYAN)
# print(RESET)

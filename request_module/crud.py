import requests
import json
BASE = "https://crudcrud.com/api/b65db85c9ea349b083c7a7295d32349f"
resource = "Std_data"
url = f"{BASE}/{resource}"


# 1.//post data
student_data={
    'id':1,
    'name1':'shanmukha',
    'batch1':'53R',
    'Phno':'8096085857',
    'Role1':'Python full stack Developer'
}
post=requests.post(url,json=student_data)
print("Status:", post.status_code)
print("Response:", post.json())



#2.get data
response = requests.get(url)
data = response.json()
print("Total records:", len(data))
print(data)





#1/get data
# print(json.dumps(data.json(), indent=4))
# print(data=json.dumps(get.json(), indent=4))
# for i in data:
#     print(i)


def get_product(product_id):
        response = requests.get(f"{url}/{product_id}")
        if response.status_code == 200:
                print(response.json())
        else:
            print(f'product not found')
#get_product("6901b11e7037b603e8a5b783")


def update_product(product_id):
    # Must include ALL fields (old + updated)
    updated_data = {
        'id': 1,
        'name1': 'Updated Wireless Mouse',
        'batch1': '53R',
        'Phno': '100000',
        'Role1': 'Python full stack Developer'
    }

    response = requests.put(f"{url}/{product_id}", json=updated_data)
    if response.status_code == 200:
        print("Product updated successfully")
    else:
        print("Error:", response.status_code, response.text)

# Update record
# update_product('6901b11e7037b603e8a5b783')

# Fetch latest data


#delate latest data
def delete_product(product_id):
    response = requests.delete(f"{url}/{product_id}")
    if response.status_code in [200, 204]:
        print("Product deleted successfully!")
    else:
        print("Error:", response.status_code)

# Check all records first
data = requests.get(url).json()
# print("Before delete:", len(data))
# print(data)

# Delete
# delete_product("6901afad7037b603e8a5b781")

# Confirm deletion
data = requests.get(url).json()
# print("After delete:", len(data))






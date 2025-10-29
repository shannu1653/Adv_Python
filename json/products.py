import json
# data={'name':'shannu','age':27,'place':'vishakhapatnam','course':'python developer'}
# op=json.dumps(data)
# print(type(op))

# data=['shannu','tharun','naveen','sathish']
# op=json.dumps(data)
# print(op)
# print(type(op))
# print(op[3])
# op1=json.loads(op)
# print(op1)
# print(op1[3])
# print(type(op1))

list=['shannu2321','tharun','sathish','naveen']

# to insert into json file

# data_json=json.dumps(list)
# data_json=json.dumps(list)
# with open('products.json','w') as f:
#     f.write(data_json)


#to read json file
# with open('products.json','r') as f:
#     res=f.read()
#     data_json=json.loads(res)
#     print(data_json)

#to convert and insert into file with single step using ----->dump
# with open('products.json','w') as f:
#     json.dump(list,f)


#to convert json to string and aslo read by using ---->load
# with open('products.json','r') as f:
#     data=json.load(f)
#     print(data[0])




#append an alement to dictionary
# list=['shannu2321','tharun','sathish','naveen']
# ip='hemanth'
# with open('products.json','r') as f:
#     data=json.load(f)
#     if ip not in data['friuts']:
#        data["friuts"].append(ip)
#     else:
#         print(f'{ip} is alredy exist')
# with open('products.json' ,'w') as f:
#     json.dump(data,f)
#     print('data succefully inserted')

# # #remove an element in a list of dictionary
# remove_element='tharun'
# with open('products.json','r') as f:
#     data=json.load(f)
#     if remove_element not in data["friuts"]:
#         print(f"{remove_element} is not available in the list")
#     else:
#         data["friuts"].remove(remove_element)
# with open('products.json','w') as f:
#     json.dump(data,f)
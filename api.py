import requests,os
api="https://fakestoreapi.in/api/products"
data=requests.get(api)
# print(data)
products=data.json()
# print(products)

# open powershell as administrator
# set-ExecutionPolicy RemoteSigned
try:
  for i in products["products"]:
    # print(i["id"],i["title"])
      print(i["id"],i["brand"],i["model"],i["price"],i["color"])
    #   raise KeyError("Key not found")
except:
   print("Key not exists")
# except Exception as e:
#    print(e)
# finally:
#    with open("files.py",'r') as f:
#      print(f.read())
#    print("executed successfully")
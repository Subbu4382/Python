# # json server
# install node
# node --version
# npm --> node package manager
# npm install -g json-server
# json-server --watch db.json


import requests,json
api="http://localhost:3000/users"
user_data=requests.get(api)
user_data=user_data.json()
print(user_data.json())


send_data={
    "id":2,"name":"subrahmanyam",
    "id":3,"name":'good bye'
}
send_data=json.dumps(send_data) # to convert into string format
send_user=requests.post(api,data=send_data)
print(send_user.json())
print(send_user)

user_exists=False
for i in user_data:
   if i["name"]==send_data["name"]:
      user_exists=True
if user_exists==False:
   send_data=json.dumps(send_data) # to convert into string format
   send_user=requests.post(api,data=send_data)
   print(send_user.json())
else:
   print("User already exists")

api="http://localhost:3000/users/2"
# put --replaces the entire object/record with the given value

put_data={
    "id":2,"name":"subrahmanyam_dunne"
}
put_data=json.dumps(put_data)
put_user=requests.put(api,data=put_data)
print(put_user)
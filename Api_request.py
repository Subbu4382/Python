# # json server
# install node
# node --version
# npm --> node package manager
# npm install -g json-server
# json-server --watch db.json
import requests,json
api="http://localhost:3000/users"
user_data=requests.get(api)
print(user_data.json())


send_data={
    "id":2,"name":"subrahmanyam"
}
send_data=json.dumps(send_data) # to convert into string format
send_user=requests.post(api,data=send_data)
print(send_user.json())
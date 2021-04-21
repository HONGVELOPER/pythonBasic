import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import requests

# print(os)
print(os.environ['UPBIT_OPEN_API_ACCESS_KEY'])
# print(jwt)
# print(requests)

def property_lookup():

    # access_key = os.environ['dKHxEpuRbsq6hAff9aMqw4FwoSsxNi87fHhpxxxJ']
    # secret_key = os.environ['dywJtnIJvrxDyakZcHuQ3xmzgvS5WbhoRwqExRdx']
    # sever_url = os.environ['http://localhost:8000']
    access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
    secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
    server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorization_token = 'Bearer {}'.format(jwt_token)
    headers = {'Authorization': authorization_token}
    res = requests.get(server_url + '/v1/accounts', headers=headers)
    # print(res.json())

    return res.json()
    

property = property_lookup()
avg = property[2]
print(avg)
avg = avg['avg_buy_price']

print(f'도지코인 평단가 : {avg}')
# for i in property:
#     print(f'i, {i}')
# print(f'도지코인 평단가 + {property[2]['avg_buy_price']}')


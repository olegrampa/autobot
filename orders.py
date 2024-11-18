import requests
import time
import hashlib
import hmac
import uuid
from tg import tg_send_mess
from config import api, secret

def open_long_orders(api_key,
           secret_key,
           category,
           symbol,
           side,
           orderType,
           qty,
           timeInForce,
           reduceOnly):


  httpClient=requests.Session()
  recv_window=str(5000)

  url = "https://api.bybit.com"

  time_stamp=str(int(time.time() * 10 ** 3))

  def HTTP_Request(endPoint,method,payload,Info):
    signature=genSignature(payload)
    headers = {'X-BAPI-API-KEY': api_key,'X-BAPI-SIGN': signature,'X-BAPI-SIGN-TYPE': '2','X-BAPI-TIMESTAMP': time_stamp,'X-BAPI-RECV-WINDOW': recv_window,'Content-Type': 'application/json'}
    if(method=="POST"):
      response = httpClient.request(method, url+endPoint, headers=headers, data=payload)
    else:
      response = httpClient.request(method, url+endPoint+"?"+payload, headers=headers)
    
    mark = eval(response.text)
    
    if mark['retCode'] == 0:
      tg_send_mess(f"Успешный рыночный вход в направлении Long объемом {qty} по паре {symbol}")
    elif mark['retCode'] != 0:
      tg_send_mess(f"Ошибка {mark['retCode']}, комментарий: {mark['retMsg']}")

                   
    print(response.text)
    print(Info + " Elapsed Time : " + str(response.elapsed))

  def genSignature(payload):
    param_str= time_stamp + api_key + recv_window + payload
    hash = hmac.new(bytes(secret_key, "utf-8"), param_str.encode("utf-8"),hashlib.sha256)
    signature = hash.hexdigest()
    return signature


  endpoint="/v5/order/create"
  method="POST"
  if reduceOnly == False:
    params = '{"category" : "'+category+'", "symbol" : "'+symbol+'", "side" : "'+side+'", "orderType" : "'+orderType+'", "qty": "'+qty+'", "timeInForce": "'+timeInForce+'", "reduceOnly" : false, "positionIdx" : 1}'

  elif reduceOnly == True:
    params = '{"category" : "'+category+'", "symbol" : "'+symbol+'", "side" : "'+side+'", "orderType" : "'+orderType+'", "qty": "'+qty+'", "timeInForce": "'+timeInForce+'", "reduceOnly" : true, "positionIdx" : 1}'

  HTTP_Request(endpoint,method,params,"Create")



def close_long_orders(api_key,
           secret_key,
           category,
           symbol,
           side,
           orderType,
           qty,
           timeInForce,
           reduceOnly):


  httpClient=requests.Session()
  recv_window=str(5000)

  url = "https://api.bybit.com"

  time_stamp=str(int(time.time() * 10 ** 3))

  def HTTP_Request(endPoint,method,payload,Info):
    signature=genSignature(payload)
    headers = {'X-BAPI-API-KEY': api_key,'X-BAPI-SIGN': signature,'X-BAPI-SIGN-TYPE': '2','X-BAPI-TIMESTAMP': time_stamp,'X-BAPI-RECV-WINDOW': recv_window,'Content-Type': 'application/json'}
    if(method=="POST"):
      response = httpClient.request(method, url+endPoint, headers=headers, data=payload)
    else:
      response = httpClient.request(method, url+endPoint+"?"+payload, headers=headers)
    
    mark = eval(response.text)
    
    if mark['retCode'] == 0:
      tg_send_mess(f"Успешный рыночный выход из Long объемом {qty} по паре {symbol}")
    elif mark['retCode'] != 0:
      tg_send_mess(f"Ошибка {mark['retCode']}, комментарий: {mark['retMsg']}")

                   
    print(response.text)
    print(Info + " Elapsed Time : " + str(response.elapsed))

  def genSignature(payload):
    param_str= time_stamp + api_key + recv_window + payload
    hash = hmac.new(bytes(secret_key, "utf-8"), param_str.encode("utf-8"),hashlib.sha256)
    signature = hash.hexdigest()
    return signature


  endpoint="/v5/order/create"
  method="POST"
  if reduceOnly == False:
    params = '{"category" : "'+category+'", "symbol" : "'+symbol+'", "side" : "'+side+'", "orderType" : "'+orderType+'", "qty": "'+qty+'", "timeInForce": "'+timeInForce+'", "reduceOnly" : false, "positionIdx" : 1}'

  elif reduceOnly == True:
    params = '{"category" : "'+category+'", "symbol" : "'+symbol+'", "side" : "'+side+'", "orderType" : "'+orderType+'", "qty": "'+qty+'", "timeInForce": "'+timeInForce+'", "reduceOnly" : true, "positionIdx" : 1}'

  HTTP_Request(endpoint,method,params,"Create")




def open_short_orders(api_key,
           secret_key,
           category,
           symbol,
           side,
           orderType,
           qty,
           timeInForce,
           reduceOnly):


  httpClient=requests.Session()
  recv_window=str(5000)

  url = "https://api.bybit.com"

  time_stamp=str(int(time.time() * 10 ** 3))

  def HTTP_Request(endPoint,method,payload,Info):
    signature=genSignature(payload)
    headers = {'X-BAPI-API-KEY': api_key,'X-BAPI-SIGN': signature,'X-BAPI-SIGN-TYPE': '2','X-BAPI-TIMESTAMP': time_stamp,'X-BAPI-RECV-WINDOW': recv_window,'Content-Type': 'application/json'}
    if(method=="POST"):
      response = httpClient.request(method, url+endPoint, headers=headers, data=payload)
    else:
      response = httpClient.request(method, url+endPoint+"?"+payload, headers=headers)
    
    mark = eval(response.text)
    
    if mark['retCode'] == 0:
      tg_send_mess(f"Успешный рыночный вход в направлении Short объемом {qty} по паре {symbol}")
    elif mark['retCode'] != 0:
      tg_send_mess(f"Ошибка {mark['retCode']}, комментарий: {mark['retMsg']}")

                   
    print(response.text)
    print(Info + " Elapsed Time : " + str(response.elapsed))

  def genSignature(payload):
    param_str= time_stamp + api_key + recv_window + payload
    hash = hmac.new(bytes(secret_key, "utf-8"), param_str.encode("utf-8"),hashlib.sha256)
    signature = hash.hexdigest()
    return signature


  endpoint="/v5/order/create"
  method="POST"
  if reduceOnly == False:
    params = '{"category" : "'+category+'", "symbol" : "'+symbol+'", "side" : "'+side+'", "orderType" : "'+orderType+'", "qty": "'+qty+'", "timeInForce": "'+timeInForce+'", "reduceOnly" : false, "positionIdx" : 2}'

  elif reduceOnly == True:
    params = '{"category" : "'+category+'", "symbol" : "'+symbol+'", "side" : "'+side+'", "orderType" : "'+orderType+'", "qty": "'+qty+'", "timeInForce": "'+timeInForce+'", "reduceOnly" : true, "positionIdx" : 2}'

  HTTP_Request(endpoint,method,params,"Create")



def close_short_orders(api_key,
           secret_key,
           category,
           symbol,
           side,
           orderType,
           qty,
           timeInForce,
           reduceOnly):


  httpClient=requests.Session()
  recv_window=str(5000)

  url = "https://api.bybit.com"

  time_stamp=str(int(time.time() * 10 ** 3))

  def HTTP_Request(endPoint,method,payload,Info):
    signature=genSignature(payload)
    headers = {'X-BAPI-API-KEY': api_key,'X-BAPI-SIGN': signature,'X-BAPI-SIGN-TYPE': '2','X-BAPI-TIMESTAMP': time_stamp,'X-BAPI-RECV-WINDOW': recv_window,'Content-Type': 'application/json'}
    if(method=="POST"):
      response = httpClient.request(method, url+endPoint, headers=headers, data=payload)
    else:
      response = httpClient.request(method, url+endPoint+"?"+payload, headers=headers)
    
    mark = eval(response.text)
    
    if mark['retCode'] == 0:
      tg_send_mess(f"Успешный рыночный выход из Short объемом {qty} по паре {symbol}")
    elif mark['retCode'] != 0:
      tg_send_mess(f"Ошибка {mark['retCode']}, комментарий: {mark['retMsg']}")

                   
    print(response.text)
    print(Info + " Elapsed Time : " + str(response.elapsed))

  def genSignature(payload):
    param_str= time_stamp + api_key + recv_window + payload
    hash = hmac.new(bytes(secret_key, "utf-8"), param_str.encode("utf-8"),hashlib.sha256)
    signature = hash.hexdigest()
    return signature


  endpoint="/v5/order/create"
  method="POST"
  if reduceOnly == False:
    params = '{"category" : "'+category+'", "symbol" : "'+symbol+'", "side" : "'+side+'", "orderType" : "'+orderType+'", "qty": "'+qty+'", "timeInForce": "'+timeInForce+'", "reduceOnly" : false, "positionIdx" : 2}'

  elif reduceOnly == True:
    params = '{"category" : "'+category+'", "symbol" : "'+symbol+'", "side" : "'+side+'", "orderType" : "'+orderType+'", "qty": "'+qty+'", "timeInForce": "'+timeInForce+'", "reduceOnly" : true, "positionIdx" : 2}'

  HTTP_Request(endpoint,method,params,"Create")



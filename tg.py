import requests
from config import token, chat_id

# функция, которая будет отправлять сообщение в телеграмм
def tg_send_mess(bm):
  btoken = token
  bchat = chat_id
  send = 'https://api.telegram.org/bot'+btoken+'/sendMessage?chat_id='+bchat+'&text='+bm+''
  resp = requests.get(send)
  return resp.json()
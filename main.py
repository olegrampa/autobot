# импорт модулей
import json
import base64
import ast



# импорт данных и функций из файлов
from tg import tg_send_mess
from market_orders import market_



# главная функция
def run(event, context):
    
  try:

    # декодировка файла json, который приходит по веб-хуку из tradingview
    mess = base64.b64decode(event['body']).decode('utf-8')
    s = mess.replace("'", "\"")
    d = ast.literal_eval(s)
    pare = d['pare'].replace(".P", "")
    order = d['ordertype'].title()
    direct = d['direction']
    pr = d['price']
    pos = d['position']
    
    # при рыночном ордере в сообщении
    if order == 'M':

      # функция входа в рыночную позицию
      market_(direct=direct, pare=pare, pos=pos)


  except Exception as e:
    tg_send_mess(f'{e}')
    
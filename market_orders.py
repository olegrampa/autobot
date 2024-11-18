# импорт модулей, данных и функций из файлов
from config import api, secret
from tg import tg_send_mess
import requests
from orders import open_long_orders, close_long_orders, open_short_orders, close_short_orders





# функция рыночных входов
def market_(direct, pare, pos):
  
  try:

    # если это не закрытие и есть buy то входим в лонг
    if 'Close entry(s)' not in direct and 'buy' in direct:
      open_long_orders(api_key=api,
              secret_key=secret,
              category="linear",
              symbol=pare,
              side="Buy",
              orderType="Market",
              qty=pos,
              timeInForce="GTC",
              reduceOnly=False)
    
    # если это закрытие и есть sell то выходим из лонг
    elif 'Close entry(s)' in direct and 'sell'in direct:
      close_long_orders(api_key=api,
        secret_key=secret,
        category="linear",
        symbol=pare,
        side="Sell",
        orderType="Market",
        qty=pos,
        timeInForce="GTC",
        reduceOnly=True)
      

      
    # если это не закрытие и есть sell то входим в шорт
    elif 'Close entry(s)' not in direct and 'sell' in direct:
      open_short_orders(api_key=api,
              secret_key=secret,
              category="linear",
              symbol=pare,
              side="Sell",
              orderType="Market",
              qty=pos,
              timeInForce="GTC",
              reduceOnly=False)


    # если это закрытие и есть buy то выходим из шорт
    elif 'Close entry(s)' in direct and 'buy' in direct:
      close_short_orders(api_key=api,
        secret_key=secret,
        category="linear",
        symbol=pare,
        side="Buy",
        orderType="Market",
        qty=pos,
        timeInForce="GTC",
        reduceOnly=True)
    
      
  except Exception as e:
    tg_send_mess(f'{e}')


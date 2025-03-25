'''
Дан временной ряд с историей изменения стоимости акции по дням.
Необходимо выбрать день покупки и день продажи так, чтобы максимизировать профит от такой сделки,
и вернуть размер выручки.
Если невозможно провернуть сделку с профитом, то вернуть 0.

in : prices = [7,1,5,3,6,4]
out : res = 5
'''


def profitFunc(prices: list) -> int:
   if not prices:
       return 0

   max_profit = 0
   for buy_day in range(len(prices)):
       for sell_day in range(buy_day+1, len(prices)):
           profit = prices[sell_day] - prices[buy_day]
           if profit > max_profit:
               max_profit = profit

   return max_profit


prices = [7,1,5,3,6,4]
print(profitFunc(prices))
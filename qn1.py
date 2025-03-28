n = int(input())  
prices = list(map(int, input().split()))  

if n == 0:
    print(0)
else:
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

    print(max_profit)
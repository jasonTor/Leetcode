# 121. Best Time to Buy and Sell Stock

def maxProfit(prices):
    left = 0 #Buy
    right = 1 #Sell
    max_profit = 0
    while right < len(prices):
        currentProfit = prices[right] - prices[left] #our current Profit
        if prices[left] < prices[right]:
            max_profit =max(currentProfit,max_profit)
        else:
            left = right
        right += 1
    return max_profit

def maxProfit2(prices):
    if len(prices) == 1:
        return 0
    n = 0
    for i in range(1,len(prices)):
        if max(prices[i:]) - min(prices[:i]) > n:
            n = max(prices[i:]) - min(prices[:i])
    return n
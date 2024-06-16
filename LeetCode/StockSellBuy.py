# Only true in best case scenario
def maxProfit(self,prices):
    a=prices[0]
    b=0
    for i in range(0,len(prices)):
        if prices[i]<a:
            a=prices[i]
            b=i
        if a==prices[-1]:
            return 0
    c=prices[b]
    for f in range(b, len(prices)):
        if prices[f]>c:
            c=prices[f]
    return(c-a)
#More reliable option
def maxProfit(self,prices):
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

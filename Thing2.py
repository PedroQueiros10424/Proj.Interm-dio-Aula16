def vendervynils1(stock_vynis1, saldo):
    saldo += 30
    stock_vynis1 -= 1
    return saldo,stock_vynis1
def vendervynils2(stock_vynis2, saldo):
    saldo += 25
    stock_vynis2-= 1
    return saldo,stock_vynis2
def vendervynils3(stock_vynis3, saldo):
    saldo += 45
    stock_vynis3 -= 1
    return saldo,stock_vynis3

def restock(stock_vynis1,stock_vynis2,stock_vynis3):
    stock_vynis1 += 5
    stock_vynis2 += 5
    stock_vynis3 += 5
    return stock_vynis2,stock_vynis1 ,stock_vynis3


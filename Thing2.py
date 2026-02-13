def vendervynils1(stock_vynis1, saldo):
    saldo += 30
    stock_vynis1 -= 1
    return saldo, stock_vynis1
def vendervynils2(stock_vynis2, saldo):
    saldo += 25
    stock_vynis2 -= 1
    return saldo, stock_vynis2
def vendervynils3(stock_vynis3, saldo):
    saldo += 45
    stock_vynis3 -= 1
    return saldo, stock_vynis3
def vendergira(stock_gira, saldo):
    saldo += 130
    stock_gira -= 1
    return saldo, stock_gira

def restock(stock_vynis1,stock_vynis2,stock_vynis3):
    stock_vynis1 += 5
    stock_vynis2 += 5
    stock_vynis3 += 5
    return stock_vynis2,stock_vynis1 ,stock_vynis3

def trocarvynils1(stock_vynis1,stock_vynis2, saldo):
    saldo += 5
    stock_vynis1 += 1
    stock_vynis2 -=1
    return saldo, stock_vynis1,stock_vynis2

def trocarvynils1_(stock_vynis1, saldo,stock_vynis2):
    saldo += 20
    stock_vynis1 += 1
    stock_vynis2 -=1
    return saldo, stock_vynis1,stock_vynis2

def trocarvynils2(stock_vynis2, saldo,stock_vynis1):
    saldo -= 5
    stock_vynis2 -= 1
    stock_vynis1 +=1
    return saldo, stock_vynis2,stock_vynis1

def trocarvynils2_(stock_vynis2, saldo,stock_vynis3):
    saldo += 15
    stock_vynis2 -= 1
    stock_vynis3 +=1
    return saldo, stock_vynis2,stock_vynis3

def trocarvynils3(stock_vynis3, saldo,stock_vynis1):
    saldo -= 20
    stock_vynis1 -= 1
    stock_vynis3 +=1
    return saldo, stock_vynis1,stock_vynis3

def trocarvynils3_(stock_vynis3, saldo,stock_vynis2):
    saldo -= 15
    stock_vynis2 -= 1
    stock_vynis3 +=1
    return saldo, stock_vynis2,stock_vynis3
import Thing2
import time
saldo=0
stock_vynis1=5
stock_vynis2=5
stock_vynis3=5
escolha= print("Olá, bem vindo há loja!")
while escolha!=4:
    time.sleep(1.2)
    escolha = int(input("Qual categoria de Vinis deseja acessar?\n1-(os best-sellers)\n2-(Nacionais)\n3-(Os favoritos da casa\n4-Nenhum"))
    if escolha==1:
        escolha2=int(input("Temos Bad Bunny(1),Drake(2).Qual deseja?"))
        time.sleep(0.8)
        if escolha2==1:
            print("Um vinil dele custará 30 euros")
        if escolha2 == 2:
            print("Um vinil dela custará 30 euros")
            time.sleep(1.5)
        saldo, stock_vynis = Thing2.vendervynils1(stock_vynis1, saldo)

    if escolha==2:
        escolha3=int(input("Temos Quim Barreiros(1),Toy(2).Qual deseja?"))
        time.sleep(0.8)
        if escolha3==1:
            print("Um vinil dele custará 25 euros")
        if escolha3 == 2:
            print("Um vinil dele custará 25 euros")
            time.sleep(1.5)
        saldo, stock_vynis = Thing2.vendervynils2(stock_vynis2, saldo)
    if escolha==3:
        escolha4=int(input("Temos Nirvana(1),The Smashing Pupkins(2).Qual deseja?"))
        time.sleep(0.8)
        if escolha4==1:
            print("Um vinil deles custará 45 euros")
        if escolha4 == 2:
            print("Um vinil deles custará 45 euros")
            time.sleep(1.5)
        saldo, stock_vynis = Thing2.vendervynils3(stock_vynis3, saldo)
        if stock_vynis1 or stock_vynis2 or stock_vynis3==0:
            yes_no=int(input(("Já não temos mais stock, fazer restock?\nSim (1)\nNão (2)")))
            if yes_no==1:
                stock_vynis1, stock_vynis2, stock_vynis3 = Thing2.restock(stock_vynis1, stock_vynis2, stock_vynis3)
            if yes_no==2:
                break
    if escolha==4:
        print(f"O seu total deu={saldo} obrigado pela sua visita ")
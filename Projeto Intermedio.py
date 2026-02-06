import Thing2
import time
saldo=0
stock_vynis1=5
stock_vynis2=5
stock_vynis3=5
stock_gira=5
escolha= print("Olá, bem vindo há loja!")

while escolha!=5:

    time.sleep(0.9)
    escolha = int(input("Qual categoria de Vinis deseja acessar?\n1-(os best-sellers)\n2-(Nacionais)\n3-(Os favoritos da casa)\n4-Gira discos\n5-Terminar compra"))
    if escolha==1 and stock_vynis1>=1:
        escolha2=int(input("Temos Bad Bunny(1),Drake(2).Qual deseja?"))
        time.sleep(0.8)
        if escolha2==1:
            print("Um vinil dele custará 30 euros")
        if escolha2 == 2:
            print("Um vinil dele custará 30 euros")
            time.sleep(1.5)
        saldo, stock_vynis1 = Thing2.vendervynils1(stock_vynis1, saldo)
    if escolha==2 and stock_vynis2>=1:
        escolha3=int(input("Temos Quim Barreiros(1),Toy(2).Qual deseja?"))
        time.sleep(0.8)
        if escolha3==1:
            print("Um vinil dele custará 25 euros")
        if escolha3 == 2:
            print("Um vinil dele custará 25 euros")
            time.sleep(1.5)
        saldo, stock_vynis2 = Thing2.vendervynils2(stock_vynis2, saldo)
    if escolha==3 and stock_vynis3>=1:
        escolha4=int(input("Temos Nirvana(1),The Smashing Pupkins(2).Qual deseja?"))
        time.sleep(0.8)
        if escolha4==1:
            print("Um vinil deles custará 45 euros")
        if escolha4 == 2:
            print("Um vinil deles custará 45 euros")
            time.sleep(1.5)
        saldo, stock_vynis3 = Thing2.vendervynils3(stock_vynis3, saldo)
    if escolha==4 and stock_gira>=1:
        print("Isso custará 130 euros")
        saldo, stock_gira = Thing2.vendergira(stock_gira, saldo)
        if stock_gira<=0:
            print("Infelizmente não temos mais gira-discos disponíveis")

    if stock_vynis1 <= 0 or stock_vynis2 <= 0 or stock_vynis3 <= 0:
        yes_no=int(input("Já não temos mais stock, fazer restock?\nSim (1)\nNão (2)"))
        if yes_no==1:
            stock_vynis1, stock_vynis2, stock_vynis3 = Thing2.restock(stock_vynis1, stock_vynis2, stock_vynis3)


if escolha==5:
    print(f"O seu total deu:{saldo}€ obrigado pela sua visita ")
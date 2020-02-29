import numpy as np

stock_no = int(input("How many stocks are you purchasing today? "))

i=0
while(i<stock_no):
    print("---Stock details---")
    name = input("What is the name of the stock: ")
    shares = int(input("Stock Number of shares: "))
    purchase_p = float(input("What is the purchase price? "))
    selling_p = float(input("What is the selling price? "))
    broker_c = float(input("What is the Broker commission? "))
    print("")

    paid = shares*purchase_p
    paid_comm = paid*broker_c

    sold = shares*selling_p
    sold_comm = sold*broker_c

    print("---Transaction details---")
    print("Stock name: ", name)
    print("Money paid: " , paid)
    print("Commission when stock bought: ", paid_comm)
    print("Amount sold: ", sold)
    print("Commission when stock sold: ", sold_comm)
    print("Profit/Loss: ", sold - sold_comm - paid - paid_comm)
    print("")

    i+=1




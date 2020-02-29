import numpy as np
markup = 2.5
proceed = 'y'

while proceed == 'y' :
    cost = float(input("Enter the item's wholesale cost: "))
    if cost >= 0:
        print("Retail price is $", markup*cost)
    else:
        while cost < 0:
            print("ERROR: the cost cannot be negative")
            cost = float(input("Enter the correct wholesale cost: "))
        print("Retail price is $", markup*cost)
    proceed = input("Do you have another item?(Enter y for yes): ")
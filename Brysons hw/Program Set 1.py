import numpy as np

quit = 0
while(not quit==-1):
    lottery_num = np.random.randint(10,100)
    lot_first = lottery_num/10
    lot_sec = lottery_num%10

    pick = int(input("Enter a two digit number: "))
    first_dig = pick//10
    sec_dig = int(pick)%10
    print(first_dig)
    
    if(pick == -1):
        quit = -1

    elif(pick == lottery_num):
        print("Congratulations! You have won $10,000")

    elif(sec_dig*10+first_dig == lottery_num):
        print("Congratulations! You have won $3,000")

    elif(lot_first == first_dig or lot_first == sec_dig
         or lot_sec == first_dig or lot_sec == sec_dig):
        print("Congratulations! You have won $1,000")
    else:
        print("Sorry! You did not win anything!")



add = int(input("How many numbers do you want to add? "))
sum = 0

for i in range(1,add+1):
    number = float(input("Enter number " + str(i) + " : "))
    sum+=number

print("The total is", float(sum))

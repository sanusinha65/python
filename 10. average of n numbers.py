n = int(input("Enter range for average ")) 
sum = 0 #declaring 0 so we can add for loop number in every iteration 
# loop from 1 to n
for i in range(1, n + 1):
    sum += i    #adding the number 
print("Total Sum=", sum) 
average = sum / n
print("Average= ", average)
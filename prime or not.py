n = int(input("Enter a number: "))      #taking input to check the number 
if n > 1:                                #prime numbers will be greater than 1, so if n is greater than 1 then the if condition will be executed 
   for i in range(2,n):                   #it will check for the factors dividing the number 
       if n%i== 0:                        #if condition for checking if the number is divisible by its own or not 
           print(n,"is not a prime number")            #printing the output if the number is not a prime number 
           break                           #breaking the for loop as it will not check for the further digits 
   else:                                     #else condition
       print(n,"is a prime number")         #if the condition is true then it will be printed
else:                                       #if the number is less than 1 then it it not prime number 
   print(n,"is not a prime number")         #printing the output
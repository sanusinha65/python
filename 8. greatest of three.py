a= int(input("Enter The Number ")) #taking input to check the number 
b= int(input("Enter The 2nd Number ")) #taking input to check the number 
c= int(input("Enter The 3rd Number ")) #taking input to check the number 
if a>b and a>c:      #if a is greater than b and c 
    print(a, "is greater than both numbers")
else: 
    if b>a and b>c:         #if b is greater than a and c 
        print(b, "is greater than both numbers")
    elif c>a and c>b:       #if c is greater than a and b
        print(c, "is greater than both the number ")

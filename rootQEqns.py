import math

print("Format of Quadratic Equation : ax*2 + bx + c = 0")
print("Here a, b, and c are coefficient and value of 'a' cannot be not equal to zero")

ch = 'y'
while ch == 'y':
    a = int(input("Enter value of a : "))
    while a == 0:
        print("Equation becomes linear (enter non-zer0 value)")
        a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    c = int(input("Enter value of c : "))

    print("Your Equation is : ",a,"x^2 + ",b,"x + ",c," = 0")

    #Discriminant calculation
    d = (b**2) - 4*a*c

    if d == 0:
        root1 = ((-b) + math.sqrt(d))/2*a
        root2 = ((-b) - math.sqrt(d))/2*a
        print("Real and Same roots exists")
        print("Root1 = ",round(root1, 2),"and Root2 = ",round(root2, 2))
    elif d > 0:
        root1 = ((-b) + math.sqrt(d))/2*a
        root2 = ((-b) - math.sqrt(d))/2*a
        print("Real roots exists")
        print("Root1 = ",round(root1, 2),"Root2 = ",round(root2, 2))
    elif d < 0:    
        print("Imaginary roots exists")
        pd = 0 - d
        print("Root1 = (-",b,"+",round(math.sqrt(pd), 2),"i) / ",2*a)
        print("Root1 = (-",b,"-",round(math.sqrt(pd), 2),"i) / ",2*a)
    else:
        print("Some error occured")
        exit
    ch = input("'y' to continue ,any other key to exit : ")

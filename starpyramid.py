#This program takes value from user and print a pyramid pattern


n = int(input("Enter a number : "))

#upper pyramid
for i in range(0, n):
    for k in range(0, n-i-1):
        print(" ", end=" ")
    for j in range(0, i+1):
        print("* ", end="  ")
    print("")
    
#lower pyramid
for a in range(0, n-1):
    for b in range(0, a+1):
        print(" ", end=" ")
    for c in range(0, n-a-1):
        print("* ", end="  ")
    print("")
    

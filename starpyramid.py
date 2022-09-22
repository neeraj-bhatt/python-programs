#This program takes value from user and print a pattern


#upper pyramid
n = int(input("Enter a Number : "))
for i in range(0, n):
    for j in range(0, n-i-1):
        print(" ", end=" ")
    for k in range(0, 2*i+1):
        print("* ", end="")
    print("")

#lower pyramid
for o in range(0, n):
    for b in range(0, 2*n-1+o):
        print(" ", end=" ")
    for c in range(0, 2*(n-o-1)+1):
        print("* ", end="")
    print("")
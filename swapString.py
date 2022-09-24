def swapStr(str1, str2):
    nstr1 = ""
    nstr2 = ""
    n1 = len(str1)
    n2 = len(str2)
    num = n1 if n1<n2 else n2
    while 1:
        n = int(input("Enter the value (no. of character to swap) : "))
        if(n <= n1 and n <= n2):
            break
        else:
            print("\nvalue is greater than String length")
            print("Please enter a valid value (max:",num,")\n")

    #swaps n charaters
    for i in range(0, num):
        if(i<n):
            nstr1 += str2[i]
            nstr2 += str1[i]
        else:
            nstr1 += str1[i]
            nstr2 += str2[i]
    
    #add remaining characters
    if(n1 > n2):
        for i in range(num, n1):
            nstr1 += str1[i]
    elif(n2 > n1):
        for i in range(num, n2):
            nstr2 += str2[i]
    print("First string (after swap) : ", nstr1)
    print("Second string (after swap) : ", nstr2)
        

str1 = input("Enter first String : ")
str2 = input("Enter second String : ")
swapStr(str1, str2)
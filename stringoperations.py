def frequency(ustr, b):
    count = 0
    n = len(ustr)
    for i in range(0, n):
        if ustr[i] == b:
            count += 1
    print("Frequency of", b ,":", count)
    

def replace(a, b, c):
    print("Previous string is : ", a)
    n = len(a)
    nstr = ""
    for i in range(0, n):
        if(a[i] == b):
            nstr += c
        else:
            nstr += a[i]
    return nstr

def removeall(a, b):
    n = len(a)
    nstr = ""
    for i in range(0, n):
        if(a[i] != b):
            nstr += a[i]
    return nstr

def removefirst(a, b):
    n = len(a)
    nstr = ""
    flag = 0
    for i in range(0, n):
        if(a[i] == b and flag == 0):
            flag = 1
            continue
        else:
            nstr += a[i]    
    return nstr    


str = input("Enter a String : ")
ch = 'y'
while(ch == 'y' or ch == 'Y'):
    print("\nYour String : ",str)
    print("\nHere are the action you can perform in your String")
    print("--------------------------------------------------")
    print("1.frequency of a given character\n2.Replace all occurence of a given character\n3.Remove first occurence of a given character\n4.Remove all occurence of a given character\n5.Exit",end="")
    choice = int(input("\nEnter your choice : "))
    if(choice == 1):
        str1 = input("\nEnter a character : ")
        frequency(str, str1)
    elif(choice == 2):
        str1 = input("\nEnter the character you want to replace : ")
        str2 = input("Enter a new character : ")
        str = replace(str, str1, str2)
        print("New String is : ",str)
    elif(choice == 3):
        str1 = input("\nEnter a character : ")
        str = removefirst(str, str1)
        print("New String is : ", str)
    elif(choice == 4):
        str1 = input("\nEnter a character : ")
        str = removeall(str, str1)
        print("New String is : ",str)
    elif(choice == 5):
        break
    else:
        print("Invalid choice :(")
    ch = input("\nY to continue or any other key to exit : ")
print("\nThank you")
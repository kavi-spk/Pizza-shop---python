print("*********Welcome to pizza corner**************\n")
print("1 small\n2 Medium\n3 Large ")

choice=input("Enter your choice : ")

if(choice == "1"):
    print("\nSmall pizza\n\nThe cost is Rs.100")
    print("\nAdditional requirements")
    print("\n1 Only poppins\n2 Only cheese\n3 Both poppins and cheese\n4 None")

    ch = input("\nEnter your choice: ")
    cost=100

    if(ch == '1'):
        print(f"The Bill amount is {cost+10}")
    elif(ch == '2'):
        print(f"The Bill amount is {cost+5}")
    elif(ch == '3'):
        print(f"The Bill amount is {cost+15}")
    else:
        print(f"The Bill amount is {cost}")

        
if(choice == "2"):
    print(f"Medium pizza\nThe cost is Rs.200")

    print("\n1 Only poppins\n2 Only cheese\n3 Both poppins and cheese\n4 None")

    ch = input("\nEnter your choice: ")
    cost1=200

    if(ch == '1'):
        print(f"The Bill amount is {cost1+20}")
    elif(ch == '2'):
        print(f"The Bill amount is {cost1+10}")
    elif(ch == '3'):
        print(f"The Bill amount is {cost1+30}")
    else:
        print(f"The Bill amount is {cost1}")



if(choice == "3"):
    print("Large pizza\nThe cost is Rs.300")

    
    ch = input("\nEnter your choice: ")
    cost2=300

    if(ch == '1'):
        print(f"The Bill amount is {cost2+30}")
    elif(ch == '2'):
        print(f"The Bill amount is {cost2+15}")
    elif(ch == '3'):
        print(f"The Bill amount is {cost2+45}")
    else:
        print(f"\nThe Bill amount is {cost2}")
print("\nEnjoy your Pizza")
print("\n*********Thank you, Visit us again")




        

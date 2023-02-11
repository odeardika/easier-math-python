print("1. Calculator\n2. 2D Figure\n3. 3D Figure\n4. Matrix\n5. History\n6. Exit\n")
option = input("Enter your choice : ")

while True:
    if option == "1" :
        print("Calculator")
    elif option == "2":
        print("2D")
    elif option == "3":
        print("3D")
    elif option == "4":
        print("Matrix")
    elif option == "5":
        print("History")
    elif option == "6":
        exit(0)
    else:
        print("Your choice is not in the menu!")

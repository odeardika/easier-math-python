def calculator():
    head = tail = 0
    print("============================================================================")
    print("|   + -> sum           |   * -> multiplication  |   ^ -> power             |")
    print("|   - -> subtraction   |   / -> division        |   v -> root              |")
    print("|   s -> sine          |   c -> cosine          |   t -> tangent           |")
    print("|   S -> cosecant      |   C -> secan           |   T -> cotangent          |")
    print("|   % -> percent       |   l -> logarithm       |   = -> result            |")
    print("============================================================================")
    head = int(input("Input yours first number : "))
    while True:
        choice = input("Pick the math operator : ")
        if choice == "+":
            tail = int(input("Input yours second number : "))
            print(f"{head} + {tail} = {head + tail}")
            head += tail
        elif choice == "-":
            tail = int(input("Input yours second number : "))
            print(f"{head} + {tail} = {head - tail}")
            head -= tail
        elif choice == "*":
            tail = int(input("Input yours second number : "))
            print(f"{head} + {tail} = {head * tail}")
            head *= tail
        elif choice == "/":
            tail = int(input("Input yours second number : "))
            print(f"{head} + {tail} = {head / tail}")
            head /= tail
        elif choice == "^":
            pass
        elif choice == "V":
            pass
        elif choice == "s":
            pass
        elif choice == "S":
            pass
        elif choice == "c":
            pass
        elif choice == "C":
            pass
        elif choice == "t":
            pass
        elif choice == "T":
            pass
        elif choice == "%":
            pass
        elif choice == "L":
            pass
        elif choice == "=":
            break
        else:
            print("Your choice is not in the menu!")



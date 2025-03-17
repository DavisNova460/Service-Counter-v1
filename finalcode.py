print("welcome to Automotive and Repair, WACTC")
print()

# Get the user's name
name = input("Welcome! Can I have your name before we get started: ")
print(f"Thanks, {name}. Here are our services and prices:")
print()

# Display services and prices
print("1. Oil Change and Tire Rotation")
print("\t$79.99 for oil and filter change")
print("\t$30.00 for standard tires")
print("\t$45.00 for 4WD or truck tires")
print()
print("2. Brake Pads and Front End Alignment")
print("\t$120 for the package")
print()
print("3. Broken Glass Repair")
print("\t$69.99 for a large window")
print("\t$39.99 for a small window")
print()
print("4. Dent Removal")
print("\t$5 per small dent")
print("\t$15 per large dent")
print()


# Loop until the user selects a valid service
valid_service = False
while not valid_service:
    service_choice = input("Which service do you need today? Please choose the number: ")
    print()
    if service_choice == "1":
        print("You selected Oil Change and Tire Rotation.")
        valid_service = True

        # Sub-loop for price selection
        while True:
            print("Options:")
            print("\t1. $79.99 for oil and filter change")
            print("\t2. $30.00 for standard tires")
            print("\t3. $45.00 for 4WD or truck tires")
            price_choice = input("Please choose the option number: ")
            if price_choice in ["1", "2", "3"]:
                if price_choice == "1":
                    print("You selected: $79.99 for oil and filter change.")
                elif price_choice == "2":
                    print("You selected: $30.00 for standard tires.")
                elif price_choice == "3":
                    print("You selected: $45.00 for 4WD or truck tires.")
                break
            else:
                print("Invalid option. Please choose again.")

    elif service_choice == "2":
        print("You selected Brake Pads and Front End Alignment.")
        print("The price is $120 for the package.")
        valid_service = True
    elif service_choice == "3":
        print("You selected Broken Glass Repair.")
        valid_service = True

        # Sub-loop for price selection
        while True:
            print("Options:")
            print("\t1. $69.99 for a large window")
            print("\t2. $39.99 for a small window")
            price_choice = input("Please choose the option number: ")
            if price_choice in ["1", "2"]:
                if price_choice == "1":
                    print("You selected: $69.99 for a large window.")
                elif price_choice == "2":
                    print("You selected: $39.99 for a small window.")
                break
            else:
                print("Invalid option. Please choose again.")

    elif service_choice == "4":
        print("You selected Dent Removal.")
        valid_service = True

        # Sub-loop for price selection
        while True:
            print("Options:")
            print("\t1. $5 per small dent")
            print("\t2. $15 per large dent")
            price_choice = input("Please choose the option number: ")
            if price_choice in ["1", "2"]:
                if price_choice == "1":
                    print("You selected: $5 per small dent.")
                elif price_choice == "2":
                    print("You selected: $15 per large dent.")
                break
            else:
                print("Invalid option. Please choose again.")

    else:
        print("Invalid service choice. Please choose again.")

print("Thank you for choosing Automotive and Repair, WACTC!")

#Task :01
pin = "4521"
while True:
    user_pin = input("Enter PIN: ")
    if user_pin == pin:
        print("Access Granted!")
        break
    elif user_pin == "cancel":
        print("Transaction Cancelled.")
        break
    else:
        print("Incorrect pin,.")

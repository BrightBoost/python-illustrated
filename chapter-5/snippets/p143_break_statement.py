for number in range(1, 10):
    if number == 5:
        print("Number 5 found! Exiting loop.")
        break
    print("Current number:", number)
print("The loop has ended.")



while True:
    text = input("Do you want to stop? " )
    if(text == "yes"):
        break
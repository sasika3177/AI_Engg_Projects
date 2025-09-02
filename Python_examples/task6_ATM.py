withdraw=int(input("Enter withdraw amount"))
if(withdraw%100==0):
    print(f"Dispensing {withdraw}")
else:
    print("Invalid amount")
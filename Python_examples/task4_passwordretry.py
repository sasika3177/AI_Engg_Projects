password = "openAI123"

for i in range(3):
    entered_password = input("Enter password: ")
    if entered_password == password:
        print("Login successful")
        break
    else:
        print(f"Attempt failed:{i+1} password Wrong..Try Again,,,chances left:{i+2}")
else:
    print("Account Locked")

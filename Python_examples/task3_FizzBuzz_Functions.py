def fizzbuzz(n):
    for i in range(1,n+1):
        if(i<=n):
            if(i%3==0) and (i%5==0):
                print("FizzBuzz")
            elif(i%3==0):
                print("Fizz")
            elif(i%5==0):
                print("Buzz")
            else:
                print(f"{i}")
            

input1=int(input("Enter the input: "))
fizzbuzz(input1)
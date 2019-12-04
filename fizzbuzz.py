for i in range(1, 101): 
    fizz = i%3 == 0
    buzz = i%5 == 0
    if fizz and buzz: 
       print("FizzBuzz")
    else:
        if buzz:
            print("Buzz")
        else:
            if fizz: 
                print("Fizz")
            else:
                print(i)
def fizz_buzz():
    value = range(1, 101)
    for n in value:
        if n % 3 == 0 and n % 5 == 0 :
         print("FizzBuzz")
        elif n % 3 == 0: 
         print("Fizz")
        elif n % 5 == 0 :
            print("Buzz")
        else: 
         print(n)

fizz_buzz()

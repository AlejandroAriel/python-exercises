def number_of_bottles():
   
    value = range(99,-1,-1)
    count = 99
    for n in value:
        if n == 1:
            print("1 bottle of milk on the wall, 1 bottle of milk. \nTake one down and pass it around, no more bottles of milk on the wall.")
        elif n == 0:
            print("No more bottles of milk on the wall, no more bottles of milk. \nGo to the store and buy some more, 99 bottles of milk on the wall.")
        else:
            print(str(count) +" bottles of milk on the wall, " + str(count) +" bottles of milk. \nTake one down and pass it around, " + str(count - 1) + " bottles of milk on the wall.")
            count -= 1
  
number_of_bottles()
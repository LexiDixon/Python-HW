
'''You work for a bakery that sells two items: muffins and cupcakes. The number of muffins and cupcakes in your shop at any given time is stored in the
variables muffins and cupcakes which you will define, and the store has 10 muffins and 10 cupcakes.  Write a program that takes strings from standard
input indicating what your customers are buying ("muffin" for a muffin, "cupcake" for a cupcake). If they buy a muffin, decrease muffins by one,
and if they buy a cupcake, decrease cupcakes by 1. If there is no more of that baked good left, print ("Out of stock").
Once you are done selling, input "0", and have the program print out the number of muffins and cupcakes remaining, in the form "muffins: 9 cupcakes: 3"
(if there were 9 muffins and 3 cupcakes left, for example).
'''
#CODE WORKS
buying = input('do you want muffins or cupcakes?')
muffins = 10
cupcakes = 10

while buying != "0":
    if buying == "muffins" and muffins > 0:
            muffins = muffins -1
            if buying == "muffins" and muffins == 0:
                      print("muffins Out of Stock")
    
              
    if buying == "cupcakes" and cupcakes > 0:
            cupcakes = cupcakes -1
            if buying == "cupcakes" and cupcakes == 0:
                    print("cupcakes Out of Stock")
                
    buying = input('Do you want muffins or cupcakes?')

print("muffins:", muffins, "cupcakes:", cupcakes)

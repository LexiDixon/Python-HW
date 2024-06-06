import math

pizzaslices = 8
family = 4
Mom = int(input("how many slices of pizza does Mom eat "))
Dad = int(input("how many slices of pizza does Dad eat "))
Bob = int(input("how many slices of pizza does Bob eat "))
Tim = int(input("how many slices of pizza does Tim eat "))
totalslices = Mom+Dad+Bob+Tim
print(totalslices)
wholepizza = math.ceil(totalslices/pizzaslices)
print("whole pizza to order", wholepizza)

leftbymodulo = totalslices%pizzaslices
print(leftbymodulo)

print("Total number of pizzas to buy", wholepizza)
print("total slices left", leftbymodulo)

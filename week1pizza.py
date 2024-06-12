import math

pizzaslices = 8
family = 4

eat = int(input("how many slices of pizza does the family eat " ))
totalslices = eat*family
print(totalslices)

wholepizza = math.ceil(totalslices/pizzaslices)
print("whole pizza to order", wholepizza)

leftbymodulo = totalslices%pizzaslices
print(leftbymodulo)

print("Total number of pizzas to buy", wholepizza)
print("total slices left", leftbymodulo)


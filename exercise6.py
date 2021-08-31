# In this section you will find Functions Exercises in Python.
#
# Try these exercises on your own, and the checkout the solutions.
#
# Learn about functions in here.
#
# Exercise 1: From given list
#
# gadgets = [“Mobile”, “Laptop”, 100, “Camera”, 310.28,
#
# “Speakers”, 27.00, “Television”, 1000, “Laptop Case”, “Camera Lens”]
#
# a) Calculate the total price of the all the gadgets.
#
# b) Calculate the average of all the gadgets.

gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case",
           "Camera Lens"]

# for item in gadgets:
#     if isinstance(item, int) or isinstance(item, float):
#         numItems.append(item)

numItems = [item for item in gadgets if isinstance(item, int) or isinstance(item, float)]

sumOfNumItems = sum(numItems)
print(sumOfNumItems)
print(sumOfNumItems / len(numItems))

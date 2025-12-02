# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.
weather = int(input("What is the temperature outside today? "))
# Prints whether it’s cold, warm, or hot using comparison operators.
if weather > -10 and weather <= 45:
    print("Its cold outside. Wear a Sweater or Jacket.")
elif weather > 45 and weather <= 80:
    print("Its warm. It may be a bit windy so you might have to wear a little sweater.")
elif weather > 80 and weather < 110:
    print("Its hot. Beware of the sun. BEACH TIME.")
else:
    print("Extreme temperature warning!")
# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:


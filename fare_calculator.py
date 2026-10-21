# Travel Fare Calculator
FARE_RATE = 14

# 1. Passenger name -- Must not be empty
while True:
    name = input("Enter passenger name: ")
    if name.strip() != "":
        break
    print("Error: Name cannot be empty. Please try again.")

# 2. Distance -- Number greater than 0
while True:
    try:
        distance = float(input("Enter distance (km): "))
        if distance > 0:
            break
        print("Error: Distance must be greater than 0.")
    except ValueError:
        print("Error: Please enter a valid number.")

# 3. Passengers -- Positive whole number
while True:
    try:
        passengers = int(input("Enter number of passengers: "))
        if passengers > 0:
            break
        print("Error: Number of passengers must be at least 1.")
    except ValueError:
        print("Error: Please enter a valid whole number.")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

#fairsbradar

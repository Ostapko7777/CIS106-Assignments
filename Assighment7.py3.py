# Problem 3 – trips, mpg and gas cost

def comp_trip(miles, gallons):
    mpg = miles / gallons
    gas_cost = gallons * 3.00
    return mpg, gas_cost


trip_count = 0
total_miles = 0.0
total_gas_cost = 0.0

response = input("Do you want to enter a trip? Enter Yes or No: ")

while response.lower() == "yes":
    city = input("Enter destination city: ")
    miles = float(input("Enter miles travelled: "))
    gallons = float(input("Enter gallons used: "))

    mpg, gas_cost = comp_trip(miles, gallons)

    print(f"City: {city}, Miles: {miles:.1f}, MPG: {mpg:.2f}, Gas cost: ${gas_cost:.2f}")

    trip_count += 1
    total_miles += miles
    total_gas_cost += gas_cost

    response = input("Do you want to enter another trip? Enter Yes or No: ")

print("Number of trips:", trip_count)
print(f"Total miles: {total_miles:.1f}")
print(f"Total gas cost: ${total_gas_cost:.2f}")

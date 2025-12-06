# Problem 5 – tuition owed

def comp_tuition(credits, dist_code):
    dist_code = dist_code.upper()

    if dist_code == "I":
        rate = 250.0
    elif dist_code == "O":
        rate = 550.0
    else:
        rate = 0.0

    tuition = credits * rate
    return tuition


total_tuition = 0.0

response = input("Do you want to enter a student? Enter Yes or No: ")

while response.lower() == "yes":
    last_name = input("Enter student last name: ")
    credits = float(input("Enter credit hours: "))
    dist_code = input("Enter district code (I or O): ")

    tuition = comp_tuition(credits, dist_code)

    print(f"Student: {last_name}, Tuition owed: ${tuition:.2f}")

    total_tuition += tuition
    response = input("Do you want to enter another student? Enter Yes or No: ")

print(f"Total tuition owed: ${total_tuition:.2f}")

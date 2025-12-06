# Problem 4 – employee pay with job code and overtime

def comp_pay(job_code, hours):
    job_code = job_code.upper()

    if job_code == "L":
        rate = 25.0
    elif job_code == "A":
        rate = 30.0
    elif job_code == "J":
        rate = 50.0
    else:
        # default rate if code is unknown
        rate = 0.0

    if hours > 40:
        regular = 40 * rate
        ot_hours = hours - 40
        ot_pay = ot_hours * rate * 1.5
        gross = regular + ot_pay
    else:
        gross = hours * rate

    return rate, gross


total_gross = 0.0

response = input("Do you want to enter an employee? Enter Yes or No: ")

while response.lower() == "yes":
    last_name = input("Enter employee last name: ")
    job_code = input("Enter job code (L, A, J): ")
    hours = float(input("Enter hours worked: "))

    rate, gross = comp_pay(job_code, hours)

    print(f"Employee: {last_name}, Hours: {hours:.2f}, Rate: ${rate:.2f}, Gross pay: ${gross:.2f}")

    total_gross += gross
    response = input("Do you want to enter another employee? Enter Yes or No: ")

print(f"Total gross pay for all employees: ${total_gross:.2f}")

# Part 1 - Employee and Manager Classes

class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def bonus(self):
        return self.annual_salary * 0.10


class Manager(Employee):
    def bonus(self):
        return self.annual_salary * 0.20

    def long_term_bonus(self):
        return self.annual_salary * 0.50


# ----- Test the classes -----
emp = Employee("John", "Smith", 60000)
print("Employee:", emp.first_name, emp.last_name)
print("Salary:", emp.annual_salary)
print("Bonus:", emp.bonus())

print()

mgr = Manager("Sarah", "Johnson", 90000)
print("Manager:", mgr.first_name, mgr.last_name)
print("Salary:", mgr.annual_salary)
print("Bonus:", mgr.bonus())
print("Long Term Bonus:", mgr.long_term_bonus())

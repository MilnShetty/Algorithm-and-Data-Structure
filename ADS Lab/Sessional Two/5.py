class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

def insert_employee_to_hash_table(hash_table, employee):
    age = employee.age
    if age in hash_table:
        hash_table[age].append(employee)
    else:
        hash_table[age] = [employee]

def search_employee(hash_table, emp_id, age):
    if age in hash_table:
        for employee in hash_table[age]:
            if employee.emp_id == emp_id:
                return employee
    return None

def calculate_average_salary(hash_table, age_lower, age_upper):
    total_salary = 0
    num_employees = 0

    for age in range(age_lower, age_upper + 1):
        if age in hash_table:
            for employee in hash_table[age]:
                total_salary += employee.salary
                num_employees += 1

    if num_employees == 0:
        return 0
    return total_salary / num_employees

# Create an empty hash table (dictionary)
employee_hash_table = {}

# Insert N employees into the hash table (you can replace this with your preferred method of input)
employee_data = [
    (1, "John", 25, 50000.0),
    (2, "Alice", 22, 45000.0),
    (3, "Bob", 30, 60000.0),
    (4, "Eve", 21, 47000.0),
    (5, "Charlie", 26, 52000.0)
]

for emp_id, name, age, salary in employee_data:
    employee = Employee(emp_id, name, age, salary)
    insert_employee_to_hash_table(employee_hash_table, employee)

# Search for an employee by ID and age
search_id = 3
search_age = 22
found_employee = search_employee(employee_hash_table, search_id, search_age)
if found_employee:
    print(f"Employee found! Details: ID: {found_employee.emp_id}, Name: {found_employee.name}, Age: {found_employee.age}, Salary: {found_employee.salary}")
else:
    print("Employee not found.")

# Calculate the average salary of employees between ages 22 and 25
average_salary = calculate_average_salary(employee_hash_table, 22, 25)
print(f"Average salary of employees between ages 22 and 25: {average_salary}")

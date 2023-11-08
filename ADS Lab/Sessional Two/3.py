class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary
        self.left = None
        self.right = None

def insert_employee(root, employee):
    if root is None:
        return employee
    if employee.emp_id < root.emp_id:
        root.left = insert_employee(root.left, employee)
    else:
        root.right = insert_employee(root.right, employee)
    return root

def search_employee(root, emp_id):
    if root is None or root.emp_id == emp_id:
        return root
    if emp_id < root.emp_id:
        return search_employee(root.left, emp_id)
    return search_employee(root.right, emp_id)

def calculate_average_salary(root, age_lower, age_upper):
    def calculate_average(node, total_salary, num_employees):
        if node:
            if age_lower <= node.age <= age_upper:
                total_salary[0] += node.salary
                num_employees[0] += 1
            calculate_average(node.left, total_salary, num_employees)
            calculate_average(node.right, total_salary, num_employees)

    total_salary = [0]
    num_employees = [0]
    calculate_average(root, total_salary, num_employees)

    if num_employees[0] == 0:
        return 0
    return total_salary[0] / num_employees[0]

# Create an empty Binary Tree
root = None

# Insert N employees into the Binary Tree (you can replace this with your preferred method of input)
employee_data = [
    (1, "John", 25, 50000.0),
    (2, "Alice", 22, 45000.0),
    (3, "Bob", 30, 60000.0),
    (4, "Eve", 21, 47000.0),
    (5, "Charlie", 26, 52000.0)
]

for emp_id, name, age, salary in employee_data:
    employee = Employee(emp_id, name, age, salary)
    root = insert_employee(root, employee)

# Search for an employee by ID
search_id = 3
found_employee = search_employee(root, search_id)
if found_employee:
    print(f"Employee found! Details: {found_employee.name}, Age: {found_employee.age}, Salary: {found_employee.salary}")
else:
    print("Employee not found.")

# Calculate the average salary of employees between ages 20 and 25
average_salary = calculate_average_salary(root, 20, 25)
print(f"Average salary of employees between ages 20 and 25: {average_salary}")

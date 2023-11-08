class Employee:
    def __init__(self, emp_id, name, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.salary = salary
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_employee(self, emp_id, name, designation, salary):
        new_employee = Employee(emp_id, name, designation, salary)
        if self.head is None:
            self.head = new_employee
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_employee

    def search_employee(self, emp_id):
        current = self.head
        while current:
            if current.emp_id == emp_id:
                print("Employee ID:", current.emp_id)
                print("Name:", current.name)
                print("Designation:", current.designation)
                print("Salary:", current.salary)
                return
            current = current.next
        print("Employee not found!")

    def average_manager_salary(self):
        total_salary = 0
        manager_count = 0
        current = self.head
        while current:
            if current.designation == "Manager":
                total_salary += current.salary
                manager_count += 1
            current = current.next
        if manager_count > 0:
            average_salary = total_salary / manager_count
            print("Average Salary of Managers:", average_salary)
        else:
            print("No Managers in the list.")

employee_list = LinkedList()

employee_list.insert_employee(1, "John", "Manager", 60000)
employee_list.insert_employee(2, "Alice", "Developer", 50000)
employee_list.insert_employee(3, "Bob", "Manager", 70000)
employee_list.insert_employee(4, "Eve", "Manager", 75000)

employee_list.search_employee(3)

employee_list.average_manager_salary()

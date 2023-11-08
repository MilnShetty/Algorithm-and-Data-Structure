class Student:
    def __init__(self, roll_no, name, math_score, science_score):
        self.roll_no = roll_no
        self.name = name
        self.math_score = math_score
        self.science_score = science_score
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_student(self, roll_no, name, math_score, science_score):
        new_student = Student(roll_no, name, math_score, science_score)
        if self.head is None:
            self.head = new_student
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_student
            new_student.prev = current

    def search_student(self, roll_no):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                print("Student Roll No:", current.roll_no)
                print("Name:", current.name)
                print("Math Score:", current.math_score)
                print("Science Score:", current.science_score)
                return
            current = current.next
        print("Student not found!")

    def display_high_scorers(self):
        current = self.head
        while current:
            if current.math_score > 90 and current.science_score > 90:
                print("Student Roll No:", current.roll_no)
                print("Name:", current.name)
                print("Math Score:", current.math_score)
                print("Science Score:", current.science_score)
            current = current.next


student_list = DoublyLinkedList()


student_list.insert_student(1, "Alice", 95, 92)
student_list.insert_student(2, "Bob", 88, 94)
student_list.insert_student(3, "Charlie", 92, 89)


student_list.search_student(2)


print("Students with Math and Science scores above 90:")
student_list.display_high_scorers()

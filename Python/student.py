class Student:
    def __init__(self, id, name, marks):
        self.id  = id
        self.name = name
        self.marks = marks

    def setId(self, id):
        self.id = id
        
    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

    def printTopper(students):
        marks = -1.0
        name = "Null"
        for student in students:
            if student.marks > marks:
                name = student.name
                marks = student.marks
        
        print(f"{name} is the top student with marks: {marks}")


if __name__ == "__main__":

    students = []
    student1 = Student(1, "Bob", 3.5)
    students.append(student1)
    student2 = Student(2, "Tom", 2.3)
    students.append(student2)
    student3 = Student(3, "John", 3.9)
    students.append(student3)

    Student.printTopper(students)
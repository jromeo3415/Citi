class Employee:
    def __init__(self, id, name, salary, Department):
        self.id = id
        self.name = name
        self.salary = salary
        self.Department = Department

class Department:
    def __init__(self, deptId, name):
        self.deptId = deptId
        self.name = name

def printEmployees(empList):
    for employee in empList:
        print(f"ID: {employee.id}, Name: {employee.name}, Salary: {employee.salary}, Department: {employee.Department.name}")
    
    print("All employees printed! \n")

def deleteEmployee(empList, name):
    for employee in empList:
        if employee.id == id:
            empList.remove(employee)
            print(f"Removed {name} from employee list \n")

def modEmployee(empList, id, name, salary, Department):
    for employee in empList:
        if id == employee.id:
            if name:
                employee.name = name
            if salary:
                employee.salary = salary
            if Department:
                employee.Department = Department

def departmentCount(empList):
    #   dict for departments
    deptList = {}

    #   going through each employee
    for employee in empList:
        deptName = employee.Department.name

        #   incrementing count if department has been encountered
        if deptName in deptList:
            deptList[deptName] += 1

        #  create key for department if not in dict
        else:
            deptList[deptName] = 1

    #   printing the count for each department
    for dept in deptList:
        print(f"{dept}: {deptList[dept]}")

    print("Printed the count for all departments (my implementation)\n")

def departmentCountCounters(empList):
    deptCounts = Counter(employee.Department.name for employee in empList)

    print(deptCounts)
    print("Printed counts using Counter")


#   placed here for demonstration
from collections import Counter

if __name__ == "__main__":
    empList = []
    
    d1 = Department(1, "HR")
    d2 = Department(2, "Sales")

    e1 = Employee(1, "John", 10000.5, d1)
    empList.append(e1)

    e2 = Employee(2, "Sally", 3000000.34, d2)
    empList.append(e2)

    e3 = Employee(3, "Dave", 700034.5, d1)
    empList.append(e3)

    #printEmployees(empList)

    #deleteEmployee(empList, "Sally")

    #printEmployees(empList)

    #modEmployee(empList, 3, None, 23393.34, None)
    #modEmployee(empList, 1, None, None, d2)

    printEmployees(empList)

    departmentCount(empList)

    departmentCountCounters(empList)
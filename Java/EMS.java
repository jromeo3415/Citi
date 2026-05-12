import java.util.*;

public class EMS {
    public static void main(String[] args){
        System.out.println("Employee Management System");
        ArrayList<Employee> empList = new ArrayList<>();
        Employee[] empArr = new Employee[5];
        Department d1 = new Department(1, "HR");
        Employee e1 = new Employee(100, "John", 1000.30, d1);

        List<Employee> emplisttt = new ArrayList<>();
        emplisttt.add(e1);

        displayAllEmployees(emplisttt);
        //populate(emplisttt);
    }

    /*private static void populate(List<Employee> emplisttt) {
        Department d1 = new Department(1, "HR");

        
        
    }*/

    public static void displayAllEmployees(List<Employee> empListtt) {
        for(Employee emp:empListtt) {
            System.out.println(emp);
        }
    }
}

class Employee {
    private int id;
    private String name;
    private double salary;
    private Department dept;

    public Employee(int id, String name, double salary, Department dept) {
        this.id = id;
        this.name = name;
        this.salary = salary;
        this.dept = dept;
    }

    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public double getSalary() {
        return salary;
    }
    public void setSalary(double salary) {
        this.salary = salary;
    }
    public Department getDept() {
        return dept;
    }
    public void setDept(Department dept) {
        this.dept = dept;
    }

	@Override
	public String toString() {
		return "Employee [id=" + id + ", name=" + name + ", salary=" + salary + ", dept=" + dept + "]";
	}

    
}

class Department {
    private int id;
    private String deptName;

    public Department(int id, String deptName) {
        this.id = id;
        this.deptName = deptName;
    }

    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getDeptName() {
        return deptName;
    }
    public void setDeptName(String deptName) {
        this.deptName = deptName;
    }
}

class 
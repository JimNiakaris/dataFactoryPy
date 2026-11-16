class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def get_details(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary:.2f}")


# Manager inherits everything from Employee
class Manager(Employee):
    # increases the salary of the employee passed in by 10%
    def promote(self, employee: Employee):
        employee.salary = employee.salary * 1.10


class Developer(Employee):
    def __init__(self, name: str, position: str, salary: float, programming_language: str):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    #overload
    def get_details(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary:.2f}, Language: {self.programming_language}")


manager = Manager("Eleni", "Manager", 1500)
developer1 = Developer("Kostas", "Developer", 1400, "C#")
developer2 = Developer("Vasilis", "Developer", 1350, "Typescript")

manager.get_details()
developer1.get_details()
developer2.get_details()

manager.promote(developer1)
manager.promote(developer2)

print("After promotion:")
developer1.get_details()
developer2.get_details()
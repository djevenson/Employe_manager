from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeRepo


class AddEmployerInput:
    def __init__(self, name:str, email: str, salary:int, post:str):
        self.name = name
        self.email = email
        self.salary = salary
        self.post = post

class AddEmployerOutput:
    def __init__(self, employer: Employer, message = str, status=bool):
        self.employer = employer
        self.message = message
        self.status = status

class AddEmployer:
    def __init__(self,repository: EmployeRepo) -> None:
        self.repository = repository

    def execute(self, input_data:AddEmployerInput) -> AddEmployerOutput:
        try:
            employee = Employee(
                name = input_data.name, email = input_data.email, post = input_data.post,salary = input_data.salary
            )
        except ValueError:
            return AddEmployerOutput("Connot add Employer retcheck the informations", None, False)
        employee = EmployerRepository.add_employee(employee)
        return AddEmployerOutput("Employee added successfully", employee, True)



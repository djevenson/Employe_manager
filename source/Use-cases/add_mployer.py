from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeRepo
from dataclasses import dataclass
from typing import Optional



@dataclass
class AddEmployerInput:
    name : str
    email : str
    salary : int
    post : str


@dataclass
class AddEmployerOutput:
    employer : Optional[Employee]
    message : str
    status : bool

class AddEmployer:
    def __init__(self,repository: EmployeRepo) -> None:
        self.repository = repository

    def execute(self, input_data:AddEmployerInput) -> AddEmployerOutput:
        employee = None
        try:
            employee = Employee(
                name = input_data.name, 
                email = input_data.email, 
                post = input_data.post,
                salary = input_data.salary
            )
        except ValueError:
            return AddEmployerOutput(
                message="Connot add Employer retcheck the informations", 
                Employee=None, 
                status=False
                )
        employee = self.repository.add_employee(employee)
        return AddEmployerOutput(
            message="Employee added successfully", 
            employee=employee, 
            status=True
        )



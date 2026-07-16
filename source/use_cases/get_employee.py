from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass
from typing import Optional


@dataclass
class GetEmployeeInput:
    id: int


@dataclass
class EmployeeOutput:
    employee : Optional[Employee]
    status : bool
    message : str = ""


class GetEmployee:
    def __init__(self, repository:EmployeeRepo):
        self.repository = repository

    def execute(self, input_data: GetEmployeeInput) -> EmployeeOutput:
        employee = self.repository.get_employee(input_data.id)
        if employee is None:
            return EmployeeOutput(
                message="Employee not found",
                employee = None,
                status = False
            )
        else:
            return EmployeeOutput(employee = employee, status = True)
from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass
from typing import Optional


@dataclass
class GetEmployeeInput:
    name: str
    def __post_init__(self):
        self.name = self.name.strip()


@dataclass
class EmployeeOutput:
    employee : Optional[Employee]
    status : bool
    message : str = ""


class GetEmployee:
    def __init__(self, repository:EmployeeRepo):
        self.repository = repository

    def execute(self, input_data: GetEmployeeInput) -> EmployeeOutput:
        employee = self.repository.get_employee(input_data.name)
        if not employee:
            return EmployeeOutput(
                message="Employee not found",
                employee = None,
                status = False
            )
        return EmployeeOutput(employee = employee, status = True)